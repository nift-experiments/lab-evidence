#!/bin/sh
# Run ONLY after parent provisioning authorization, before certification/timing.
set -eu
: "${SUITE:?build-systems or task-runners required}"
mkdir -p work /opt/refresh-tools/bin /opt/refresh-tools/sources
if [ "$SUITE" = task-runners ]; then
 mkdir -p work/tools
 cp docs/tools-package.json work/tools/package.json
 cp docs/tools-package-lock.json work/tools/package-lock.json
 (cd work/tools && npm ci --no-audit --no-fund)
 cc -O2 scripts/measure.c -o work/measure
 cc -O2 scripts/tiny-body.c -o work/tiny-body
 work/tools/node_modules/.bin/turbo --version
 work/tools/node_modules/.bin/nx --version
else
 cd /opt/refresh-tools/sources
 curl -fL https://ftp.gnu.org/gnu/make/make-4.4.1.tar.gz -o make-4.4.1.tar.gz
 echo 'dd16fb1d67bfab79a72f5e8390735c49e3e8e70b4945a15ab1f81ddb78658fb3  make-4.4.1.tar.gz' | sha256sum -c -
 tar -xzf make-4.4.1.tar.gz
 (cd make-4.4.1 && ./configure --prefix=/opt/refresh-tools && make -j4 && make install)
 curl -fL https://github.com/ninja-build/ninja/releases/download/v1.13.2/ninja-linux.zip -o ninja-1.13.2.zip
 echo '5749cbc4e668273514150a80e387a957f933c6ed3f5f11e03fb30955e2bbead6  ninja-1.13.2.zip' | sha256sum -c -
 unzip -o ninja-1.13.2.zip -d /opt/refresh-tools/bin
 chmod +x /opt/refresh-tools/bin/ninja
 /opt/refresh-tools/bin/make --version
 /opt/refresh-tools/bin/ninja --version
 sha256sum /opt/refresh-tools/bin/make /opt/refresh-tools/bin/ninja
fi

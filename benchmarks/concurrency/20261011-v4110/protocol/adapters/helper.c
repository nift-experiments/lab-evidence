#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(int argc,char **argv){if(argc!=4)return 64;long id=strtol(argv[1],0,10),ms=strtol(argv[2],0,10),code=strtol(argv[3],0,10);struct timespec t={ms/1000,(ms%1000)*1000000};nanosleep(&t,0);printf("%ld\n",id*17+3);return (int)code;}

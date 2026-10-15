bool write_readonly_file(const fs::path& path, const std::string& contents, fs::perms mode) {
    ensure_parent_directory(path);
    remove_stale_temporaries(path);
    // A forced full build still renders and validates every page, but replacing
    // byte-identical files would pay an unnecessary temp-write + rename cost.
    // Refreshing the mtime preserves the build-current marker used by modified
    // mode while avoiding filesystem churn. Any content change still takes the
    // transactional path below and therefore retains last-good interruption
    // safety. If touching is unsupported, fall back to the transactional write.
    if (file_contents_equal(path, contents)) {
        if ((is_readonly(path) || apply_mode(path, mode)) && refresh_modified_time(path)) return true;
    }
    const fs::path temp = temporary_sibling(path);
    if (!write_temp_file(temp, contents)) {
        std::error_code cleanup;
        fs::remove(temp, cleanup);
        return false;
    }
    if (!apply_mode(temp, mode)) {
        std::error_code cleanup;
        fs::remove(temp, cleanup);
        return false;
    }
    return replace_file_atomic(temp, path);
}


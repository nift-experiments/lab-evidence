        output += "]}";
    }
    output += "\n}\n";

    // Certification metadata uses the existing atomic readonly replacement.
    return filesystem::write_readonly_file(info_path(info), output);
}


class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return the file extension (including .)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    ### TODO
    # static get_directory - extracts directory path
    # static get_basename - extracts the file or directory name

# Usage
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("image.png"))
print(PathUtils.get_extension("file"))
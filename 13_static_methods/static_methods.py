class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return the file extension (including .)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    ### TODO
    # static get_directory - extracts directory path
    @staticmethod
    def get_directory(path):
        return path[:path.rfind("/")] if "/" in path else ""
    # static get_basename - extracts the file or directory name
    @staticmethod
    def get_basename(file):
        return file[file.rfind("/") + 1 : file.rfind(".")] if "/" and "." in file else ""

# Usage
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("image.png"))
print(PathUtils.get_extension("file"))

print(PathUtils.get_directory("Users/ikorb/school/COP2080/PythonProgramming/13_static_methods/static_methods.py"))
print(PathUtils.get_basename("Users/ikorb/school/COP2080/PythonProgramming/13_static_methods/static_methods.py"))
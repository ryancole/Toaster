import os
import os.path
import shutil

class StaticFile:

    modification_times = {}

    def __init__(self, site, base, dir, name):
        """
        Creates a new StaticFile.
            site is the Site object
            base is the String path to the source
            dir is the String path between the source and the file
            name is the String filename of the file
        """
        self.site = site
        self.base = base
        self.dir = dir
        self.name = name

    def path(self):
        """
        Obtains the source file path.
        """
        return os.path.join(self.base, self.dir, self.name)
    
    def destination(self, dest):
        """
        returns the destination path.
        """
        return os.path.join(dest, self.dir, self.name)

    def mtime(self):
        """
        Checks the modification time for the file.
        """
        return os.path.getmtime(self.path)

    def is_modified(self):
        """
        returns true if the path has been modified since the last write.
        """
        return StaticFile[path] != self.mtime
        
    def write(self, dest):
        """
        Writes the static files directory to the destination path if the 
        modification times are different and the destination directory doesn't
        already exist.

        Returns false if no copying is performed.
        """
        dest_path = self.destination(dest)

        if os.path.exists(dest_path) and not self.is_modified():
            return false

        StaticFile.modification_times[path] = mtime

        os.makedirs(os.path.dirname(dest_path))
        # Just shutil.copyfile here.  Possibly more efficent to use shutil.copy
        # but it would impare the utility for copying files without a parent
        # directory.
        shutil.copyfile(path, dest_path)

        return true

    def reset_cache(self):
        """
        Reset the modification_times dictionary (for testing purposes only)
        """
        StaticFiles.modificiation_times = {}



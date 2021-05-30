import os
import shutil

from Filters import RegexFilter

class ManagerFiles:

    def __init__(self, groupers, filters=None):
        self.filters = filters
        self.groupers = groupers
    
    def organize(self, path):
        files = self.get_files_names(path) 
        for f in files:
            _ , ext = os.path.splitext(f)
            dir_folder = f"{path}/{ext.replace('.','')}"

            if not os.path.isdir(dir_folder):
                os.mkdir(dir_folder)
            
            shutil.move(f"{path}/{f}", f"{dir_folder}/{f}")

    def get_files_names(self, path):
        if not os.path.isdir(path):
            raise Exception("Invalid path")
        
        file_names = []
        for file_name in os.listdir(path=path):
            if not self.filters or all(f.match(file_name) for f in self.filters):
                file_names.append(file_name)

        return file_names

if __name__=="__main__":
    pass
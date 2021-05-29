import os
import shutil

class GroupByFiles:
    
    def by_extension(self, path):
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
        
        return os.listdir(path=path)

if __name__=="__main__":
    pass
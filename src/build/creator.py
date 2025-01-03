from os import path, makedirs
from src.utils.logger import Log
from src.data.var import files, folders, configDataDefault

class Creator:
    def __init__(self):
        Log.log("Creator started.")
        self.create_folder(folders["config"])
        self.create_folder(folders["logs"])
        self.create_file(files["config"], configDataDefault)

    def create_file(self, file, data={}):
        try:
            if path.exists(file):
                Log.log(f"File {file} already exists.")
                return None
            import json
            with open(file, "w") as f:
                if not data:
                    data = {}
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def create_folder(self, folder):
        try:
            if path.exists(folder):
                return None
            makedirs(folder)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
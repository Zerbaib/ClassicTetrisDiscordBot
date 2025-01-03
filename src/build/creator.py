from os import path, makedirs
from src.utils.logger import Log
from src.data.var import files, folders, configDataDefault

class Creator:
    def __init__(self):
        self.create_folder(folders["config"])
        self.create_folder(folders["logs"])
        self.create_file(files["config"], configDataDefault)

    def create_file(self, file, data={}):
        try:
            if path.exists(file):
                return Log.log(f"File {file} already exists.")
            import json
            with open(file, "w") as f:
                if not data:
                    data = {}
                json.dump(data, f, indent=4)
            return Log.info(f"File {file} created.")
        except Exception as e:
            Log.error(f"Error on create file: {file}")
            Log.error(e)
            return

    def create_folder(self, folder):
        try:
            if path.exists(folder):
                return Log.log(f"Folder {folder} already exists.")
            makedirs(folder)
            return Log.info(f"Folder {folder} created.")
        except Exception as e:
            Log.error(f"Error on create folder: {folder}")
            Log.error(e)
            return
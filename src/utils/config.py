from src.data.var import files
from src.utils.logger import Log


def get_config(index: str):
    try:
        import json
        with open(files["config"], "r") as f:
            data = json.load(f)
            return data[index]
    except Exception as e:
        Log.error(f"Error on get config: {index}")
        Log.error(e)
        return
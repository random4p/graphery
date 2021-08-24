from pandas import DataFrame, read_csv, read_json
import json.decoder


class DataManager:
    def __init__(self, file=None, file_type=None):
        if file_type == "csv":
            self.data = read_csv(file)
        elif file_type == "txt":
            self.data = file.readlines()
        elif file_type == "json":
            self.data = json.load(file)




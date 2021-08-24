from pandas import DataFrame, read_csv, read_json, read_fwf
import json.decoder


class DataManager:
    def __init__(self, file=None, file_type=None):
        if file_type == "csv":
            tmp = read_csv(file)
            self.data = DataFrame.from_dict(tmp)

        elif file_type == "txt":
            tmp = read_csv(file, delimiter=",")
            self.data = DataFrame.from_dict(tmp)

        elif file_type == "json":
            tmp = json.load(file)
            self.data = DataFrame.from_dict(tmp)

        else:
            print("Your file type is not supported!")





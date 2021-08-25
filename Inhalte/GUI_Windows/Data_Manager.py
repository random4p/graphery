from pandas import DataFrame, read_csv
import json

# -------------------------------DATABASE-------------------------------------#


# ----------------------------DATA_MANAGEMENT---------------------------------#
class DataManager:
    def __init__(self, file=None, file_type=None, name=None):
        self.name = name
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




from pandas import DataFrame, read_csv, read_sql_table
import json

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

type_of_data = ["categorical", "numerical-finite", "numerical-infinite", "continuous", "qualitative-nominal",
                "qualitative-ordinal", "quantitative-interval", "quantitative-ratios"]


# ----------------------------DATA_MANAGEMENT---------------------------------#
class DataManager:
    def __init__(self, file=None, file_type=None, name=None, mode="import"):
        self.name = name
        self.version_list = []
        self.version_list.append(self.name)

        # import mode -- data in dataframe can be used by using self.data
        if mode == "import":
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

            try:
                self.engine = create_engine(f"sqlite:///Database/{self.name}.db")
                # self.engine = create_engine(f"sqlite:///Inhalte/GUI_Windows/Database/{self.name}.db", echo=True)
                self.data.to_sql(self.name, self.engine)
                print("Data was loaded into the database.")
            except FileExistsError:
                print("The file already exists!")

        # open mode -- data is loaded from the sql database into dataframe
        elif mode == "open":
            try:
                self.engine = create_engine(f"sqlite:///Database/{self.name}.db")
                # self.engine = create_engine(f"sqlite:///Inhalte/GUI_Windows/Database/{self.name}.db", echo=True)
                self.data = read_sql_table(self.name, self.engine)
            except FileNotFoundError:
                print("File could not be found.")

    def get_DataFrame_cl(self):
        return list(self.data.columns.values)

    def get_DataFrame(self):
        return self.data

    def create_new_sql_table(self, name):
        if name in self.version_list:
            engine = create_engine(f"sqlite:///Database/{self.name}.db")
            base = declarative_base()
            metadata = MetaData()
            metadata.reflect(bind=engine)
            table = metadata.tables.get(name)
            base.metadata.drop_all(engine, [table])

        engine = create_engine(f"sqlite:///Database/{self.name}.db")
        # engine = create_engine(f"sqlite:///Inhalte/GUI_Windows/Database/{self.name}.db", echo=True)
        self.data.to_sql(name, self.engine)
        print("Data was loaded into the database.")


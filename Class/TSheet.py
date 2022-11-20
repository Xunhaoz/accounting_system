import pandas as pd
import warnings


class TSheet:
    def __init__(self, title):
        self.title = title  # self.title : __init__的物件  、 title :負責接收傳入的參數
        self.summary = 0
        self.data = pd.DataFrame({"Debit": [], "Credit": []})

    def debit(self, monetary):
        self.data = self.data.append({"Debit": monetary, "Credit": 0}, ignore_index=True)

    def credit(self, monetary):
        self.data = self.data.append({"Debit": 0, "Credit": monetary}, ignore_index=True)




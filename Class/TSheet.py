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

    # axis=0:row 、axis=1:column
    def get_balance(self):
        if self.data.empty:
            return "T-Sheet is Empty"

        if len(self.data.index) == 1:
            a, b = self.data['Debit'].iloc[0], self.data['Credit'].iloc[0]
            balance = int(a) - int(b)
            return f"Credit: {-balance}" if balance < 0 else f"Debit: {balance}"

        balance = int(self.data.sum(axis=0)[0]) - int(self.data.sum(axis=0)[1])
        return f"Credit: {-balance}" if balance < 0 else f"Debit: {balance}"

    def get_for_pos(self):
        if self.data.empty:
            return 0

        if len(self.data.index) == 1:
            a, b = self.data['Debit'].iloc[0], self.data['Credit'].iloc[0]
            balance = int(a) - int(b)
            return -balance if balance < 0 else balance

        balance = int(self.data.sum(axis=0)[0]) - int(self.data.sum(axis=0)[1])
        return -balance if balance < 0 else balance

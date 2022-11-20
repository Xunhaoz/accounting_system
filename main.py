import json
import warnings

import pandas as pd
from pandas.io.formats.style import Styler
from Class.TSheet import TSheet
from Class.Global import Global

warnings.filterwarnings('ignore')

if __name__ == "__main__":
    with open('src/acountings.json', 'r') as f:
        accounting_dict = json.load(f)  # json轉成dict

    for accounting in accounting_dict['accounting']:
        accounting_dict[accounting] = TSheet(accounting)

    while True:
        command = input("系統指令：")
        if command == "accounting":
            command_code = input("請輸入會計代碼: \n")
            monetary = input("請輸入金額: \n")

            for accounting in Global.code[command_code]['debit']:
                accounting_dict[accounting].debit(monetary)

            for accounting in Global.code[command_code]['credit']:
                accounting_dict[accounting].credit(monetary)
        elif command == "list":
            for title in accounting_dict['accounting']:
                print(accounting_dict[title].title)
                print(accounting_dict[title].get_balance())
                print()
        elif command == "financial_position":
            df = pd.DataFrame({"Subject": [], "Monetary": []})
            df = df.append({"Subject": "短期資產", "Monetary": None}, ignore_index=True)
            df = df.append({"Subject": "    現金", "Monetary": accounting_dict["Cash"].get_for_pos()}, ignore_index=True)
            df = df.append({"Subject": "    應收帳款", "Monetary": accounting_dict["Accounts Receivable"].get_for_pos()},
                           ignore_index=True)
            df = df.append({"Subject": "    存貨", "Monetary": accounting_dict["Inventory"].get_for_pos()},
                           ignore_index=True)
            df = df.append({"Subject": "    銷貨成本", "Monetary": accounting_dict["Cost of Goods Sold"].get_for_pos()},
                           ignore_index=True)
            df = df.append({"Subject": "長期資產", "Monetary": None}, ignore_index=True)
            df = df.append({"Subject": "    應付票據", "Monetary": accounting_dict["Notes Payable"].get_for_pos()},
                           ignore_index=True)
            df = df.append({"Subject": "    資產", "Monetary": df.sum(axis=0)[1]},
                           ignore_index=True)

            df.to_csv('financial_position.csv', encoding='utf-8-sig')
            print(df)

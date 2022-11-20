import json
import pprint
import warnings

from Class.TSheet import TSheet
from Class.Global import Global

warnings.filterwarnings('ignore')

if __name__ == "__main__":

    with open('src/acountings.json', 'r') as f:
        accounting_dict = json.load(f)  # json轉成dict

    for accounting in accounting_dict['accounting']:
        accounting_dict[accounting] = TSheet(accounting)

    while True:
        command_code = input("請輸入會計代碼: \n")
        monetary = input("請輸入金額: \n")

        for accounting in Global.code[command_code]['debit']:
            accounting_dict[accounting].debit(monetary)
            print(accounting, accounting_dict[accounting].data)

        # print(Global.code[command_code], monetary)

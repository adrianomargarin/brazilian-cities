# -*- coding:utf-8 -*-

import json
from xlrd import open_workbook

STATE_TRANSLATE = {
    u'11': u'RO',
    u'12': u'AC',
    u'13': u'AM',
    u'14': u'RR',
    u'15': u'PA',
    u'16': u'AP',
    u'17': u'TO',
    u'21': u'MA',
    u'22': u'PI',
    u'23': u'CE',
    u'24': u'RN',
    u'25': u'PB',
    u'26': u'PE',
    u'27': u'AL',
    u'28': u'SE',
    u'29': u'BA',
    u'31': u'MG',
    u'32': u'ES',
    u'33': u'RJ',
    u'35': u'SP',
    u'41': u'PR',
    u'42': u'SC',
    u'43': u'RS',
    u'50': u'MS',
    u'51': u'MT',
    u'52': u'GO',
    u'53': u'DF'
}

def main():

    lista = []
    arquivo = open_workbook("database_ibge_2013.xls")
    sheet = arquivo.sheet_by_name('dtb_2013')

    for nrow in range(1, sheet.nrows):
        data = {
            "state_acronym": STATE_TRANSLATE[sheet.col_values(0)[nrow]],
            "state_name": sheet.col_values(1)[nrow],
            "state_code": sheet.col_values(0)[nrow],
            "city_code": sheet.col_values(0)[nrow] + sheet.col_values(6)[nrow],
            "city_name": sheet.col_values(7)[nrow],
        }
        lista.append(data)

    arquivo_json = open('cities.json', 'wr')
    arquivo_json.write(json.dumps(lista))
    arquivo_json.close()

if __name__ == "__main__":
    main()

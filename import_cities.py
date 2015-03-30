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

    aux_list = []
    file = open_workbook("database_ibge_2013.xls")
    sheet = file.sheet_by_name('dtb_2013')

    add_number = 0
    for nrow in range(1, sheet.nrows):
        data = {}
        data["state"] = STATE_TRANSLATE[sheet.col_values(0)[nrow]]
        data["city_code"] = sheet.col_values(0)[nrow] + sheet.col_values(6)[nrow]
        data["city_name"] = unicode(sheet.col_values(7)[nrow])

        if data not in aux_list:
            add_number += 1
            aux_list.append(data)
            print u"%s - Cidade %s adicionada com sucesso!" % (add_number, data["city_name"])

    print u"%s cidades adicionadas!" % add_number

    json_file = open('cities.json', 'wr')
    json_file.write(json.dumps(aux_list))
    json_file.close()

if __name__ == "__main__":
    main()

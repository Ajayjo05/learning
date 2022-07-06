import csv
from itertools import count
import pandas as pd
import os
import csv
import sqlalchemy
import datetime
import pandas as pd
import numpy as np
from datetime import datetime, date
import re

# get data and convert csv form
# data base connection
# now = datetime.now()
# engine = sqlalchemy.create_engine("postgresql://postgres:password@172.17.0.1:5432/testing")
# derr = pd.read_sql_table('data_extractor_regex_rules', engine)
# os.makedirs('DB', exist_ok=True)
# # create csv with date and time
# derr.to_csv(f'DB/export_{now.strftime("%Y.%m.%d")}_to_{now.strftime("%H.%M")}.csv',date_format='%Y-%m-%d %H:%M:%S', encoding='utf-8', index=False)
# # print(x)
# get id from old csv and new csv
new_data = pd.read_csv('new.csv')
old_data = pd.read_csv('old.csv')
# breakpoint()
new = new_data['id'].tolist()  # id convert into list
le = len(new)
# csv code
new_csv = open("new.csv")
old_csv = open("old.csv")
# csv data convert into dictionary  objects
new_records = csv.DictReader(new_csv)
old_records = csv.DictReader(old_csv)


# return old object to dictionary
def newCsv_data(n):
    for i in n:
        return i


# return new object to dictionary
# def oldCsv_data(n,id):
#     # print("Object ======================",n)
#     for i in n:
#         # breakpoint()
#         # print("Data =======================",i)
#         # print("-------------->",id)
#         # breakpoint()
#         if i['id'] == id:
#             # print("123================",i)
#             return i
#     return False
# test
def oldCsv_data(old, id, new_obj):
    # for x in new_obj:
    #     print("Object id======================",x['id'])
    #     for i in old:
    #         # breakpoint()
    #         print("Data =======================",i['id'])
    #         # print("-------------->",x['id'])
    #         # breakpoint()
    #         if i['id'] == x['id']:
    #             # print("123================",i)
    #             return i
    #     return False
    for x in old:
        # print("Object id======================",x['id'])
        for i in new_obj:
            # breakpoint()
            # print("Data =======================",i['id'])
            # print("-------------->",x['id'])
            # breakpoint()
            if i['id'] == x['id']:
                # print("123================",i)
                return i
        return False


today = datetime.today()
upFile = open("Up_migration_" + str(today) + ".sql", "a")
downFile = open("Down_migration_" + str(today) + ".sql", "a")


def csv_creator_up(final_up):
    upFile.write("\n\n")
    upFile.write(final_up)


def csv_creator_down(final_down):
    downFile.write("\n\n")
    downFile.write(final_down)


def up_migartion(set_data_new, set_data_old):
    final_up = "UPDATE TABLE SET " + set_data_new + " WHERE " + set_data_old + ";"
    final_where = re.sub("(?i)([\,]+)(?=\s+where)", '', final_up)
    final = re.sub("(?i)(and\s?)(?=\s*?\;$)", '', final_where)
    csv_creator_up(final)


def down_migartion(set_data_set, set_data_where):
    set = re.sub('(?i)(?<=\'\s\s)(and)(?=\s?\w)', ',', set_data_set)
    where = re.sub('(?i)(?<=\'\s\s)(\,)(?=\s?\w)', 'and', set_data_where)
    final_down = "UPDATE TABLE SET " + set + " WHERE " + where + ";"
    final_where = re.sub("(?i)(and)(?=\s+where)", '', final_down)
    final = re.sub("(?i)(\,\s?)(?=\s*?\;$)", '', final_where)
    csv_creator_down(final)


def creator(le, new_records, old_records):
    set_data_new = " "
    set_data_old = " "
    final_up = " "
    for i in range(le):
        set_data_new = " "
        set_data_old = " "
        final_up = " "
        # print("+++++++++++++++++=length",le)
        new_dict_data = newCsv_data(new_records)
        # print("===================>", new_dict_data['id'])
        # breakpoint()
        old_dict_data = oldCsv_data(old_records, new_dict_data['id'], new_records)
        # print("Return Obj ============================",old_dict_data)
        if False:
            # print(new_dict_data['id'])
            # if new_dict_data['id'] == old_dict_data['id']:
            update_flag = False
            value_and = " and "
            value_comma = " , "
            for csv_old_key, csv_old_value in old_dict_data.items():
                if new_dict_data[csv_old_key] != csv_old_value:
                    if csv_old_key == 'valid_pages' or csv_old_key == 'value_position' or csv_old_key == 'key_position':
                        new_v = re.sub(
                            "(?i)(\')", '', new_dict_data[csv_old_key])
                        old_v = re.sub(
                            "(?i)(\')", '', old_dict_data[csv_old_key])
                        new_dict_data[csv_old_key] = new_v
                        old_dict_data[csv_old_key] = old_v
                    update_flag = True
                    set_data_new = set_data_new + csv_old_key + "=" + "'" + \
                                   str(new_dict_data[csv_old_key]) + "'" + value_comma
                    set_data_old = set_data_old + csv_old_key + "=" + \
                                   "'" + str(old_dict_data[csv_old_key]) + "'" + value_and
            if update_flag:
                up_migartion(set_data_new, set_data_old)
                down_migartion(set_data_old, set_data_new)
        else:
            insert_key = ""
            insert_value = ""
            final_insert = ""
            for key, value in new_dict_data.items():
                print(type(value))
                if key == "id" and value == new_dict_data['id']:
                    pass
                    # print("Value==============",value)
                    # new_dict_data.pop(new_dict_data['id'])
                    # print(key+"========"+new_dict_data['id'])
                # print(key)
                # print(value)
                insert_key = insert_key + key + " , "
                insert_value = insert_value + value + ","
            insert_key = re.sub("(?i)(\,\s)$", '', insert_key)
            # print("insert ===============",insert_key)
            insert_value = re.sub("(?i)(\,)$", '', insert_value)
            # print(insert_key)
            final_insert = "INSERT INTO public.data_extractor_regex_rules(" + insert_key + ") VALUES(" + insert_value + ');'
            # pass
            # print(final_insert)


'''INSERT INTO public.data_extractor_regex_rules(doc_type, field_name, enabled, valid_pages, rule_priority, 
source_page_resolution, "key_type", key_regex, key_position, key_level, value_type, value_data_type, value_regex, 
value_position, capture_regex, format_regex, top_limiter, bottom_limiter, left_limiter, right_limiter, capture_index, 
confidence_score, config_set, capture_multiple_value) VALUES('{"Deed of trust"}', 'deed_type', true, '{0,1}', 11, 
200, 'variable', '(?i)MORT|FLORIDA\sOPEN\WE', '{18,12,1686,931}', 'line', 'text', 'string', 
'(?i)(?:FLORIDA\sOPEN\WEND)\s[\w]+\s\W\w+\s\w+\s\w+\W|(?:MORTGAGE)\s\W[\w]+\s\w+\s\w+\W', '{18,12,1686,931}', 
'Data]', '', NULL, NULL, NULL, NULL, 0, 70, 'default', false); '''
'''INSERT INTO public.data_extractor_regex_rules(id , doc_type , field_name , enabled , valid_pages , rule_priority , 
source_page_resolution , key_type , key_regex , key_position , key_level , value_type , value_data_type , value_regex 
, value_position , capture_regex , format_regex , top_limiter , bottom_limiter , left_limiter , right_limiter , 
capture_index , confidence_score , config_set , capture_multiple_value ) VALUES(49,{"Deed of trust"},amount,true,
{all},1,200,variable,(?i)promissory note signed|the\scredit\slimit|DOLLARS\sand\sNO\sCENTS,{1489,1661,1774,1692},
line,text,string,(?i)([\d]{1,5}[\W][\d]{1,3}[\W][\d]{2}),{-1459,1658,2652,1820},(?i)^\W+,,,,,,0,70,default,false); '''
creator(le, new_records, old_records)

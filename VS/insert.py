import re
from datetime import date

import csv
global data
l = ['valid_pages,', 'key_regex,', 'value_regex,','capture_regex,', 'capture_index,', 'key_position,', 'value_position,']

table_name = "public.data_extractor_regex_rules"

def create_up(Old_ins, New_ins, table_name, l):
    global data

    id = re.findall("(?i)(?<=values\W)(\d+)", New_ins)
    key_data_new = re.findall("(?i)(?:\(id\,\s)(.*?)(?=\)\s?values)", New_ins)
    value_data_new = re.findall("(?i)(?:values[\W]\d+\,\s?)(.*?)(?=\W\;)", New_ins)

    key_data_old = re.findall("(?i)(?:\(id\,\s)(.*?)(?=\)\s?values)", Old_ins)
    value_data_old = re.findall("(?i)(?:values\([\d]+\,\s)(.*)(?=\;)", Old_ins)

    # Old Insert----------------------------------------------------------------------------------------
    key_old = ", ".join(key_data_old)
    val_old = ", ".join(value_data_old)

    key_list_old = key_old.split()
    value_list_old = val_old.split(", ")
    k_len = len(key_list_old)
    v_len = len(value_list_old)
    old_where_value = ''
    lin = len(l)
    for f in key_list_old:
        if f in l:
            index = key_list_old.index(f)
            value = value_list_old[index]

            if lin > 1:
                old_where_value = old_where_value + f + "="+value+" and "
            else:
                old_where_value = old_where_value + f + "="+value
            lin = lin-1

    insert_data = re.sub("(?i)(\,=)", "=", old_where_value)
    old_where_value = insert_data.replace(', ', ' ')
    # end Old Insert

    # New Insert
    key = ", ".join(key_data_new)
    val = ", ".join(value_data_new)

    key_list = key.split()
    value_list = val.split(", ")

    k_len = len(key_list)
    v_len = len(value_list)
    # code for choice fileds
    where_list = ['valid_pages,', 'key_regex,', 'value_regex,','capture_regex,', 'top_limiter,', 'bottom_limiter,', 'capture_index,']
    data = []
    print("""Choice Change Fileds : """, id)
    for field in where_list:
        print("Did You Change "+'"'+field+'"'+": Yes / No")
        choice = input()
        if 'yes' == choice:
            data.append(field)
    set_value = ''
    lin = len(data)
    for f in key_list:
        if f in data:
            index = key_list.index(f)
            value = value_list[index]
            if lin > 1:
                set_value = set_value + f + "="+value+","
            else:
                set_value = set_value + f + "="+value
            lin = lin-1

    insert_data = re.sub("(?i)(\,=)", "=", set_value)
    set_values = insert_data.replace(', ', ' ')

    for f in key_list:
        if f in data:
            index = key_list.index(f)
            value = value_list[index]
            key_list.pop(index)
            value_list.remove(value)

    if k_len == v_len:
        # str_table_name=re.search('(?i)(public.extractor_configs_old)(?=\s\()',string)
        final = "UPDATE " + table_name + " SET " + \
            set_values + " WHERE " + old_where_value + ";"
        # print("Up : ", final)
        return data, final
    else:
        print("Index Length Out of Range")


# Function for Down


def create_down(Old_ins, New_ins, table_name, data,l):

    key_data_old = re.findall("(?i)(?:\(id\,\s)(.*?)(?=\)\s?values)", Old_ins)
    value_data_old = re.findall("(?i)(?:values\([\d]+\,\s)(.*)(?=\;)", Old_ins)

    key_old = "''".join(key_data_old)
    val_old = "''".join(value_data_old)
    key_list_down_old = key_old.split()
    value_list_down_old = val_old.split(", ")

    set_value_down = ''
    k_len_down = len(key_list_down_old)
    v_len_down = len(value_list_down_old)

    len_down = len(data)
    for down in key_list_down_old:
        if down in data:
            index = key_list_down_old.index(down)
            value_old = value_list_down_old[index]
            if len_down > 1:
                set_value_down = set_value_down + down + "="+value_old+","
            else:
                set_value_down = set_value_down + down + "="+value_old
            len_down = len_down-1

    insert_data = re.sub("(?i)(\,=)", "=", set_value_down)
    set_value_down = insert_data.replace(', ', ' ')

    # end Old values Set

    key_data_new = re.findall("(?i)(?:\(id\,\s)(.*?)(?=\)\s?values)", New_ins)
    value_data_new = re.findall("(?i)(?:values\([\d]+\,\s)(.*)(?=\;)", New_ins)

    key_new_down = ", ".join(key_data_new)
    val_new_down = ", ".join(value_data_new)

    key_list_down_new = key_new_down.split()
    value_list_down_new = val_new_down.split(", ")

    new_where_value = ''
    lin = len(l)
    for new_down in key_list_down_new:
        if new_down in l:
            index = key_list_down_new.index(new_down)
            value_down = value_list_down_new[index]

            if lin > 1:
                new_where_value = new_where_value + new_down + "="+value_down+" and "
            else:
                new_where_value = new_where_value + new_down + "="+value_down
            lin = lin-1

    insert_data_where = re.sub("(?i)(\,=)", "=", new_where_value)
    new_where_value = insert_data_where.replace(', ', ' ')
    if k_len_down == v_len_down:
        # str_table_name=re.search('(?i)(public.extractor_configs_old)(?=\s\()',string)
        final_down = "UPDATE " + table_name + " SET " + \
            set_value_down + " WHERE " + new_where_value + ";"
        return final_down
        # print("Down : ", final_down)



def file_creator(up_migration, down_migration):
    today = date.today()

    upFile = open("Up_migration_"+str(today)+".sql", "a")
    upFile.write("\n\n")
    upFile.write(up_migration)
    # upFile.close()

    downFile = open("Down_migration_"+str(today)+".sql", "a")
    downFile.write("\n\n")
    downFile.write(down_migration)
    # downFile.close()


New_ins = []
with open("new_test.csv", 'r') as file_new:
    csvreader = csv.reader(file_new)
    for i in csvreader:
        New_ins.append('"""'+i[0]+'"""')
        # print(type(i))


Old_ins = []
with open("old_test.csv", 'r') as file_old:
    csvreader = csv.reader(file_old)
    for i in csvreader:
        Old_ins.append('"""'+i[0]+'"""')

for count in range(len(New_ins)):
    data, up_migration = create_up(Old_ins[count], New_ins[count], table_name,l)
    down_migration = create_down(Old_ins[count], New_ins[count], table_name, data,l)

    file_creator(up_migration, down_migration)
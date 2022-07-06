# Correct Code for UP and Down SQL
import re

New_ins = '''INSERT INTO public.data_extractor_regex_rules1
(id, doc_type, field_name, enabled, valid_pages, rule_priority, source_page_resolution, "key_type", key_regex, key_position, key_level, value_type, value_data_type, value_regex, value_position, capture_regex, format_regex, top_limiter, bottom_limiter, left_limiter, right_limiter, capture_index, confidence_score, config_set)
VALUES(14, 'Deed', 'vesting', true, '{"0"}', 5, 200, 'variable', '(?i)[\d]+,\sto', '{"38","1425","683","1555"}', 'line', 'text', 'string', '(?i)(?:[\d]+,\sto\s)(.*?)(?=hereinafter\scalled\sGrantee)', '{"-1600","700","2521","1967"}', '(\.|,|\.,)$|(^i\s*f)|\(\"Grantees\"\)|no|\(hereinafter|\#|DEED|\(\"Grantee\"\)\,|\,\s*Grantees|\(Grantees\)|yes|,\s*Grantee\(s\)\:|Marisa White\, party of the second part|the\ssaid|the Grantee|\*|Grantee|, 4|^and\s|Grantee:', '', NULL, '', NULL, NULL, 0, 70, 'default');'''
Old_ins = '''INSERT INTO public.data_extractor_regex_rules1
(id, doc_type, field_name, enabled, valid_pages, rule_priority, source_page_resolution, "key_type", key_regex, key_position, key_level, value_type, value_data_type, value_regex, value_position, capture_regex, format_regex, top_limiter, bottom_limiter, left_limiter, right_limiter, capture_index, confidence_score, config_set)
VALUES(14, 'Deed', 'vesting', true, '{"0","1"}', 10, 200, 'variable', '(?i)[\d]+,\sto', '{"38","1425","683","1555"}', 'line', 'text', 'string', '(?i)(?:[\d]+,\sto\s)(.*?)(?=hereinafter\scalled\sGrantee)', '{"-1600","700","2521","1967"}', '(\.|,|\.,)$|(^i\s*f)|\(\"Grantees\"\)|no|\(hereinafter|\#|DEED|\(\"Grantee\"\)\,|\,\s*Grantees|\(Grantees\)|yes|,\s*Grantee\(s\)\:|Marisa White\, party of the second part|the\ssaid|the Grantee|\*|Grantee|, 4|^and\s|Grantee:', '', NULL, '', NULL, NULL, 0, 70, 'default');'''
key = re.findall('(?i)(?:\(id\,\s)(.*?)(?=\)\svalues)', New_ins)
val = re.findall('(?i)(?:values\([\d]+\,\s)(.*)(?=\;)', New_ins)
value_position = re.findall("(?i)(\'\{\W+\d{1,4}\W\,\W+\d{1,4}\W\,\W+\d{1,4}\W\,\W+\d{1,4}\W\}\'\,\s)", New_ins)

old_key = re.findall('(?i)(?:\(id\,\s)(.*?)(?=\)\svalues)', Old_ins)
old_val = re.findall('(?i)(?:values\([\d]+\,\s)(.*)(?=\;)', Old_ins)
old_value_position = re.findall("(?i)(\'\{\W+\d{1,4}\W\,\W+\d{1,4}\W\,\W+\d{1,4}\W\,\W+\d{1,4}\W\}\'\,\s)", Old_ins)

# to convert regex obj into string join by " , "
N_k = ','.join(key)
N_v = ','.join(val)

Ok = ','.join(old_key)
Ov = ','.join(old_val)

# to convert data in list for UP
N_k = N_k.split()
# N_v=N_v.split(", ")
# N_v = N_v.split("/,(?=(?:(?:[^"]*"){2})*[^"]*$)/")
N_v = re.split(r',(?=")', N_v)

Ok = Ok.split()
Ov = Ov.split(", ")

l = ['key_regex,', 'valid_pages,', 'value_regex,', 'rule_priority,', 'capture_regex,', 'top_limiter,',
     'bottom_limiter,']
W_l = ['key_regex,', 'valid_pages,', 'value_regex,', 'rule_priority,', 'capture_regex,', 'key_position,',
       'value_position,']

# Choice for the fields changed
data = []
print("""Choice for Changed Fileds""")
for field in l:
    print("Did You Change " + '"' + field + '"' + ": Yes / No")
    choice = input()
    if 'yes' == choice:
        data.append(field)

# SET value for UP
set_value = ''
lin = len(data)
for i in N_k:
    if i in data:
        index = N_k.index(i)
        value = N_v[index]
        if lin > 1:
            set_value = set_value + i + "=" + value + ","
        else:
            set_value = set_value + i + "=" + value
        lin = lin - 1

insert_data = re.sub("(?i)(\,=)", "=", set_value)
set_values = insert_data.replace(', ', ' ')

# where for UP
where_value = ''
lin = len(W_l)
for i in Ok:
    if i in W_l:
        index = Ok.index(i)
        value = Ov[index]
        if lin > 1:
            where_value = where_value + i + "=" + value + " and "
        else:
            where_value = where_value + i + "=" + value + ";"
        lin = lin - 1
runner = re.sub('(?i)(\,=)', ' = ', where_value)
where_value = runner.replace(', ', ' ')

str_table_name = re.search(
    '(?i)(public.extractor_configs_old|public.platform_fields|public.data_extractor_regex_rules1)(?=\s\()', New_ins)
final_up = "UPDATE " + str_table_name[0] + " SET " + set_values + " WHERE " + where_value

# SET value for DOWN
set_value_down = ''
lin = len(data)
for i in Ok:
    if i in data:
        index = Ok.index(i)
        N_value = Ov[index]
        if lin > 1:
            set_value_down = set_value_down + i + "=" + N_value + ","
        else:
            set_value_down = set_value_down + i + "=" + N_value
        lin = lin - 1

insert_data = re.sub("(?i)(\,=)", "=", set_value_down)
set_values_down = insert_data.replace(', ', ' ')

# where for DOWN
where_value_down = ''
lin_down = len(W_l)
for j in N_k:
    if j in W_l:
        index = N_k.index(j)
        N_value = N_v[index]
        if lin_down > 1:
            where_value_down = where_value_down + j + "=" + N_value + " and "
        else:
            where_value_down = where_value_down + j + "=" + N_value + ";"
        lin_down = lin_down - 1
runner = re.sub('(?i)(\,=)', ' = ', where_value_down)
where_value_down = runner.replace(', ', ' ')

str_table_name = re.search(
    '(?i)(public.extractor_configs_old|public.platform_fields|public.data_extractor_regex_rules1)(?=\s\()', Old_ins)
final_down = "UPDATE " + str_table_name[0] + " SET " + set_values_down + " WHERE " + where_value_down

print(final_up)
print("\n")
print(final_down)

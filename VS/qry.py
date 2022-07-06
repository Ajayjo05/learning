import re
str= '''INSERT INTO public.data_extractor_regex_rules1
(id, doc_type, field_name, enabled, valid_pages, rule_priority, source_page_resolution, "key_type", key_regex, key_position, key_level, value_type, value_data_type, value_regex, value_position, capture_regex, format_regex, top_limiter, bottom_limiter, left_limiter, right_limiter, capture_index, confidence_score, config_set)
VALUES(42, 'Deed of trust', 'trustor', true, '{"1"}', 10, 200, 'fixed', '^TRS', '{"152","710","669","853"}', 'line', 'text', 'name', '(?i)(?:TRS.?.?.?.?\s?)(.*?)(?=.?.?and 426 west)', '{"152","710","669","853"}', '(\.|,|\.,)?$', '', NULL, NULL, NULL, NULL, 0, 70, 'default');'''
key = re.findall('(?i)(?:\(id\,\s)(.*?)(?=\)\svalues)', str)
val = re.findall('(?i)(?:values\([\d]+\,\s)(.*)(?=\;)', str)
value_position = re.findall("(?i)(\'\{\W\d{2,4}\W\,\W\d{2,4}\W\,\W\d{2,4}\W\,\W\d{2,4}\W\}\'\,\s)", str)

#to convert regex obj into string join by " , "
k=','.join(key)
v=','.join(val)

#to replace key and value position from column names with none
x=k.replace("key_position,","")
r_key=x.replace("value_position,","")

#to replace value position {123,456,456,789} from values
vp=v.replace(value_position[0],"")
r_value=vp.replace(value_position[1],"")

#to convert data in list
k=r_key.split()
v=r_value.split(", ")

# print(k)
# print("\n")
# print(v)
str1=''
for i in range(0,len(v)):
    if i!=len(v)-1:
        str1=str1+k[i]+"="+v[i]+" and "       
    else:
        str1=str1+k[i]+"="+v[i] + ";"
runner=re.sub('(?i)(\,=)',' = ',str1)
run=runner.replace(', ',' ')
str_table_name=re.search('(?i)(public.extractor_configs_old|public.platform_fields|public.data_extractor_regex_rules1)(?=\s\()',str)
final= "UPDATE " +str_table_name[0]+" SET "+" WHERE "+run

print(final)






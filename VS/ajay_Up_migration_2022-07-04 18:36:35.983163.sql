

UPDATE public.data_extractor_regex_rules SET  valid_pages = '{"vineet"}' , key_regex = (?i)promissory note signed|the\scredit\slimit|DOLLARS\sand\sNO\sCENTS , capture_regex = (?i)^\W+ ,  WHERE  valid_pages = '{"all"}' and key_regex = (?i)promissory note signed|the\scredit\slimit and capture_regex =  and ;

UPDATE public.data_extractor_regex_rules SET  key_regex = (?i)with credit limit|Dollars\s|The\sCredit\sLimit\sis ,  WHERE  key_regex = (?i)with credit limit|Dollars\s and ;

UPDATE public.data_extractor_regex_rules SET  valid_pages = '{"0","1","3"}' , key_regex = (?i)principal\ssum\sof|U\WS\W+|defined in the Agreement\W+of\W+? ,  WHERE  valid_pages = '{"0","1"}' and key_regex = (?i)principal\ssum\sof|U\WS\W+|defined in the Agreement\W+of\W+?(?i)principal\ssum\sof|U\WS\W+ and ;
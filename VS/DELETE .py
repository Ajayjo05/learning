DELETE FROM public.extractor_configs_old
WHERE "name"='recorded_requested_by' and doc_type='Deed' and key_regex='(?i)(requestor\W+|after\srecording\W+please\sreturn\sto\W+)' and value_regex='(?i)(?:requestor\W+|after\srecording\W+please\sreturn\sto\W+)(.*?)(?=\srecorded\sby|\s\d+\s\w)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE  "name"='apn' and doc_type='Deed' and key_regex='(?i)(apn\s?no\W+)' and value_regex='(?i)(?:apn\s?no\W+)([\d\-]+)(?=\s\w)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='stamp_value' and doc_type='Deed' and "key_type"='variable' and key_regex='(?i)(rptt\W+)' and value_regex='(?i)(?:rptt\W+)([\d\.?]+)(?=\s\w+)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='recorded_requested_by' and doc_type='Deed' and key_regex='(?i)(Recording\srequested\sby\W+|after\srecording\W+please\sreturn\sto\W+)' and value_regex='(?i)(?:Recording\srequested\sby\W+|after\srecording\W+please\sreturn\sto\W+)(.*?)(?=\swhen\srecorded|\s\d+\s\w)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='vesting' and doc_type='Deed' and key_regex='(?i)(the\s\Wgrantor\W+and\s)' and value_regex='(?i)(?:the\s\Wgrantor\W+and\s)(.*?)(?=\shaving\sa\smailing)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='property_address' and doc_type='Deed' and key_regex='(?i)(grantee\Ws\saddress\W\s|grant[ce]e\Ws\smailing\saddress\s|whose\saddress\sis\s|whose\spost\soffice\saddress\sis\W?\s|grantee\Ws\smailing\saddress\W?\s|by\sstreet\sand\snumber\sas\W+)' and value_regex='(?i)(?:grantee\Ws\saddress\W\s|grant[ce]e\Ws\smailing\saddress\s|whose\saddress\sis\s|whose\spost\soffice\saddress\sis\W?\s|grantee\Ws\smailing\saddress\W?\s|by\sstreet\sand\snumber\sas\W+)([\w\W]{15,80})(?=\skelly\sm|\sconsideration|\sthe\sfollowing|\shereinafter\scalled\sthe\sgrantee|lender\W|\s\Wwhether|\swith\sall)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='recorded_requested_by' and doc_type='Deed' and key_regex='(?i)(processed\sby\W?\s?|return\sto\W+)' and value_regex='(?i)(?:processed\sby\W?\s?|return\sto\W+)(.*?)(?=\sthis\spage|\sproperty)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='grantee' and doc_type='Deed' and key_regex='(?i)(grantee\s\(whether\sone\sor\smore\)\:\s|\"grantor\,\W+.*more\W+and)' and value_regex='(?i)(?:grantee\s\(whether\sone\sor\smore\)\:\s|\"grantor\,\W+.*more\W+and\s)(.*?)(?=\W\ssingle\sman|\s\W+grantee|\sbook\spage)' and config_set='Fluid';







DELETE FROM public.extractor_configs_old
WHERE "name"='grantee' and doc_type='Deed' and key_regex='(?i)(deed\swith.*to\s|hereby\sacknowledged\W)' and value_regex='(?i)(?:deed\swith.*to\s)(.*?)(?=\,\ssingle\sman)' and config_set='Fluid';



DELETE FROM public.extractor_configs_old
WHERE "name"='grantor' and doc_type='Deed' and key_regex='(?i)(presents\W+that\s1\W+|hereby\sacknowledged\W+|deed\swith.*from|co\W?trustees\sof\sthe\s|special\swarranty\sdeed|this\sindenture.*between|quitclaim\scovenants\sto\s|grantor\Ws\W+|grantor\W+|between\s|correction\sis\sas\sfollows\W+|made\sthe.*?by\s)' and value_regex='(?i)(?:presents\W+that\s1\W+|hereby\sacknowledged\W+|deed\swith.*from|co\W?trustees\sof\sthe\s|special\swarranty\sdeed|this\sindenture.*between|quitclaim\scovenants\sto\s|grantor\Ws\W+|grantor\W+|between\s|correction\sis\sas\sfollows\W+|made\sthe.*?by\s)(.*?)(?=\sto\s|\sjoint\srestated|\sgrantee\s\Wwhether|\W\shusband\sand|\W+individuals|\W+husband\sand\swife|grantee|\W+trustees\sof\sthe|\W+of\slancaster|\W+whose\sstreet|\W+a\sflorida)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='grantee' and doc_type='Deed' and key_regex='(?i)(whose\smailing\saddress\sis.*\d+\W\sand\s|and\squitclaims\sto\W\s+?)' and value_regex='(?i)(?:whose\smailing\saddress\sis.*\d+\W\sand\s|and\squitclaims\sto\W\s+?)(.*?)(?=\W\shusband\sand|\W?\strustee\Ws\W)' and config_set='Fluid';




DELETE FROM public.extractor_configs_old
WHERE "name"='grantor' and doc_type='Deed' and key_regex='(?i)(this\swarranty\sdeed\smade.*by\s|county.*that\s\d?\W?\s?|hereby\sacknowledged\W+|dated\sthis.*\W+by\s|grantor\W+|made\sbetween\s|considerations.*we\W+|by\sand\sbetween\s|made\sthis.*\sby\s)' and value_regex='(?i)(?:this\swarranty\sdeed\smade.*by\s|county.*that\s\d?\W?\s?|hereby\sacknowledged\W+|dated\sthis.*\W+by\s|grantor\W+|made\sbetween\s|considerations.*we\W+|by\sand\sbetween\s|made\sthis.*\sby\s)(.*?)(?=trustee\sunder|\sgrantee\W|\W+wife\sand|\W+hereinafter|\W+husband\sand\swife|\W?\s?a\ssingle|\W+an?\sunmarried|\W+who\s|\W+husband\sof|\W+texas\W+|\W+a\smarried|\W+\sa\scalifornia|\W+party\Wies.*first)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='grantee' and doc_type='Deed' and key_regex='(?i)(Grantor\,\sand\s|whose\spost\soffice.*f1\s\d+\sto\s|first\spart\W+and\s)' and value_regex='(?i)(?:Grantor\,\sand\s|whose\spost\soffice.*f1\s\d+\sto\s|first\spart\W+and\s)(.*?)(?=\swhose\spost\soffice|\sparty)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='instrument_number' and doc_type='Deed' and key_regex='(?i)(Public\srecords)' and value_regex='(?i)(?:records\s.*am\s)(\w[\d]+)' and config_set='Fluid';



DELETE FROM public.extractor_configs_old
WHERE "name"='instrument_number' and doc_type='Deed' and key_regex='(?i)(notice\sof\sConfidentiality|correction\saffidavit)' and value_regex='(?i)\d{17}|\d{12}|\d{10}|\d{11}' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='instrument_number' and doc_type='Deed' and key_regex='(?i)(doc\W?\s?|do\snot\sdiscard\s\w?\s|\d{0,2}\/)' and value_regex='(?i)(?:doc\W?\s?|do\snot\sdiscard\s\w?\s)([\d\-?]+)(?=\s\w)' and config_set='Fluid';


DELETE FROM public.extractor_configs_old
WHERE "name"='instrument_number' and doc_type='Deed' and key_regex='(?i)(file\sno\W+\s|file\s?\W?)' and value_regex='(?i)(?:file\sno\W+\s|file\s?\W?)([\d\w\-]+)(?=\sor|\s)' and config_set='Fluid';
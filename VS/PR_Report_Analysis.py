import pandas as pd
import numpy as np
import os
doc1=dict()             #to convert enumerate object into list
i=0
tb=pd.read_csv("/home/billion/Desktop/Detailed-PR-report-15062022.csv")

def analysis():
    

    #to get unique names from doc_type
    doc_type=tb['doc_name'].unique().tolist()
    #del doc_type[-1]                #to delete the "nan" from list
    en_doc=enumerate(doc_type)      #to convert list into enumerate
    global doc1
    doc1=dict(en_doc)               #to convert enumerate object into list

    print(f"Choose the document type: {doc1} ")
    global i
    i=int(input())                  #for getting value of dictionary on the basis of key                    
    choice=int(input("Press 1 for individual field wise document OR : press 2 for a single file with sorted field_names : oR Press 3 for compare")) 
    if choice==1:
        multi()
    elif choice==2: 
        single()
    elif choice==3:
        compare()
    else:
        print("wrong choice")

#to print multiple files field wise        
def multi():
    field=tb['field_name'].unique().tolist()
    for value in field: 
        if not (tb[tb['doc_name']==doc1[i]].empty) & (tb[tb['field_name']==value].empty):
            insta=tb[(tb['field_name']==value) & (tb['doc_name']==doc1[i])]
            if len(insta)>0:
                Deed=insta[(insta['status']=="fp")|(insta['status']=="fn")]
                os.makedirs(f'Analysis/{doc1[i]}', exist_ok=True)  
                Deed.to_csv(f'Analysis/{doc1[i]}/{doc1[i]}_{value}.csv',index=False)
        else:
            print("choose appropriate Document type")

#to print single file sorted with field_names
def single():
    a=tb[tb['doc_name']==doc1[i]]
    uni=a['field_name'].unique().tolist()
    if not (tb[tb['doc_name']==doc1[i]].empty):
        Deed=a[(a['status']=="fp")|(a['status']=="fn")]
        Deed=Deed.sort_values(['field_name'])
        os.makedirs(f'Analysis/{doc1[i]}', exist_ok=True)  
        Deed.to_csv(f'Analysis/{doc1[i]}/{doc1[i]}.csv',index=False)
    else:
        print("choose appropriate Document type")
        
# to compare expected_value and regex_extractor_value
def compare():
    a=tb[tb['doc_name']==doc1[i]]
    uni=a['field_name'].unique().tolist()
    if not tb[tb['doc_name']==doc1[i]].empty:
        diff=a['expected_value'].compare(a['regex_extractor_value'])
        result=pd.concat([a,diff],axis=1)
        result.rename(columns = {'self':'Expected','other':'Regex'}, inplace = True) 
        result=result.sort_values(['field_name'])
        result['Difference']=np.where(result['regex_extractor_value']==result['expected_value'],'True','False')
        result=result[result['Difference']=="False"]
        print(type(result))
        os.makedirs(f'Analysis/{doc1[i]}', exist_ok=True)  
        result.to_csv(f'Analysis/{doc1[i]}/{doc1[i]}.csv',index=False)
    else:
        print("choose appropriate Document type")
           
    
    
if __name__ == '__main__':
    analysis()
def convert(lst):
    res_dct={lst[i]:lst[i+1] for i in range(0,len(lst),2)}
    return res_dct

convert(['a',1,'b',2,'c',3,'d',4])


        # d= {lst[i]:lst[i+1] for i in range(1,10,2)}
        # print(d)
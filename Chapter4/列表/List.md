# [列表](#list)
python的列表对象是一个序列，可以存储任意类型的对象，没有固定大小，可以通过偏移量赋值调用  
## [序列操作](#operate)
由于列表是序列的一种，列表支持所有对字符串序列的操作  
    L=[123,'spam',1.23]  
    len(L)  # Number of items in the list  
    L[0]    # Indexing by position  
    L[:-1]  # Slicing a list returns a new list  
    L+[4,5,6]   # Concatenation makes a new list too  
    
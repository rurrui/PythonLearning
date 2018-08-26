# [列表](#list)
## [1.序列操作](#operate)
## [2.类型特定的操作](#operatespecial)
## [3.边界检查](#boundary)
## [4.嵌套](#nest)
## [5.列表解析](#analysis)
<span id="list">0.&emsp;列表概念</span>  
&emsp;python的列表对象是一个序列，可以存储任意类型的对象，没有固定大小，可以通过偏移量赋值调用  
<span id="operate">2. 由于列表是序列的一种，列表支持所有对字符串序列的操作</span>  
``` python
    L=[123,'spam',1.23]  
    len(L)              # Number of items in the list  
    L[0]                # Indexing by position  
    L[:-1]              # Slicing a list returns a new list  
    L+[4,5,6]           # Concatenation makes a new list too  
```
<span id="operatespecial">2.&emsp;类型特定的操作</span>  
&emsp;Python的列表和其他语言的数组相似，但是列表更为强大。
列表没有固定类型，没有固定大小。所以可以根据需求增加或删除列表的元素，代码：
``` python
    >>> L=[123,'spam',1.23]
    >>> L.append('NI')      # 在列表的尾部追加一个元素
    >>> L
    [123,'spam',1.23,'NI']
    >>> L.pop(2)            # 把列表索引为二的元素移除
    1.23
    >>> L
    [123,'spam','NI']
    >>> L.insert(1,'wwe')   # 按照索引位置追加一个元素
    >>> L
    [123,'wwe','spam','NI']
    >>> L.remove('wwe')     # 移除列表中的指定值
    >>> L
    [123,'spam','NI']
    >>> L1=[2,1,3]
    >>> L1.sort()           # 按照升序重新排序列表L1
    >>> L1
    [1,2,3]
    >>> L1.reverse()        # 按照降序重新排序列表L2
    >>> L1
    [3,2,1]
```
<span id="boundary">3.&emsp;为列表取值或者赋值时不能超出索引范围</span>
``` python
    >>> L=[1,2,3]
    >>> L=[99]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range
```
<span id="nest">4.&emsp;列表的嵌套有两大特点：</span>  
1).可以以任意的组合对进行嵌套  
``` python
L=[[1,2,3],"wwe",{'name'='wzh','age'=23}]
```
2).可以多个层次进行嵌套
```python
L=[[1,2,{'name':[1,2,3]}]]
```
<span id="analysis">5.&emsp;列表解析</span>  
&emsp;列表解析是一种强大的功能，可以有效的帮助我们处理列表对象。例如，如果我们要取一个矩阵(Matrix)的第二列，可以以列表解析方式取得：
```python
>>> M=[[1,2,3],[4,5,6],[7,8,9]]
>>> col2=[row[2] for row in M]
>>> col2
[2,5,8]
```
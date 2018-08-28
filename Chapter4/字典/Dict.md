# [字典](#dict)
1.字典的概念  
&emsp;字典是一种映射关系的类型，字典具有可变性，可以像列表那样增加或者减少.  
2.映射操作  
&emsp;
``` python
    >>> D={'food':'Spam','quantity':4,'color':'pink'} #创建一个字典对象
    >>> D['food']       # 匹配键为food的字典值
    'Spam'
    >>> D['quantity']+=1
    >>> D
    {'food':'Spam','quantity':5,'color':'pink'}
```
创建字典的其他方法：
```python
    >>> D={}
    >>> D['name']='Bob'
    >>> D['job']='dev'
    >>> D['age']=40
    >>> D
    {'name':'Bob','job':'dev','age':40}
```
3.字典的嵌套  
&emsp;有时候会需要更加复杂的数据信息，所以字典可以支持嵌套。例如之前创建的字典D中的name键所对应的值，我们现在需要更为详细的信息，LastName和FirstName:  
```python
    >>> D={'name':{'FirstName':'Tom','LastName':'W'},'job':['dev','princinple'],'age':23}
```
`一个有趣的问题`
```python
    >>> D={'name':'wzh','age':23}
    >>> D=0
```
&emsp;以上两行代码执行过程中有一个有趣的操作，就是计算机把{'name':'wzh','age':23}这个对象所占用的内存给释放了，因为在执行D=0的时候，已经重新为D变量赋值，之前的字典对象已经失去了引用，所以python会自动帮我们销毁字典对象的资源！  

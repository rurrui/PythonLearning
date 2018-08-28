# 键的排序：for循环
D={'b':2,'a':1,'c':3}
Ks=list(D.keys())
Ks.sort()
for key in Ks:
    print(key,"=>",D[key])
# 另外一种排序方法
D1={'c':3,'b':2,'a':1}
for key in sorted(D1):
    print(key,"=>",D1[key])
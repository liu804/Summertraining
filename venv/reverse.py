def string_reverse(m):
    num=len(m)
    a=[]
    for i in range(num):
        a.append(m[num-1-i])#从最后一位的元素开始往新list内添加元素
    return a
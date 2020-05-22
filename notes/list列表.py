1. list.append(元素):               # 向列表末尾添加一个元素
    >>> list1 = [1, 2, 3,]
        list1.append(34)
        print(list1)
    >>> [1, 2, 3, 34]

2. list.extend(列表):               # 在末尾把一个列表的元素添加到另一个列表中，作为另一个列表的元素
    >>> list1.extend([1,2,3])
        print(list1)
    >>> [1, 2, 3, 1, 2, 3]

3. list[下标] = 值:                 # 替换
    eg. >>> list1[3] = 3000
        >>> list1 = [1, 2, 3000]
    
4. list3 =  list1 + list2 :         # 列表的组合    
    >>> list2 = [5, 6, 7]
        print (list3)
    >>> [1, 2, 3, 5, 6, 7]

5. list4 = list1 * 2:               # 列表的重复
    >>> list4 = liat1 * 2
        print (list4)
    >>> [1, 2, 3, 1, 2, 3]

6. 元素 in list:                    # 判断元素是否在列表里
    >>> print (3 in list1)
    >>> True

7. list[start:stop]:                # 截取列表中的元素 同 str = 'asdf' str[1:]
    >>> list5 = [1, 2, 3, 4, 5, 6, 7]                   # >>> 'sdf'
        print (list5[2:4])
    >>> [3, 4, 5]

8. 多维列表:
    >>> list6 = [[1, 2, 3, 4], ['sh', 28, 'sn'], [True, False]]
        print (list6[3][1])
    >>> False

9. list.insert(下标, 元素):         # 在指定下标处添加特定元素(不覆盖原数据)
    >>> list5.insert(1, 300)
        print (list5)
    >>> [1, 300, 2, 3, 4, 5, 6, 7]

10. list.pop(下标):                  # 删除指定下标的元素 并返回删除的数据
    >>> list5.pop()                  # 默认为-1 即最后一个元素的下标
        list1.pop(1)
        print(list5)
        print(list1)
        print(list1.pop(1))
    >>> [1, 2, 3, 4, 5, 6]
        [1, 3]
        2   # 得到返回的数据

11. list.remove(元素):                # 删除指定的元素,重复的元素只删除第一个
    >>> list7 = [1, 2, 3, 4, 5, 5, 6] # 两个五
        list7.remove(5)
    >>> [1, 2, 3, 4, 5, 6]  # 一个五

    list.clear(元素):                 # 清除所有数据
    >>> list7.clear()
        pritn(list7)
    >>> []
    
12. list.index(元素, start, stop):                 # 从列表中找出某元素第一个下标
    >>> print(list7.index(5))
        print(list7.index(5, 0, 3))
    >>> 4   # 第一个5的下标
        ValueError: 5 not in list   # 报错，说明5不在0到3内

13. len(list):                        # 看列表中有几个元素
    max(list):                        # 获取列表中最大的元素
    min(list):
    list.count(元素):                 # 计算某元素在列表中出现的次数
    >>> print (len(list7), 
            max(list7), 
            min(list7), 
            list7.count(5))
    >>> 7
        6
        1
        2                               # 删除列表中所有重复元素的方法：
                                        count = list7.count(5)
                                        now_count = 1
                                        while now_count <= count :
                                            list7.remove(5)
                                            now_count += 1
                                        print (list7)

                                        >>>[1, 2, 3, 4, 6]


14. list.sort():                        # 列表倒叙
    list.reverse():                     # 列表顺叙
    >>> list8 = [5, 3, 4, 1, 2]        
        print(list8.reverse())
        print(list8.sort())
    >>> [5, 4, 3, 2, 1]
        [1, 2, 3, 4, 5]


15. list = list:                        # 浅拷贝  引用拷贝(复制了指向值的地址)
    >>> list9 = [1, 2, 3]               # (并给了 list10, 两个变量指向一个数据)
        list10 = list9
        list10[1] = 300
        print(llist9, list10)
    >>> [1, 300, 3]                     # 可以发现list9的值也跟着改变了，
        [1, 300, 3]                     # 其实 id(list9) 与 id(list10) 是相等的


16. list = list.copy():                 # 深拷贝 内存拷贝(重新创建了一个list(内存值))
    >>> list10 = list9.copy()
        list10[1] = 300
        print (list9, list10)
    >>> [1, 2, 3]
        [1, 300, 3]
17. list = (元组):                       # 元组转列表   元组:eg. (1, 2, 3, 4)
    >>> list11 = list((1, 2, 3))
        print (list11)
    >>> [1, 2, 3]

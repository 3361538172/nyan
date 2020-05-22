	1. eval('数式')
		eg. eval('3+2')
		>>> 5                     # 自动将字符串转成数式并求和
	
	2. len(str)                       # 求字符串长度(空格也算)

	3. str.lower()                    # 将大写字母转成小写
		eg. str1 = 'Good'
		    print(str1.lower())
		>>> good

	4. str.upper()                    # 大写字母转小写
		eg. print(str1.upper())
		>>> GOOD

	5. str.swapcase()                 # 字母大小写互换
		eg. print(str1.swapcase())
		>>> gOOD
	
	6. str.capitalize()               # 自动规范格式(句首大写，其余小写)
		eg. str2 = 'heLLOW WORld'
		    print(str2.capitalize())
		>>> Hellow world

        7. str.title()                    # 每个词首字母大写
                eg. print(str2.tilte())
                >>> Hellow World

        8. str.center(width, fillchar)    # char:字符(character) 在字符串两边填充指定字符, 可用于打印分割线 【默认为空格】
                eg. print(str2.center(17, '*'))
                >>> ***heLLOW WORld*** # 此宽度为17

                eg. print (str.center(10))
                >>>    Good    # 此宽度为10(6个空格)
        
        9. str.ljust(width[, fillchar])   # 向两边靠齐[默认为空格]，str向左，其他向右
                eg1. print(str1.ljust(10, '*'))
                >>> Good****** # 此宽度为10

                eg2. print(str1.ljust(10, '$', '*'))
                >>> Good$$$$$*

        9. str.rjust(width[, fillchar])   # 向两边靠齐[默认为空格]，str向右，其余向左
                eg1. print(str1.rjust(10, '*'))
                >>>  ******Good # 此宽度为10

                eg2. print(str1.rjust(10, '$', '*'))
                >>> *$$$$$Goood

        10. str.zfill(width)              # 用0来填充,字符右对齐
                eg. print (str1.zfill(10))
                >>> 000000Good

        11. str.count(''[,start][,end])   # 计算引号内字符串出现的次数
            eg. print (str1.count('o'))
            >>> 2
                print (str1.count('oo'))
            >>> 1
                print (str1.count('o', 2, len(str1)))
            >>> 1     # 从2号字符开始(0，1，2，3，4)，到最后一位

        12. str.find(str[,start][,end])   # 找出你要找的字符在哪一位
            eg. print (str1.find('oo'))
            >>> 1     # 表示第一个o在第1号字符的位置(只显示第一个的o位置)
                pritn (str1.find('asd'))
            >>> -1    # -1表示无此字符串
        ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
        *          以上默认从左往右                       *
        *          若要从右往左，使用 rfind               *
        ***************************************************

        13. str.index(str[,start][,end])  # 与find一样，但检索的()str不存在时会报错
            str.rindex(str.....)

        14. str.lstrip()                  # 截去左边的指定字符，默认为空格
        eg. str3 = '    good'
            str4 = '111good'
            print (str3.lstrip())
            print (str4.lstrip('1'))
            >>> good
            >>> good
        同理：str.rstrip()

        15. str.strip('1')                # 左右都截
        eg. str5 = '1111111good11111111'
            print (atr5.strip('1'))
            >>> good

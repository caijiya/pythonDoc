age = input("请输入你的年龄:")#input获取的所有数据,都当做 字符串类型  20--->age-->"20"
age_num = int(age)#----->整形,,,,去除了双引号之后的值  20

#if 如果年龄大于18:
if age_num>18:
    print("已成年,可以去网吧嗨皮.....")
else:
    print("未成年,回家写作业吧......")


stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
stus.sort(key=lambda x: x["name"])
for x in stus:
    print(x)


# f1 = open('test.txt', 'w+')
# f2 = open("1.txt","w")
# buffer = [1024]
# f1.read(buffer)


def func(x, y, function):
    return function(x, y)


print(func(1, 2, lambda x, y: x + y))

f1 = open("test.txt", "r")
f2 = open("222.txt", "w+")
content = f1.readlines()
f2.writelines(content)
# done = True
# while done:
#     content = f1.readline()
#     f2.write(content)
#     if content.__eq__(""):
#         done = False

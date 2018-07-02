# #  编写程序，完成以下要求：
# #
# # 统计字符串中，各个字符的个数
# # 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
#
# map = {}
# str = "hello world"
# for s in str:
#     if s in map.keys():
#         value = map.get(s)
#         map[s] = value + 1
#     else:
#         map[s] = 1
# print(map)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    for n in primes():
        if n < 100:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()

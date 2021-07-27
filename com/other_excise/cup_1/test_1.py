# from cup import exfile

# file_lock = exfile.LockFile()
# 
# file_lock.lock(blocking=True)
# 
# file_lock.unlock()


print(f" CHAR -> ASCII : {ord('A')}")
print(f' ASCII -> CHAR : { chr(65) }')


# 字节和 字符数的统计
str1 = "我用Python"
# str1 = "Python"

# 字节数_ UTF-8编码(一个中文占3个字节), GBK是 一个中文2个字节

# 8 12  10
print(f'{str1}的字符数 : {len(str1)}， '
      f'UTF-8编码下的字节数:{len(str1.encode())}, '
      f'GBK下的字节数{len(str1.encode(encoding="GBK"))}')







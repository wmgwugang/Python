# 以写模式打开文件，如果文件不存在，则创建一个新文件；如果文件存在，则打开文件，并重新编辑(即会覆盖原有文件内容)
f = open('test.txt', 'w')

f.writelines('hello world, Python')

# 在原有内容的末尾追加输入内容
f.writelines('.........')
f.close()

# 以只读模式打开文件，文件的指针会放在文件的开头。如果文件不存在，则会抛出异常
r = open('test.txt', 'r')
content = r.readline();
r.close()
print(content)
# coding:utf-8
ip_path = r'/home/super-zou/Desktop/读取IP后测试端口'
with open(ip_path + '/ip文件') as f:
    ip_host = f.readlines()
host_list = []
for host in ip_host:
    host_list.append(host.strip())


def add_mark(leftmark,rightmark):
    new_host = []
    for host1 in ip_host:
        new_host.append(leftmark+host1.strip()+rightmark)
    writ_txt(new_host)


def add_port():
    ip_port = raw_input('请输入你要添加的端口号：\n')
    new_host_port = []
    for host2 in host_list:
        new_host_port.append(host2 + ":" + ip_port)
    writ_txt(new_host_port)


def writ_txt(list_line):
    sep = '\n'
    txt_name = raw_input('请输入文件名：\n')
    with open(txt_name + '.txt', 'w') as fl:
        fl.write(sep.join(list_line))


elect = raw_input('请输入你要添加的选项：1、添加单引号；2、添加端口号;3、添加端口号和引号.\n')
if elect == str(1):
    add_mark(leftmark="'", rightmark="'")
elif elect == str(2):
    add_port()
else:
    add_mark("'", ":80'")



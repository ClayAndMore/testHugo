# coding:utf-8
import sys
import os

"""

- [Grammer]({{< relref "/02__Python/Grammer" >}})
  - [3rd]({{< relref "/02__Python/Grammer/01-python" >}})
    - [4th]({{< relref "/02__Python/Grammer/02-变量类型" >}})

"""
dir_templet = "%s- **%s**"
templet = '%s- [%s]({{< relref "/%s" >}})'

def main(memu):
    for dirpath, dirnames, filenames in os.walk(memu):
        print dirpath, dirnames, filenames
        print "当前目录下的文件:"
        for f in filenames:
        	print "  ", f.decode("utf-8")


# root_menu 的形式为 02__python
def getMemu(root_menu, deep=0):
    print (dir_templet % ('  ' * deep, root_menu.split('/')[-1])).decode("utf-8")
    #print (dir_templet % ('  ' * deep, root_menu.split('/')[-1])).decode("utf-8") todo:折叠
    lists = sorted(os.listdir(root_menu))
    for path in lists:
        pathtemp = root_menu + '/' + path
        if os.path.isdir(pathtemp):
            getMemu(pathtemp, deep=deep+1)
    else:
        if "_index.md" not in lists:
            # print "1111", root_menu, os.path.abspath(root_menu)
    	    open(os.path.join(os.path.abspath(root_menu),"_index.md"), "w").close()

        for path in lists:
            if path[0] in ["_","."]:
                continue
            pathtemp = root_menu + '/' + path
            if not os.path.isdir(pathtemp):
                print (templet % ('  ' * (deep+1), path, pathtemp)).decode("utf-8")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        memu = sys.argv[1]
        print "待操作的目录为：", memu
        getMemu(memu)
#!/usr/bin/python
# coding=utf-8
import sys
import subprocess


def getUserResult(key):
     answer=input(key)
     return answer


def check_code_git_status():
    result = subprocess.getstatusoutput('git status')
    if result[0] >> 8 != 0:
        print("Get git statuts fail")
        sys.exit(1);
    else:
        committype = getUserResult('编译正式软件发现本地代码有差异： 是否过滤掉，过滤（yes），停止（no）:')
        if not (committype == 'yes' or committype == 'no'):
            print("\033[7;31m输入错误，请重新选择\033[0m")
            sys.exit(0)
        elif not (committype == 'yes'):
            print("\033[7;31m本地代码与服务器有差异，您已停止编译\033[0m")
            sys.exit(0)
        else:
            print("\033[7;31m本地代码与服务器有差异，但您选择忽略，故继续编译\033[0m")
            sys.exit(1)
			
def main(make_module):
    if not (make_module[0:1]=='r'):
        sys.exit(1)
    else:
        print("zhangxuemei")
        check_code_git_status()


if __name__ == '__main__':
    main(sys.argv[1])


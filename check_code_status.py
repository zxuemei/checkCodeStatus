import subprocess
import sys

def check_code_git_status():
    result = subprocess.getstatusoutput('git status')
    if result[0]>>8 != 0:
        print('git statu Failed! pls check your git')
        sys.exit(0)
    elif 'Changes not staged for commit:' in result[1]:
        answer = input('编译正式软件发现本地代码有差异，是否要过滤掉？过滤(yes),停止(no)：')
        if not (answer == 'yes' or answer == 'no'):
            print('\033[7;31m 选择错误，中断/033[0m')
            sys.exit(0)
        elif answer == 'yes':
            print('\033[7;31m 选择过滤，继续编译\033[0m')
            sys.exit(1)
        else:
            print('\033[7;31m 选择停止，停止编译\033[0m')
            sys.exit(0)

def main():
    check_code_git_status()

if __name__ == '__main__':
    main()


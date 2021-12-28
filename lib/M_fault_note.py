# coding=utf-8
import os
import re
import pickle


base_path = './data/fault_note/'
def solve_no_note(file_name):
    if (not os.path.isfile(f'{base_path}{file_name}')):
        file = open(f'{base_path}{file_name}', 'wb')
        file.close()


def add_fault_note(file_name,title, type, options, key):

    solve_no_note(file_name)
    file_in = open(f'{base_path}{file_name}', mode='rb')
    content = file_in.read()
    fault_dic = {}
    if (len(content)):
        fault_dic = pickle.loads(content)

    if (title not in fault_dic):
        temp = {'type': type, 'options': options, 'key': key}
        fault_dic[title] = temp

        file_in.close()

        file_out = open(f'{base_path}{file_name}', mode='wb')
        pickle.dump(fault_dic, file_out)
        file_out.close()


def rmove_fault_note(file_name,title):
    solve_no_note(file_name)
    file_in = open(f'{base_path}{file_name}', mode='rb')
    content = file_in.read()
    fault_dic = {}
    if (len(content)):
        fault_dic = pickle.loads(content)

    if (title in fault_dic):
        del fault_dic[title]
        file_in.close()

        file_out = open(f'{base_path}{file_name}', mode='wb')
        pickle.dump(fault_dic, file_out)
        file_out.close()


def review_fault(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    solve_no_note(file_name)
    file_in = open(f'{base_path}{file_name}', mode='rb')
    content = file_in.read()
    fault_dic = {}
    if (len(content)):
        fault_dic = pickle.loads(content)

    times = 0
    for title, opt_key in fault_dic.items():
        times += 1
        type = opt_key['type']
        options = opt_key['options']
        key = opt_key['key']

        os.system('cls' if os.name == 'nt' else 'clear')
        print('错题回顾')
        print('({}/{})'.format(times, len(fault_dic)))
        print(title)
        print(opt_key['options'], '\n')

        answer = input('请输入你的答案(输入u返回上一级,q退出)：')
        answer = answer.replace(' ', '')
        answer = answer.upper()

        if type == '判断题':
            if answer == 'A':
                answer = '对'

            elif answer == 'B':
                answer = '错'


        if (answer == 'q' or answer == 'Q'):
            exit()

        elif (answer == 'u' or answer == 'U'):
            return

        elif (answer == key):
            print('正确！')
            rmove_fault_note(file_name,title)

        else:
            print('错误！  正确答案：', key)
            add_fault_note(file_name,title, type, options, key)

        input("输入任意键继续：")
        os.system('cls' if os.name == 'nt' else 'clear')

    choice = input('错题做完了！\n[q]退出\n[u]返回主菜单\n请输入你的选择[*|q]:')

    if (choice == 'u' or choice == 'U'):
        return

    elif (choice == 'q' or choice == 'Q'):
        exit()


def get_fault_note_numbers(file_name):
    solve_no_note(file_name)
    file_in = open(f'{base_path}{file_name}', mode='rb')
    content = file_in.read()
    fault_dic = {}
    if (len(content)):
        fault_dic = pickle.loads(content)
        num = len(fault_dic)
        return num

    else:
        return 0


def reset_fault_note(file_name):
    os.remove(f'{base_path}{file_name}')
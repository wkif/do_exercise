import os
import json
from pydoc import doc
from re import T
import signal
import time
from tokenize import Number

class globalData:
    processPath=''
    problems = []
def check_answer(a1: str, a2: str):
    if a1 == a2:
        return True
    if a1.upper() == a2.upper():
        return True
    b1 = a1.upper().replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D")\
        .replace("对", "A").replace("错", "B").replace("T", "A").replace("F", "B")
    b2 = a2.upper().replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D")\
        .replace("对", "A").replace("错", "B").replace("T", "A").replace("F", "B")
    if b1 == b2:
        return True
    return False





def save_exit(signum, frame):
    with open(globalData.processPath, "w") as f:
        f.write(json.dumps(globalData.problems, ensure_ascii=False))
    exit(0)


def rushb():

# 跳过个数
    bypass_count = 0

    error_threshold = 1
# 是否清屏
    do_clear = False
    jsonLIst=['马克思主义基本原理题库.json','毛泽东思想和中国特色社会主义理论体系概论题库.json']
    index= input("选择题库（马原输入0,毛概输入1）\n")
    do_what = os.path.join('./assets',jsonLIst[int(index)]).replace('\\','/')
    processName = "process"+jsonLIst[int(index)].split('.')[0]+'.json'
    globalData.processPath = os.path.join('./process',processName).replace('\\','/')
    doerror = input("只做错题？（0/1）\n")
    if int(doerror)==1:
        only_do_error=True
    else:
         only_do_error = False
    signal.signal(signal.SIGINT, save_exit)
    signal.signal(signal.SIGTERM, save_exit)
    if os.path.exists(globalData.processPath):
        with open(globalData.processPath, "r") as f:
            globalData.problems = json.loads(f.read())
    else:
        with open(do_what, "r", encoding='UTF-8') as f:
            globalData.problems = json.loads(f.read())

    for pid, problem in enumerate(globalData.problems):
        if pid < bypass_count:
            continue
        if only_do_error:
            try:
                if problem['error_times'] < error_threshold:
                    continue
            except KeyError:
                continue
        try:
            if check_answer(problem['answer'], problem['my_answer']):
                continue
        except KeyError:
            pass
        print("[%s]第%d题：\n" % (problem['type'].replace("题", ""), pid))
        print(problem['problem'])
        if problem['type'] != "判断题":
            print(problem['A'])
            print(problem['B'])
            print(problem['C'])
            print(problem['D'])
        my_answer = input()
        if my_answer.upper() == "SAVE":
            with open(globalData.processPath, "w") as f:
                f.write(json.dumps(globalData.problems, ensure_ascii=False))
            my_answer = input()
        if my_answer.upper() == "QUIT":
            with open(globalData.processPath, "w") as f:
                f.write(json.dumps(globalData.problems, ensure_ascii=False))
            exit(0)
        globalData.problems[pid]['my_answer'] = my_answer
        if check_answer(problem['answer'], my_answer):
            print("\033[32m答对了！\033[0m\n\n\n")
            if do_clear:
                time.sleep(1)
                os.system("clear")
        else:
            print("\033[31m答错了！\033[0m")
            print("正确答案：\033[32m" + problem['answer'] + "\033[0m")
            print("我的答案：\033[31m" + my_answer + "\033[0m")
            try:
                globalData.problems[pid]['error_times'] += 1
            except KeyError:
                globalData.problems[pid]['error_times'] = 1
            input()
            print("\n\n\n")
            if do_clear:
                os.system("clear")


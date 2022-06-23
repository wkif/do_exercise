import json
import os

def extract_wrong():
    jsonLIst=['马克思主义基本原理题库.json','毛泽东思想和中国特色社会主义理论体系概论题库.json']
    index= input("选择题库（马原输入0,毛概输入1）\n")
    processName = "process"+jsonLIst[int(index)].split('.')[0]+'.json'
    processPath = os.path.join('./process',processName).replace('\\','/')
    if not os.path.exists(processPath):
        print('没有记录呢\n')
        return
    problems = []
    wrong_problems = []
    wrong_txt = ""
    with open(processPath, "r") as f:
        problems = json.loads(f.read())
    for problem in problems:
        try:
            if problem['error_times'] > 1:
                wrong_problem = {}
                wrong_problem['problem'] = problem['problem']
                wrong_problem['type'] = problem['type']
                if problem['type'] != "判断题":
                    wrong_problem['A'] = problem['A']
                    wrong_problem['B'] = problem['B']
                    wrong_problem['C'] = problem['C']
                    wrong_problem['D'] = problem['D']
                wrong_problem['answer'] = problem['answer']
                wrong_problem['error_times'] = problem['error_times']
                wrong_problems.append(wrong_problem)
                wrong_txt += "[" + problem['type'].replace("题", "") + "]"
                wrong_txt += problem['problem'] + "\n"
                if problem['type'] != "判断题":
                    wrong_txt += problem['A'] + "\n"
                    wrong_txt += problem['B'] + "\n"
                    wrong_txt += problem['C'] + "\n"
                    wrong_txt += problem['D'] + "\n"
                wrong_txt += "正确答案: " + problem['answer'] + "\n"
                wrong_txt += "错误次数: " + str(problem['error_times']) + "\n\n"
        except KeyError:
            continue
    Jsonpath = jsonLIst[int(index)].split('.')[0]+"-错题.json"
    with open(Jsonpath, "w") as f:
        f.write(json.dumps(wrong_problems, ensure_ascii=False))
    Txtpath = jsonLIst[int(index)].split('.')[0]+"-错题.txt"
    with open(Txtpath, "w") as f:
        f.write(wrong_txt)

    print('已经导出txt和json文件啦\n')
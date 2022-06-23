import json
import os

def gen_markdown():
    jsonLIst=['马克思主义基本原理题库.json','毛泽东思想和中国特色社会主义理论体系概论题库.json']
    index= input("选择题库（马原输入0,毛概输入1）\n")
    processName = "process"+jsonLIst[int(index)].split('.')[0]+'.json'
    processPath = os.path.join('./process',processName).replace('\\','/')
    if not os.path.exists(processPath):
        print('没有记录呢\n')
        return
    doerror = input("只导出错题？（0/1）\n")
    if int(doerror)==1:
        only_export_error=True
    else:
        
        only_export_error = False
    problems = []
    markdown_text = ""
    with open(processPath, "r") as f:
        problems = json.loads(f.read())
    for pid, problem in enumerate(problems):
        try:
            if only_export_error and problem['error_times'] < 1:
                continue
            markdown_text += "【" + problem['type'].replace("题", "") + "】"
            markdown_text += str(pid) + "、"
            markdown_text += problem['problem'] + "\n"
            if problem['type'] != "判断题":
                if "A" in problem['answer']:
                    markdown_text += "- [X] " + problem['A'] + "\n"
                else:
                    markdown_text += "- [ ] " + problem['A'] + "\n"
                if "B" in problem['answer']:
                    markdown_text += "- [X] " + problem['B'] + "\n"
                else:
                    markdown_text += "- [ ] " + problem['B'] + "\n"
                if "C" in problem['answer']:
                    markdown_text += "- [X] " + problem['C'] + "\n"
                else:
                    markdown_text += "- [ ] " + problem['C'] + "\n"
                if "D" in problem['answer']:
                    markdown_text += "- [X] " + problem['D'] + "\n"
                else:
                    markdown_text += "- [ ] " + problem['D'] + "\n"
            else:
                markdown_text += "正确答案: " + problem['answer'] + "\n"
            markdown_text += "错误次数: " + str(problem['error_times']) + "\n\n"
        except KeyError:
            if not only_export_error:
                markdown_text += "\n"
            continue
    if only_export_error:
        Markdownpath = jsonLIst[int(index)].split('.')[0]+"-错题.md"
    else:
        Markdownpath = jsonLIst[int(index)].split('.')[0]+".md"
    with open(Markdownpath, "w") as f:
        f.write(markdown_text)
    print('已经导出tmarkdown文件啦\n')
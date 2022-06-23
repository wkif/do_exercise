
from question.rush_b import rushb 
from question.extract_wrong import extract_wrong
from question.gen_markdown import gen_markdown

if __name__ == "__main__":
    print("-----------------------------------\n")
    print("-----------功能--------------------\n")
    print("-----------练习题目     ：0--------\n")
    print("-----------导出错题     ：1--------\n")
    print("-----------导出markdown ：2--------\n")
    print("-----------------------------------\n")
    selectOne = input("请输入:\n")
    if int(selectOne)==0:
        rushb()
    elif int(selectOne)==1:
        extract_wrong()
    elif int(selectOne)==2:
        gen_markdown()
    else:
        pass


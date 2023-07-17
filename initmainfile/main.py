#自分で変数の名前をつけその変数に持たせるステータスがTrueかFalseかを定義するライブラリ

import json

true = True
false = False

def true_variable(variable):
    variable = True
    #jsonファイルに代入
    with open("json/true_false_list.json", "r", encoding="utf-8") as file:
        true_false_list = json.load(file)
    true_false_list[variable] = true
    with open("json/true_false_list.json", "w", encoding="utf-8") as file:
        json.dump(true_false_list, file)

def false_variable(variable):
    variable = False
    #jsonファイルに代入
    with open("json/true_false_list.json", "r", encoding="utf-8") as file:
        true_false_list = json.load(file)
    true_false_list[variable] = false
    with open("json/true_false_list.json", "w", encoding="utf-8") as file:
        json.dump(true_false_list, file)

def see_variable(variable):
    with open("json/true_false_list.json", "r", encoding="utf-8") as file:
        true_false_list = json.load(file)
    print(true_false_list[variable])

#test
def true_false_defined():
    while True:
        enter = input(">")
        if enter == "true-variable":
            print("変数名をつけてください")
            variable = input(">")
            true_variable(variable)
        elif enter == "false-variable":
            print("変数名をつけてください")
            variable = input(">")
            false_variable(variable)
        elif enter == "see-variable":
            print("どの変数のステータスを見ますか？")
            variable = input(">")
            see_variable(variable)
        else:
            print("そのようなコマンドはありません")

#test2
while True:
    enter = input(">")
    if enter == "true-variable":
        true_variable()
    elif enter == "test_mode":
        with open("json/true_false_list.json", "r", encoding="utf-8") as file:
            true_false_list = json.load(file)
        test_variable = true_false_list[""]
        print(test_variable)
    else:
        print("そのようなコマンドはありません")


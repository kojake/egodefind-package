#自分で変数の名前をつけその変数に持たせるステータスがTrueかFalseかを定義するライブラリ

import json

true = True
false = False

def true_variable(variable):
    #jsonファイルに代入
    with open("json/true_false_list.json", "r", encoding="utf-8") as file:
        true_false_list = json.load(file)
    true_false_list[variable] = true
    with open("json/true_false_list.json", "w", encoding="utf-8") as file:
        json.dump(true_false_list, file)

def false_variable(variable):
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
            break
        elif enter == "false-variable":
            print("変数名をつけてください")
            variable = input(">")
            false_variable(variable)
            break
        elif enter == "see-variable":
            print("どの変数のステータスを見ますか？")
            variable = input(">")
            see_variable(variable)
            break
        else:
            print("そのようなコマンドはありません")

#test2
while True:
    enter = input(">")
    if enter == "true-false-defined":
        true_false_defined()
    elif enter == "test_mode":
        print("変数名を入力してください")
        variable_enter = input(">")

        with open("json/true_false_list.json", "r", encoding="utf-8") as file:
            true_false_defined = json.load(file)

        if variable_enter in true_false_defined.keys():
            with open("json/true_false_list.json", "r", encoding="utf-8") as file:
                true_false_list = json.load(file)
            test_variable = true_false_list[variable_enter]
            print(test_variable)
        else:
            print("一致する変数がありませんでした。")
    else:
        print("そのようなコマンドはありません")


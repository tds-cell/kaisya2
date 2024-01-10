from os.path import exists
import openpyxl
import glob

"""
備忘録：実行環境に注意の事
実行ファイルの場所と下のPS C:\Users\tadashi\python>
違ってても実行できるよ
"""

#a.xdtファイルはC:\Users\tadashi\python>にある
#だからtest.pyが違うフォルダに有っても実行出来ている。
with open('a.xdt', 'rb') as f: #xdtファイルをバイト形式で読み込み
    a = f.read()    #変数aへ格納
    b = a.hex()     #さらに2進数から16進数へ変換
    #print(len(b))   #総文字数を確認 
    #print(type(b))  #classを確認　str型なので注意
    c = list(b)     #bはstrで文字の挿入が難しい? listへ変換
    #print(type(c))

    num = 0         #2バイト区切り変数
    d = 0           #改行変数

    for i in range(len(b)):
        k = 2 * (i + 1)
        
        if i == 0:          #初期値うまく処理できなかった
            c.insert(k, " ")
            num = num + 1
        else:               #改行コード
            c.insert(k + i + d, " ")
            num = num + 1    
        if num == 16:       #改行変数
            d = d + 1
            c.insert(k + i + d, '\n')
            num = 0
            
    d = ''.join(c)  #リスト型のままだとテキストファイルに書き込めない        

#16進数のデータaをテキストファイルのtest.txtへ書き込み

with open('test.txt', 'w') as t:
    t.write(d)


f.close
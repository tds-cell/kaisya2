from os.path import exists
#なぜ使えない状態なのか不明
import openpyxl
import glob

data = []
h_data = []

#a.xdtファイルはC:\Users\tadashi\python>にある
#だからtest.pyが違うフォルダに有っても実行出来ている。
with open('a_test.xdt', 'rb') as f: #xdtファイルをバイト形式で読み込み
    a = f.read()    #変数aへ格納
    b = a.hex()     #さらに2進数から16進数へ変換
    #print(len(b))   #総文字数を確認 
    #print(type(b))  #classを確認　str型なので注意
    c = list(b)     #bはstrで文字の挿入が難しい? listへ変換
    #print(type(c))

    #num = 0         #2バイト区切り変数
    num = 1           #改行変数
    
    for i in range(len(b)):
        k = 32 * num
        l = 32 * (num - 1)
        if i == k:
            data.append(c[l:i])
            num = num + 1


#print(type(data[0])) #<class 'list'>
"""
    for i in range(len(data)):
        if i == 0:
            u = data[0].decode(hex)
            h_data.append(u)
"""            
    #print(len(data))        
    #e = ''.join(data)  #リスト型のままだとテキストファイルに書き込めない        

#16進数のデータaをテキストファイルのtest.txtへ書き込み
with open('test_ver2.txt', 'w') as t:
    t.write(data)

f.close
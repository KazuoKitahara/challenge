#4
answer=[9, 1, 4,39]

while True:
    a=input("guess a numer or enter q to quit:")
    if a=="q":
        break
    try:
        a=int(a)
    except:
        print("数字を入力するか、qで終了します")
    if a in answer:
            print("正解")
            
    else:
            print("不正解")
            
        

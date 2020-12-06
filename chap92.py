#2
a=input("欲しい物は何ですか？")
with open("want.txt","w") as f:
    f.write(a)

#p48 challenge 1
print("1. やっと243頁のウェブスクレイピングまで来たぞ。")
print("1. 今度こそ３１３ページの最後まで読んで、Pythonマスターするぞ。")
print("1. 頑張れ！君ならできる")

#2
#x=1
x=39
if x<10:
    print("2. x is less than 10!")
else:
    print("2. x is greater than or equal to 10!")
#3
#x=10
#x=25
x=100
if x<=10:
    print("3. x is less than or equal to 10!")
elif x<=25:
    print("3. x is greater than 10 and is less than or equal to 25!")
else:
    print("3. x is greater than 25!")

#4
x=100
y=13
print("4.",x,"を",y,"で割った余りは",x%y)

#5
x=19
y=2
print("5.",x,"を",y,"で割ると商は",x//y)

#6
age=39
retirement=65
if age<18:
    print("6. まだこどもです。")
elif age<30:
    print("6. おとなです。３０歳未満です。")
elif age<40:
    print("6. ３０代です。がんばって仕事を見つけ、経済的に自立しましょう。")
elif age<60:
    print("6. 60才まで頑張って国民年金を収めましょう。")
elif age<65:
    print("6. 還暦すぎでも、まだ高齢者ではありません。")
else:
    print("6. 高齢者です。")

if retirement-age>0:
    print("6. ６５歳までの年数は",retirement-age)

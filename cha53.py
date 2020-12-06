#3
mydict={
    "height":"175cm",
    "favorite color":"blue",
    "favorite author":"Natsune Soseki"
    }
print(mydict)
#4
key=input('"height","favorite color",または"favorite author"と入力してください：')
if key in mydict:
    print(mydict[key])
else:
    print("入力されたキーは辞書にありません。")


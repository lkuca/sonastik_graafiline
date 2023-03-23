from module1 import *
from tkinter import *
global valik,aken,vene_letters
eesti_list =[] 
vene_list=[] 
vene_list=Loe_failist("vene.txt")
eesti_list=Loe_failist("eesti.txt")
aken=Tk()
aken.geometry("1920x1080")
spisokruskij=Label(aken,text="ввод ,комманда, язык программирования, синткс, семантика, машинный язык, язык ассемблера, машинная команда, переменная, целое число, число с плавающей запятой, str, boolean, коментарий, ошибка, действие, правдивый, ложный, разветвление, ветвь, отступ",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
spisokestonsky=Label(aken,text="sisend ja väljund ,käsk, programmeerimiskeel, süntaks ,semantika/tähendusõpetus, masinakeel, assemblerkeel, masinkäsk, muutuja, täisarv, ujukomaarv, sõne/tekst, tõeväärtus, kommentaar, viga, tehe, tõene, väär, hargnemine, haru, taane",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
valik=Entry(aken,fg="blue",text=f"1-translate\n2-lisa sona\n3-muuda sona\n4-mang\n ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
if valik==1:
    vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    sona=Label(aken,text="sissesta sona:",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
    sonavastus=Entry(aken,fg="blue",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
    if sona.lower()[0] in vene_letters:
       resultsõnast=Label(aken,text=f"{sona} on vene keeles",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
       try:
           ind = vene_list.index(sona)
           vaste = eesti_list[ind]
           eesti_sõna=Label(aken,text=f"{sona} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
       except ValueError:
           vale=Label(aken,text="sona ei ole leitud",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
    else:
        resultsõnast1=Label(aken,text=f"{sona} on inglise keeles",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
        try:
            ind =eesti_list.index(sona)
            vaste = vene_list[ind]
            vene_sõna=Label(aken,text=f"{sona} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
        except ValueError:
            vale=Label(aken,text="sona ei ole leitud",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)


spisokruskij.pack()
spisokestonsky.pack()
valik.pack()
valik.bind("<Return>",)
aken.mainloop()
         
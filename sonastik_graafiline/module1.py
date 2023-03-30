from pickle import LIST
from tkinter import *
import random
global vene_list, eesti_list
def Loe_failist(fail:str)->list:
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def tõlkida():
    vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    aken=Tk()
    aken.geometry("800x500")
    tran=Label(aken, text="Sisesta sõna mis tahad tõlkida:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
    translate=Entry(aken, text="Sisesta sõna mis tahad tõlkida:",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
    tran.pack()
    translate.pack()
    def tõlkida_check(event):
        trin=translate.get()
        if trin.lower()[0] in vene_letters:
            vast=Label(aken, text="{trin} on vene keeles:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
            vast.pack()
            try:
                ind = vene_list.index(trin)
                vaste = eesti_list[ind]
                trun=Label(aken, text=f"{trin} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                trun.pack()
            except ValueError:
                tron=Label(aken, text=f"sona ei ole leitud",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                tron.pack()
    aken.bind("<Return>",tõlkida_check)
    aken.mainloop()

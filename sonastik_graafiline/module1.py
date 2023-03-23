from pickle import LIST
from tkinter import *
import random
def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
aken1=Tk()
aken1.geometry("1920x1080")
valik=Entry(fg="blue",text=f"1-translate\n2-lisa sona\n3-muuda sona\n4-mang\n ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
sona=Label(text="sissesta sona:",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
sonavastus=Entry(fg="blue",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
resultsõnast=Label(aken,text=f"{sona} on vene keeles",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
eesti_sõna=Label(aken,text=f"{sona} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
vale=Label(aken,text="sona ei ole leitud",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
resultsõnast1=Label(aken,text=f"{sona} on inglise keeles",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)
vene_sõna=Label(aken,text=f"{sona} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=5,width=15)

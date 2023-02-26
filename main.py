import customtkinter as ctk
import tkinter
from element import window
from func import reset,showorhide,change,vals,verif
ctk.set_default_color_theme("dark-blue")
show=False
win=ctk.CTk()
win.geometry("600x300")
win.resizable(False,False)
win.title("password verif")
img = tkinter.PhotoImage(file = 's.png')
win.iconphoto(False, img)
sc = ctk.CTkProgressBar(win ,width=400, height=20)
sc.place(x=115,y=170)
c=False


v1=ctk.CTkButton(master=win, text="abc",width=40,font=("normal",40),fg_color="transparent",text_color="grey",height=40,border_color="green",border_width=0
,hover_color="white", state="DISABLED")
v1.place(x=450, y=200)
v2=ctk.CTkButton(master=win, text="ABC",width=40,font=("normal",40),fg_color="transparent",text_color="grey",height=40,border_color="green",border_width=0
,hover_color="white", state="DISABLED")
v2.place(x=330, y=200)
v3=ctk.CTkButton(master=win, text="* !@",width=40,font=("normal",40),fg_color="transparent",text_color="grey",height=40,border_color="green",border_width=0
,hover_color="white", state="DISABLED")
v3.place(x=220, y=200)
v4=ctk.CTkButton(master=win, text="123",width=40,font=("normal",40),fg_color="transparent",text_color="grey",height=40,border_color="green",border_width=0
,hover_color="white", state="DISABLED")
v4.place(x=100, y=200)



tt2=ctk.CTkLabel(master=win,text="by 17med_achour",text_color="white",font=("normal",20))
tt2.place(x=510,y=280,anchor="center")
tt=ctk.CTkLabel(master=win,text="",text_color="#404040",font=("normal",35))
tt.place(x=300,y=73,anchor="center") 
def callback(var):
    global sc
    verif(psw.get(),[v1,v2,v3,v4])
    vals(sc,tt,psw,[v1,v2,v3,v4])
    pass
    
   
def lp():
    global c,var
    c=True  
    psw.set("")


psw = ctk.StringVar()
psw.trace("w", lambda name, index,mode, psw=psw: callback(psw))

inp=ctk.CTkEntry(master=win,textvariable=psw,height=50,width=200,font=("normal",40),show="*")
inp.place(x=205, y=100)
bt0=ctk.CTkButton(master=win, text="reset",width=40,font=("normal",40),fg_color="#C0C0C0",text_color="#202020",height=40,border_color="grey"
,hover_color="white",command=lp).place(x=95, y=100)
bt1=ctk.CTkButton(master=win, text="show",width=40,font=("normal",40),fg_color="#C0C0C0",text_color="#202020",height=40,border_color="grey"
,hover_color="white",)
bt1.place(x=410, y=100)
bt1.configure(command=lambda :bt1.configure(text=showorhide(inp)))
# create CTk scrollbar

change(sc,tt,0)

win.mainloop()
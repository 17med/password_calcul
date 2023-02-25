from element import window,label
import tkinter
import customtkinter as ctk
c=window(height=900,width=500,windowborder=1)
z=label(c,"hi",size=100,xfromcenter=0.5,yfromcenter=0.49,pos="center")
z2=label(c,"hello world",size=20,padx=50,pady=50,pos="left")


c.show()
import customtkinter as ctk
import passwordmeter
def verif(m,e):
    
    a=False
    A=False
    nb=False
    sp=False
    for i in m:
        if(ord(i) in range(ord("a"),ord("z")+1)):
            a=True
        elif (ord(i) in range(ord("A"),ord("Z")+1)):
            A=True
        elif (ord(i) in range(ord("0"),ord("9")+1)):
            nb=True
        else:
            sp=True
    if(a):
        e[0].configure(border_width=2,text_color="green")
    else:
        e[0].configure(border_width=0,text_color="grey")
    if(A):
        e[1].configure(border_width=2,text_color="green")
    else:
        e[1].configure(border_width=0,text_color="grey")
    if(sp):
        e[2].configure(border_width=2,text_color="green")
    else:
        e[2].configure(border_width=0,text_color="grey")
    if(nb):
        e[3].configure(border_width=2,text_color="green")
    else:
        e[3].configure(border_width=0,text_color="grey")
def reset(m):
    m.set("")

    #m.delete(0,last_index=len(m.get()))
def showorhide(m):
    print("h")
    l=m.cget("show")
    if(l=="*"):
        m.configure(show="")
        return "hide"
    else:
        m.configure(show="*")
        return "show"
def vals(sc,x2,m,l):
    if(m.get()!=""):
        verif(m.get(),l)
        c=time(m.get())
        strength, improvements = passwordmeter.test(m.get())

        change(sc,x2,strength+0.1)
        #x.configure(text=c[1])
    else:
        
        x2.configure(text="")
        
        change(sc,x2,0)
def change(sc,x2,nb):

    sc.set(nb)
    if(nb==0):
        x2.configure(text="")
        sc.configure(progress_color="#4c4c54")
    elif(nb<0.4):
        x2.configure(text="bad",text_color="red")
        sc.configure(progress_color="red")
    elif(nb>=0.4 and nb<=0.6):
        x2.configure(text="ehhh good",text_color="yellow")
        sc.configure(progress_color="yellow")
    else:
        x2.configure(text="strong",text_color="green")
        sc.configure(progress_color="green")

import math

def time(password):
    guesses_per_second = 1000000
    """
    Calculate the time it would take to guess a password using brute-force attack.

    Parameters:
    password (str): The password to be guessed.
    guesses_per_second (int): The number of guesses that can be made per second.

    Returns:
    A dictionary containing the estimated time in seconds for a brute-force attack using the given guesses per second.

    """
    # Calculate the number of possible guesses
    character_set_size = 95  # printable ASCII characters
    password_length = len(password)
    guesses = math.pow(character_set_size, password_length)

    # Calculate the time in seconds
    time_seconds = guesses / guesses_per_second

    # Format the time in a human-readable way
    time_string = ""
    if time_seconds < 60:
        time_string = "{:.2f} seconds".format(time_seconds)
    elif time_seconds < 3600:
        time_string = "{:.2f} minutes".format(time_seconds / 60)
    elif time_seconds < 86400:
        time_string = "{:.2f} hours".format(time_seconds / 3600)
    elif time_seconds<15552000:
        time_string = "{:.2f} days".format(time_seconds / 86400)
    elif time_seconds<15552000*1000:
        time_string = "{:.2f} years".format(time_seconds / 15552000)
    elif time_seconds<15552000*1000*9999:
         time_string = "{:.2f} thousand years".format(time_seconds / (15552000*1000))
    else:
        time_string = "infinit"
    # Return the time as a dictionary
    return  time_seconds,time_string

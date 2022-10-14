# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:27:43 2022

@author: Calypso
"""

## Importing
from tkinter import *
import sqlite3

## Functions
def add_user():
    new_username = username_input.get()
    new_password = password_input.get()
    
    data = con.execute("SELECT count(*) FROM infolar where username = '"+new_username+"' " )
    result = data.fetchone()
    if result[0] > 0:
        msg["text"] = "Error: Username Already Exists!"
        msg["bg"] = "red"
    else:
        msg["text"] = "Username Succesfuly Added!"
        msg["bg"] = "green"
        con.execute("INSERT INTO infolar(username, password) values(?,?)",(new_username,new_password))
        con.commit()
        
def clear():
    username_value.set("")
    password_value.set("")

## DataBase
con = sqlite3.connect("melumatlar.db")
con.execute("""CREATE TABLE IF NOT EXISTS infolar(username text NOT NULL,
                                    password text NOT NULL)""")
con.commit()                  

## Window Configurations
window = Tk()
window.title("Login Page")
window.geometry("500x220")
window.configure(bg = "gray65")

## Labels
username_label = Label(window, text = "Enter Username", font = "Calibri 15", bg = "lightgreen")
username_label.place(x = 30, y = 40)

password_label = Label(window, text = "Enter Password", font = "Calibri 15", bg = "lightgreen")
password_label.place(x = 30, y = 90)
## Message
msg = Message(window, text = "", width = 200)
msg.place(x = 30, y = 10)

## Inputs
username_value = DoubleVar()
username_input = Entry(window, font = "Calibri 15", textvariable = username_value)
username_input.place(x = 200, y = 40)
username_input.delete(0,"end")

password_value = DoubleVar()
password_input = Entry(window, font = "Calibri 15", textvariable = password_value)
password_input.place(x = 200, y = 90)
password_input.delete(0,"end")
## Buttons

add_button = Button(window, text =" Add User", font = "Calibri 15", bg = "cyan", command = add_user)
add_button.place(x = 30, y = 140)

quit_button = Button(window, text = "Quit", font = "Calibri 15", bg=  "black", fg = "white", command = window.destroy)
quit_button.place(x = 350, y = 140)

clear_button = Button(window, text = "Clear", font = "calibri 15", bg = "pink", command = clear)
clear_button.place(x = 200, y = 140)

window.mainloop()













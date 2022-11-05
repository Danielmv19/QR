import tkinter
from tkinter import *
import qrcode
from pyzbar import pyzbar
from PIL import Image
from tkinter.filedialog import *
import customtkinter
import re
import cv2
import numpy
import os

def tema():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry('650x300')
root.resizable(0, 0)
root.title('QR Tool')

def select_file():
    global file_names
    global directory
    file_names = askopenfilename(initialdir="C:\\Users",
                                  title="Select File",
                                  filetypes=[
                                      ("image", ".png")
                                  ])
    #directory = os.path.split(file_names)[0]
    #os.path.normpath(file_names)
    return file_names

def guardar():
    save_file = asksaveasfile(mode='w', defaultextension=".png", filetypes = (("png files","*.png"),("all files","*.*")))
#------------------------------------ GENERADOR QR ----------------------------------------
def generar():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.clear()
    data = "hola k hace"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="white")
    img.save('qr1.png')
#------------------------------------ LECTOR QR ----------------------------------------
def leer():
    img = cv2.imread(file_names)
    detector = cv2.QRCodeDetector()
    data, bbox, stigh_code = detector.detectAndDecode(img)
    print(data)
#---------------------------------------------------------------------------------------
def create_toplevel():

    window = customtkinter.CTkToplevel()
    window.configure(fg_color="gray")
    window.geometry("400x200")
    label = customtkinter.CTkLabel(master=window, text='hola')
    label.place(relx=0.5,rely=0.5)
#---------------------------------------------------------------------------------------
frame = customtkinter.CTkFrame(master=root,
                               width=200,
                               height=300,
                               corner_radius=10,
                               fg_color=("white", "gray10"))
frame.pack(padx=0, pady=0, side=RIGHT)

text_var1 = tkinter.StringVar(value="QR TOOL")
text_var2 = tkinter.StringVar(value="QR creador")
text_var3 = tkinter.StringVar(value="QR lector")

label1 = customtkinter.CTkLabel(master=root,
                               textvariable=text_var1,
                               width=150,
                               height=30,
                               corner_radius=8,
                               bg_color=("gray10"),
                               text_color=("white"))
label1.place(relx=0.5, rely=0.01, anchor=tkinter.N)
























boton1 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Select Images",
                                 command=select_file)
boton1.place(relx=0.2, rely=0.2, anchor=tkinter.S)
boton2 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="generar",
                                 command=generar)
boton2.place(relx=0.2, rely=0.3, anchor=tkinter.S)
boton3 = button = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="leer",
                                 command=leer)
boton3.place(relx=0.2, rely=0.4, anchor=tkinter.S)
boton4 = button = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="guardar",
                                 command=guardar)
boton4.place(relx=0.2, rely=0.5, anchor=tkinter.S)
boton5 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="create_toplevel",
                                 command=create_toplevel)
boton5.place(relx=0.2, rely=6, anchor=tkinter.S)






































root.mainloop()

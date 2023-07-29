import customtkinter as ctk
from tkinter import Entry

#Configurando a janela
root = ctk.CTk()
ctk.set_appearance_mode('light')
root.geometry('380x500')
root.resizable(False, False)
root.iconbitmap("image/icon.ico")

#Label Login

user_label = ctk.CTkLabel(root, text='E-mail:', font=('Helvetica', 20))
user_label.place(x=160, y=40)

user_entry = ctk.CTkEntry(root, width=294, font=('Helvetica', 20), fg_color='#ebebeb', border_width=0)  
user_entry.place(x=50, y=80)

frame = ctk.CTkFrame(root, width=294, height=3, bg_color='black')
frame.place(x=50, y=110)


pass_label = ctk.CTkLabel(root, text='Senha:', font=('Helvetica', 20))
pass_label.place(x=160, y=180)

pass_entry = ctk.CTkEntry(root, width=294, show='*', fg_color='#ebebeb', border_width=0)
pass_entry.place(x=50, y=210)

frame = ctk.CTkFrame(root, width=294, height=3, bg_color='black')
frame.place(x=50, y=240)


btn_login = ctk.CTkButton(root, text='Entrar', font=('Helvetica bold', 24,'bold'), fg_color='#15e280', hover_color='#02f681', corner_radius=25, height=38, width=155)
btn_login.place(x=111, y=320)



esqueceu_pass = ctk.CTkButton(root, text='Esqueci minha senha', font=('Helvetica bold', 14), border_width=0, fg_color='#ebebeb' ,text_color='#5f82ff', hover_color='#ebebeb', corner_radius=25)
esqueceu_pass.place(x=111, y=390)

spam = ctk.CTkLabel(root, text='Não possui cadastro?', font=('Helvetica', 14), bg_color=('transparent'))
spam.place(x=80, y=410)

cadastro_label = ctk.CTkButton(root, width=50, text='Clique aqui', font=('Helvetica bold', 14), border_width=0, fg_color='#ebebeb' ,text_color='#5f82ff', hover_color='#ebebeb')
cadastro_label.place(x=220, y=410)






root.mainloop()
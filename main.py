import builtins
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#Trabalhando com frame do Logo

app_lg = Image.open('kaio/assets/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text= "Cadastro de Clientes", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=("ivy 15 bold"), bg = co6, fg=co0)
app_logo.place(x=0, y=0)



#função cliente
def cliente():
    print('Cliente')

#função para adicionar
def adicionar():
    print('adicionar')
        
def salvar():
    print('salvar')

#Função de controle ------------------
def controle(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        cliente()

    elif i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        adicionar()

    elif i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        salvar()

    




#Criando botões
app_img_cadastro = Image.open('kaio/assets/add_box_icon.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:controle('cadastro'), image=app_img_cadastro, text= "Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=("ivy 11"), bg = co1, fg=co0)
app_cadastro.place(x=10, y=30)  

app_img_add = Image.open('kaio/assets/add_box_icon.png')
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_adicionar = Button(frame_dados, command=lambda:controle('adicionar'), image=app_img_add, text= "Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=("ivy 11"), bg = co1, fg=co0)
app_adicionar.place(x=120, y=30)  

app_img_save = Image.open('kaio/assets/save_icon.png')
app_img_save = app_img_save.resize((18,18))
app_img_save = ImageTk.PhotoImage(app_img_save)
app_salvar = Button(frame_dados,command=lambda:controle('salvar'), image=app_img_save, text= "Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=("ivy 11"), bg = co1, fg=co0)
app_salvar.place(x=230, y=30)  

janela.mainloop()
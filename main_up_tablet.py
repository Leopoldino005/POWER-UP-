''' Programação do Protótipo do tablet POWER UP'''

# Impotando as blibliotecas
from tkinter import *

class Editar(Toplevel): # tela de edição de vídeos e informações
    
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP EDIÇÃO DE EXERCÍCIOS')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        #imagens
        self.video = PhotoImage(file='adiciona video.png')
        self.image = Label(self, image=self.video)
        self.image.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.65)

        self.aviso = PhotoImage(file='adiciona aviso.png')
        self.image = Label(self, image=self.aviso)
        self.image.place(relx=0.5, rely=0.2, relwidth=0.467, relheight=0.46)
        
        #botões
        self.bot = Button(self, text='EDITAR', font=('Britannic Bold', 14), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot.place(relx=0.73, rely=0.23, relwidth=0.1, relheight=0.05)

        self.bot2 = Button(self, text='EDITAR', font=('Britannic Bold', 14), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot2.place(relx=0.52, rely=0.39, relwidth=0.1, relheight=0.05)

        self.img = PhotoImage(file='btn_voltar.png')
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.041, rely=0.76)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Rmartelo_edite(Toplevel): #tela de edição do exercício rosca martelo
    
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP BRAÇOS')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        #imagem
        self.roscaM_ex = PhotoImage(file='rosca martelo-exemplo.png')
        self.image = Label(self, image=self.roscaM_ex)
        self.image.place(relx=0.15, rely=0.06)

        self.aviso = PhotoImage(file='aviso.png')
        self.image = Label(self, image=self.aviso)
        self.image.place(relx=0.53, rely=0.06)
        #botões
        self.img = PhotoImage(file='btn_voltar.png') 
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.15, rely=0.7)

        self.bot1 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot1.place(relx=0.15, rely=0.587, relwidth=0.2, relheight=0.1)

        self.bot2 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot2.place(relx=0.53, rely=0.587, relwidth=0.2, relheight=0.1)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Rmartelo(Toplevel): # tela do exercício rosca martelo
    
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP ROSCA MARTELO')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        #imagem
        self.roscaM_ex = PhotoImage(file='rosca martelo-exemplo.png')
        self.image = Label(self, image=self.roscaM_ex)
        self.image.place(relx=0.15, rely=0.06)

        self.aviso = PhotoImage(file='aviso.png')
        self.image = Label(self, image=self.aviso)
        self.image.place(relx=0.53, rely=0.06)
        #botão
        self.img = PhotoImage(file='btn_voltar.png')
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.15, rely=0.6)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Braco_edite(Toplevel):
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP BRAÇOS EDIÇÃO')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        # imagens
        self.roscaM = PhotoImage(file='rosca martelo.png')
        self.image = Label(self, image=self.roscaM)
        self.image.place(relx=0.04, rely=0.01)

        self.ttb = PhotoImage(file='triceps testa com barra.png')
        self.image = Label(self, image=self.ttb)
        self.image.place(relx=0.65, rely=0.4)

        self.roscaB = PhotoImage(file='rosca com barra.png')
        self.image = Label(self, image=self.roscaB)
        self.image.place(relx=0.65, rely=0.01)

        self.barraF = PhotoImage(file='barra fixa.png')
        self.image = Label(self, image=self.barraF)
        self.image.place(relx=0.04, rely=0.4)

        # botões
        self.bot1 = Button(self, text='ROSCA MARTELO', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4', command=self.entrarr_ed)
        self.bot1.place(relx=0.041, rely=0.27, relwidth=0.322, relheight=0.1)

        self.bot2 = Button(self, text='BARRA FIXA', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot2.place(relx=0.041, rely=0.64, relwidth=0.3229, relheight=0.1)

        self.bot3 = Button(self, text='ROSCA COM BARRA', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot3.place(relx=0.651, rely=0.27, relwidth=0.322, relheight=0.1)

        self.bot4 = Button(self, text='ADICIONAR', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot4.place(relx=0.651, rely=0.64, relwidth=0.322, relheight=0.1)

        self.img = PhotoImage(file='btn_voltar.png')  # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.041, rely=0.76)

        self.bot5 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot5.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.05)

        self.bot6 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot6.place(relx=0.65, rely=0.01, relwidth=0.1, relheight=0.05)

        self.bot7 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot7.place(relx=0.04, rely=0.4, relwidth=0.1, relheight=0.05)

        self.bot8 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot8.place(relx=0.04, rely=0.01, relwidth=0.1, relheight=0.05)
    #mudança de tela
    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def entrarr_ed(self):
        self.hide()
        self.subFrame = Rmartelo_edite(self)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Adm(Toplevel): # tela de login do administrador
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP ADM')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        self.frame1 = Frame(self, bg='#f48c06')
        self.frame1.place(relx=0, rely=0.11, relwidth=1, relheight=0.13)

        self.caixat = Entry(self.frame1, font=("Arial", 12), fg="black")
        self.caixat.place(relx=0.07, rely=0.54, relwidth=0.85, relheight=0.05)

        self.titulo = Label(self.frame1, text='ENTRAR', font=('Britannic Bold', 30), bg='#f48c06', fg='black')
        self.titulo.place(relx=0.1, rely=0.15)

        self.email = Label(self, text='E-mail:', font=('Britannic Bold', 20), bg='white', fg='black')
        self.email.place(relx=0.15, rely=0.28)

        self.email_entry = Entry(self, bg='#ced4da', fg='black', font=('Britannic Bold', 16))
        self.email_entry.place(relx=0.22, rely=0.28, relwidth=0.7, relheight=0.06)

        self.senha = Label(self, text='Senha:', font=('Britannic Bold', 20), bg='white', fg='black')
        self.senha.place(relx=0.15, rely=0.35)

        self.senha_entry = Entry(self, show='*', bg='#ced4da', fg='black', font=('Britannic Bold', 16))
        self.senha_entry.place(relx=0.22, rely=0.35, relwidth=0.7, relheight=0.06)

        self.txt1 = Label(self, text='Esqueceu sua senha?', font=('Britannic', 20), bg='white', fg='black')
        self.txt1.place(relx=0.15, rely=0.43)

        self.btn_senha = Button(self, bg='#f48c06', fg='white', text='Substituir Senha', font=('Britannic Bold', 20))
        self.btn_senha.place(relx=0.17, rely=0.5, relwidth=0.17, relheight=0.06)

        self.btn_entrar = Button(self, bg='#f48c06', fg='white', text='Entrar', font=('Britannic Bold', 20),
                                 command=self.entrar_adm)
        self.btn_entrar.place(relx=0.75, rely=0.43, relwidth=0.17, relheight=0.08)

        self.txt2 = Label(self, text='Caso não possua conta, clique em cadastre-se:', font=('Britannic', 20),
                          bg='white', fg='black')
        self.txt2.place(relx=0.15, rely=0.7)

        self.btn_cadastro = Button(self, bg='#f48c06', fg='white', text='Cadastra-se', font=('Britannic Bold', 20))
        self.btn_cadastro.place(relx=0.17, rely=0.76, relwidth=0.17, relheight=0.08)

        self.img = PhotoImage(file='btn_voltar.png')  # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.041, rely=0.76)

    def limpa_tela(self):
        self.email_entry.delete(0, END)
        self.senha_entry.delete(0, END)

    # mudança de tela
    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def entrar_adm(self):
        self.hide()
        self.subFrame = Adm_edite(self)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Adm_edite(Toplevel): #tela de edição de exercícios
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP EDIÇÃO DE EXERCÍCIOS')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        #imagens
        self.logo = PhotoImage(file='logo-POWER UP.png')
        self.image = Label(self, image=self.logo)
        self.image.place(relx=0.24, rely=0.4, relwidth=0.52, relheight=0.62)

        self.braco = PhotoImage(file='braço.png')
        self.image = Label(self, image=self.braco)
        self.image.place(relx=0.04, rely=0.02)

        self.flex = PhotoImage(file='flexao.png')
        self.image = Label(self, image=self.flex)
        self.image.place(relx=0.65, rely=0.43)

        self.perna = PhotoImage(file='perna.png')
        self.image = Label(self, image=self.perna)
        self.image.place(relx=0.65, rely=0.02)

        self.pesos = PhotoImage(file='pesos.png')
        self.image = Label(self, image=self.pesos)
        self.image.place(relx=0.04, rely=0.43)
        # botões
        self.bot1 = Button(self, text='BRAÇOS', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4',
                           command=self.entrarBed)
        self.bot1.place(relx=0.041, rely=0.3, relwidth=0.322, relheight=0.1)

        self.bot2 = Button(self, text='PESOS', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot2.place(relx=0.041, rely=0.7, relwidth=0.3229, relheight=0.1)

        self.bot3 = Button(self, text='PERNAS', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot3.place(relx=0.651, rely=0.3, relwidth=0.322, relheight=0.1)

        self.bot4 = Button(self, text='ADICIONAR', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4', command=self.entrarAd)
        self.bot4.place(relx=0.651, rely=0.7, relwidth=0.322, relheight=0.1)

        self.bot5 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot5.place(relx=0.65, rely=0.43, relwidth=0.1, relheight=0.05)

        self.bot6 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot6.place(relx=0.65, rely=0.02, relwidth=0.1, relheight=0.05)

        self.bot7 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot7.place(relx=0.04, rely=0.43, relwidth=0.1, relheight=0.05)

        self.bot8 = Button(self, text='EDITAR', font=('Britannic Bold', 20), bg='#a5a58d', activebackground='#b7b7a4')
        self.bot8.place(relx=0.04, rely=0.02, relwidth=0.1, relheight=0.05)
        
        self.img = PhotoImage(file='btn_voltar.png')
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.046, rely=0.82)
    # mudança de tela
    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def entrarBed(self):
        self.hide()
        self.subFrame = Braco_edite(self)

    def entrarAd(self):
        self.hide()
        self.subFrame = Editar(self)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Braco(Toplevel): #tela de exercícios especificos (Braços)
    def __init__(self, original): # Método Construtor
        self.frame_original = original
        Toplevel.__init__(self)
        self.tela()
        self.widgets()

    def tela(self): # configuração de tela
        self.title('POWER UP BRAÇOS')
        self.configure(bg='white')
        self.iconbitmap('powerup_icone.ico')
        self.geometry('1080x650+10+6')
        self.resizable(False, False)

    def widgets(self): # configuração de widgets
        # imagens
        self.roscaM = PhotoImage(file='rosca martelo.png')
        self.image = Label(self, image=self.roscaM)
        self.image.place(relx=0.04, rely=0.01)

        self.ttb = PhotoImage(file='triceps testa com barra.png')
        self.image = Label(self, image=self.ttb)
        self.image.place(relx=0.65, rely=0.4)

        self.roscaB = PhotoImage(file='rosca com barra.png')
        self.image = Label(self, image=self.roscaB)
        self.image.place(relx=0.65, rely=0.01)

        self.barraF = PhotoImage(file='barra fixa.png')
        self.image = Label(self, image=self.barraF)
        self.image.place(relx=0.04, rely=0.4)

        # botões
        self.bot1 = Button(self, text='ROSCA MARTELO', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4', command=self.entrarR)
        self.bot1.place(relx=0.041, rely=0.27, relwidth=0.322, relheight=0.1)

        self.bot2 = Button(self, text='BARRA FIXA', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot2.place(relx=0.041, rely=0.64, relwidth=0.3229, relheight=0.1)

        self.bot3 = Button(self, text='ROSCA COM BARRA', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot3.place(relx=0.651, rely=0.27, relwidth=0.322, relheight=0.1)

        self.bot4 = Button(self, text='TESTA COM BARRA', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot4.place(relx=0.651, rely=0.64, relwidth=0.322, relheight=0.1)

        self.img = PhotoImage(file='btn_voltar.png')
        self.btn_voltar = Button(self, image=self.img, command=self.onClose)
        self.btn_voltar.place(relx=0.041, rely=0.76)
    # mudança de tela
    def hide(self):
        self.withdraw()

    def show(self):
        self.update()
        self.deiconify()

    def entrarR(self):
        self.hide()
        self.subFrame = Rmartelo(self)

    def onClose(self): # retorna à ultima tela
        self.destroy()
        self.frame_original.show()

class Aplicativo:
    def __init__(self): # Método Construtor
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()

    def tela(self): # configuração de tela
        self.root.title('POWER UP')
        root.configure(bg='white')
        root.iconbitmap('powerup_icone.ico')
        self.root.geometry('1080x650+10+6')
        self.root.resizable(False, False)

    def widgets(self): # configuração de widgets
        # imagem
        self.logo = PhotoImage(file='logo-POWER UP.png')
        self.image = Label(self.root, image=self.logo)
        self.image.place(relx=0.24, rely=0.4, relwidth=0.52, relheight=0.62)

        self.braco = PhotoImage(file='braço.png')
        self.image = Label(self.root, image=self.braco)
        self.image.place(relx=0.04, rely=0.06)

        self.flex = PhotoImage(file='flexao.png')
        self.image = Label(self.root, image=self.flex)
        self.image.place(relx=0.65, rely=0.56)

        self.perna = PhotoImage(file='perna.png')
        self.image = Label(self.root, image=self.perna)
        self.image.place(relx=0.65, rely=0.06)

        self.pesos = PhotoImage(file='pesos.png')
        self.image = Label(self.root, image=self.pesos)
        self.image.place(relx=0.04, rely=0.56)
        # botões
        self.bot1 = Button(self.root, text='BRAÇOS', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4', command=self.entrarB)
        self.bot1.place(relx=0.041, rely=0.34, relwidth=0.322, relheight=0.1)

        self.bot2 = Button(self.root, text='PESOS', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot2.place(relx=0.041, rely=0.84, relwidth=0.3229, relheight=0.1)

        self.bot3 = Button(self.root, text='PERNAS', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4')
        self.bot3.place(relx=0.651, rely=0.34, relwidth=0.322, relheight=0.1)

        self.bot4 = Button(self.root, text='ADMINISTRADOR', font=('Britannic Bold', 20), bg='#a5a58d',
                           activebackground='#b7b7a4', command=self.entrarA)
        self.bot4.place(relx=0.651, rely=0.84, relwidth=0.322, relheight=0.1)
    # mudança de tela
    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def entrarB(self):
        self.hide()
        self.subFrame = Braco(self)

    def entrarA(self):
        self.hide()
        self.subFrame = Adm(self)

##### PROGRAMA PRINCIPAL #####
root = Tk()
Aplicativo()
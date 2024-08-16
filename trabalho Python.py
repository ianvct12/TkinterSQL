from tkinter import *
import mysql.connector
import customtkinter as ctk
import tkinter.messagebox as MessageBox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#window
window = ctk.CTk()
window.title('Caso do Léo')
window.geometry('800x600')
window.resizable(width=False,height=False)
'''conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database = 'casadoleo'
)'''

#x=conexao.cursor()

'''x.execute('create database casadoleo')'''

#x.execute('Create Table doador_pessoa(cpf varchar(14) primary key, nome varchar(64), senha varchar(64), telefone varchar(13), endereco varchar(128), email varchar(64), doacao varchar(50), qtd int(10))')
#x.execute('Create Table doador_empresa(cnpj varchar(18) primary key, nome varchar(64), senha varchar(64), telefone varchar(13), endereco varchar(128), email varchar(64), doacao varchar(50), qtd int(10))')
#x.execute('Create Table voluntario(cpf varchar(14) primary key, nome varchar(64), senha varchar(64), telefone varchar(13), endereco varchar(128), email varchar(64))')
        
    
#Janela Doador - Pessoa física - Cadastrar
def janelaDoadorPF():
    novaJanela=Toplevel(window)
    novaJanela.title("Cadastro de Doadores - Pessoa Física")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Cadastro de Doadores Pessoa Física',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome.place(x=10,y=20)
    
    e_nome = ctk.CTkEntry(novaJanela, placeholder_text='Nome Completo')
    e_nome.place(x=75,y=20)

    label_email = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email.place(x=10, y=55)
    
    e_email = ctk.CTkEntry(novaJanela)
    e_email.place(x=75, y=55)

    label_cpf=ctk.CTkLabel(novaJanela, text='CPF: ', font=('Arial',12), text_color='white')
    label_cpf.place(x=10, y=90)
    
    e_cpf=ctk.CTkEntry(novaJanela)
    e_cpf.place(x=75, y=90 )

    label_senha=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha.place(x=10,y=125)
    
    e_senha = ctk.CTkEntry(novaJanela, show = '*')
    e_senha.place(x=75, y = 125)

    label_telefone=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white')
    label_telefone.place(x=10,y=160)
    
    e_telefone = ctk.CTkEntry(novaJanela)
    e_telefone.place(x=75,y=160)

    label_endereco=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco.place(x=10,y=195)
    
    e_endereco = ctk.CTkEntry(novaJanela)
    e_endereco.place(x=75,y=195)

    label_doacao=ctk.CTkLabel(novaJanela, text='Doação: ', font=('Arial',12), text_color='white')
    label_doacao.place(x=10,y=230)
    
    e_doacao = ctk.CTkEntry(novaJanela)
    e_doacao.place(x=75,y=230)

    label_qtd=ctk.CTkLabel(novaJanela, text='Quantidade: ', font=('Arial',12), text_color='white').place(x=11,y=265)
    e_qtd = ctk.CTkEntry(novaJanela)
    e_qtd.place(x=75,y=265)
    
#Inserir na tabela doadores (Pessoa Física)
    def inserir_doador_pessoaPF():
        cpf=e_cpf.get()
        nome=e_nome.get()
        senha=e_senha.get()
        telefone=e_telefone.get()
        endereco=e_endereco.get()
        email=e_email.get()
        doacao=e_doacao.get()
        qtd=e_qtd.get()

        if(nome =='' or cpf =='' or email =='' or telefone=='' or senha=='' or endereco=='' or doacao=='' or qtd==''):
            MessageBox.showinfo('Status inserido','Todos os campos são obrigatórios')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('insert into doador_pessoa values(%s,%s,%s,%s,%s,%s,%s,%s)',(cpf,nome,senha,telefone,endereco,email,doacao,qtd))
            con.commit()
            MessageBox.showinfo('Status inserido','Cadastrado com sucesso!')
            con.close()
            
    botao_cadastrar = ctk.CTkButton(novaJanela, text = 'Cadastrar',height=20, width=40, border_spacing=4,  fg_color='white', text_color='black', command =inserir_doador_pessoaPF)
    botao_cadastrar.place(x=20, y=320)



#Janela Doador - Pessoa física - Excluir
    

def janelaExcluirPF():
    novaJanela=Toplevel(window)
    novaJanela.title("Exclusão de Doadores - Pessoa Física")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Excluir Doador Pessoa Física',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)


    label_cpf=ctk.CTkLabel(novaJanela, text='Digite o CPF: ', font=('Arial',12), text_color='white')
    label_cpf.place(x=10, y=90)
    
    e_cpf=ctk.CTkEntry(novaJanela)
    e_cpf.place(x=95, y=90 )

    
    
#Excluir na tabela doadores (Pessoa Física)
 
    def excluir_pf():
        cpf=e_cpf.get()
            
        if(cpf==''):
             MessageBox.showinfo("Status inserido","É necessário preencher o CPF.")
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo'
            )
                
            cursor=con.cursor()

            cursor.execute('delete from doador_pessoa where cpf='+cpf)
            con.commit()
            MessageBox.showinfo("Status Inserido","Doador removido com sucesso!")
            con.close()
            
            

    botao_excluir = ctk.CTkButton(novaJanela, text = 'Excluir',height=20, width=40, border_spacing=4,  fg_color='white', text_color='black', command =excluir_pf)
    botao_excluir.place(x=20, y=150)



#Janela Doador Pessoa Física - Alterar
def alterar_doador_pessoaPF():
    novaJanela=Toplevel(window)
    novaJanela.title("Alterar cadastro de Doadores - Pessoa Física")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Alterar Cadastro de Doadores Pessoa Física',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome.place(x=10,y=20)
    
    e_nome = ctk.CTkEntry(novaJanela, placeholder_text='Nome Completo')
    e_nome.place(x=75,y=20)

    label_email = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email.place(x =10, y = 55)
    
    e_email = ctk.CTkEntry(novaJanela)
    e_email.place(x=75, y = 55)

    label_cpf=ctk.CTkLabel(novaJanela, text='CPF: ', font=('Arial',12), text_color='white')
    label_cpf.place(x=10,y=90)
    
    e_cpf=ctk.CTkEntry(novaJanela)
    e_cpf.place(x=75, y=90)

    label_senha=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha.place(x=10,y=125)
    
    e_senha = ctk.CTkEntry(novaJanela, show = '*')
    e_senha.place(x=75, y = 125)

    label_telefone=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white')
    label_telefone.place(x=10,y=160)
    
    e_telefone = ctk.CTkEntry(novaJanela)
    e_telefone.place(x=75,y=160)

    label_endereco=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco.place(x=10,y=195)
    
    e_endereco = ctk.CTkEntry(novaJanela)
    e_endereco.place(x=75,y=195)

    label_doacao=ctk.CTkLabel(novaJanela, text='Doação: ', font=('Arial',12), text_color='white')
    label_doacao.place(x=10,y=230)
    
    e_doacao = ctk.CTkEntry(novaJanela)
    e_doacao.place(x=75,y=230)

    label_qtd=ctk.CTkLabel(novaJanela, text='Quantidade: ', font=('Arial',12), text_color='white')
    label_qtd.place(x=10,y=265)
    
    e_qtd = ctk.CTkEntry(novaJanela)
    e_qtd.place(x=75,y=265)

#Alterar Doador Pessoa Física
    def modificar_doador_pessoaPF():
        cpf=e_cpf.get()
        nome=e_nome.get()
        senha=e_senha.get()
        telefone=e_telefone.get()
        endereco=e_endereco.get()
        email=e_email.get()
        doacao=e_doacao.get()
        qtd=e_qtd.get()

        if(cpf ==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CPF para alterar o cadastro.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('UPDATE doador_pessoa set nome=%s, senha=%s,telefone=%s,endereco=%s,email=%s,doacao=%s,qtd=%s where cpf=%s',(nome,senha,telefone,endereco,email,doacao,qtd,cpf))
            con.commit()
            MessageBox.showinfo('Status inserido','Alteração realizada com sucesso!')
            con.close()
            
    botao = ctk.CTkButton(novaJanela, text = 'Alterar', height=20, width=40, border_spacing=4, border_width=2, fg_color='white', text_color='black', command = modificar_doador_pessoaPF)
    botao.place(x=10,y=320)


#Janela Doador - Pessoa física - Consultar
    

def janelaConsultarPF():
    novaJanela=Toplevel(window)
    novaJanela.title("Consulta de Doadores - Pessoa Física")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Consultar Doador Pessoa Física',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)


    label_cpf=ctk.CTkLabel(novaJanela, text='Digite o CPF: ', font=('Arial',12), text_color='white')
    label_cpf.place(x=10, y=90)
    
    e_cpf=ctk.CTkEntry(novaJanela)
    e_cpf.place(x=95, y=90 )

    
    
#Consultar na tabela doadores (Pessoa Física)
 
    def consultar_pf():
        cpf=e_cpf.get()
            
        if(cpf==''):
             MessageBox.showinfo("Status inserido","É necessário preencher o CPF.")
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo'
            )
                
            cursor=con.cursor()

            cursor.execute('select * from doador_pessoa where cpf='+cpf)
            result = cursor.fetchall()#percorre toas as linhas da tabela
            for j in result:
                MessageBox.showinfo("Status Inserido",result)
            con.close()
            
            
#Botão para Consultar
    botao_consultar = ctk.CTkButton(novaJanela, text = 'Consultar',height=20, width=40, border_spacing=4,  fg_color='white', text_color='black', command =consultar_pf)
    botao_consultar.place(x=20, y=150)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------#

#Janela Voluntário - Cadastrar
def janelaVoluntario():
    novaJanela=Toplevel(window)
    novaJanela.title("Cadastro de Voluntários")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Cadastro de Voluntários',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome2 = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome2.place(x=10,y=20)
    
    e_nome2 = ctk.CTkEntry(novaJanela,placeholder_text='Nome Completo')
    e_nome2.place(x=75, y=20)

    label_email2 = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email2.place(x =10, y = 55)
    
    e_email2 = ctk.CTkEntry(novaJanela)
    e_email2.place(x = 75, y = 55)

    label_cpf2=ctk.CTkLabel(novaJanela, text='CPF: ', font=('Arial',12), text_color='white')
    label_cpf2.place(x=10,y=90)
    
    e_cpf2=ctk.CTkEntry(novaJanela)
    e_cpf2.place(x = 75, y=90 )

    label_senha2=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha2.place(x=10,y=125)
    
    e_senha2 = ctk.CTkEntry(novaJanela, show = '*')
    e_senha2.place(x = 75, y = 125)

    label_telefone2=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white')
    label_telefone2.place(x=10,y=160)
    
    e_telefone2 = ctk.CTkEntry(novaJanela)
    e_telefone2.place(x=75,y=160)

    label_endereco2=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco2.place(x=10,y=195)
    
    e_endereco2 = ctk.CTkEntry(novaJanela)
    e_endereco2.place(x=75,y=195)

    def inserir_voluntario():
        cpf2=e_cpf2.get()
        nome2=e_nome2.get()
        senha2=e_senha2.get()
        telefone2=e_telefone2.get()
        endereco2=e_endereco2.get()
        email2=e_email2.get()
    
        if(nome2 =='' or cpf2=='' or senha2=='' or telefone2=='' or endereco2=='' or email2==''):
            MessageBox.showinfo('Status inserido','Todos os campos são Obrigatórios')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('insert into voluntario values(%s,%s,%s,%s,%s,%s)',(cpf2,nome2,senha2,telefone2,endereco2,email2))
            con.commit()
            MessageBox.showinfo('Status inserido','Cadastro com sucesso!')
            con.close()


    botao = ctk.CTkButton(novaJanela, text = 'Cadastrar', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = inserir_voluntario)
    botao.place(x= 20, y = 240)




#Janela Voluntário - Excluir
def janelaExcluirVoluntario():
    novaJanela=Toplevel(window)
    novaJanela.title("Exclusão de Voluntários")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Excluir Voluntários',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_cpf2=ctk.CTkLabel(novaJanela, text='Digite o CPF: ', font=('Arial',12), text_color='white')
    label_cpf2.place(x=10,y=90)
    
    e_cpf2=ctk.CTkEntry(novaJanela)
    e_cpf2.place(x=95, y=90 )

    def excluir_voluntario():
        cpf2=e_cpf2.get()
        
    
        if(cpf2==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CPF.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('delete from voluntario where cpf='+cpf2)
            con.commit()
            MessageBox.showinfo('Status inserido','Cadastro com sucesso!')
            con.close()


    botao = ctk.CTkButton(novaJanela, text = 'Excluir', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = excluir_voluntario)
    botao.place(x= 20, y = 150)




#Janela Voluntário- Alterar
def alterar_voluntario():
    novaJanela=Toplevel(window)
    novaJanela.title("Cadastro de Voluntários")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Cadastro de Voluntários',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome2 = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome2.place(x=20,y=20)
    
    e_nome2 = ctk.CTkEntry(novaJanela,placeholder_text='Nome Completo')
    e_nome2.place(x=66, y=20)

    label_email2 = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email2.place(x=20, y=55)
    
    e_email2 = ctk.CTkEntry(novaJanela)
    e_email2.place(x=66, y=55)

    label_cpf2=ctk.CTkLabel(novaJanela, text='CPF: ', font=('Arial',12), text_color='white')
    label_cpf2.place(x=20,y=90)
    
    e_cpf2=ctk.CTkEntry(novaJanela)
    e_cpf2.place(x = 66, y=90 )

    label_senha2=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha2.place(x=20,y=125)
    
    e_senha2 = ctk.CTkEntry(novaJanela, show = '*')
    e_senha2.place(x = 66, y = 125)

    label_telefone2=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white')
    label_telefone2.place(x=11,y=160)
    
    e_telefone2 = ctk.CTkEntry(novaJanela)
    e_telefone2.place(x=66,y=160)

    label_endereco2=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco2.place(x=11,y=195)
    
    e_endereco2 = ctk.CTkEntry(novaJanela)
    e_endereco2.place(x=66,y=195)

#Alterar Voluntário
    def modificar_voluntario():
        cpf2=e_cpf2.get()
        nome2=e_nome2.get()
        senha2=e_senha2.get()
        telefone2=e_telefone2.get()
        endereco2=e_endereco2.get()
        email2=e_email2.get()

        if(cpf2 ==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CPF para alterar o cadastro.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('UPDATE voluntario set nome=%s, senha=%s,telefone=%s,endereco=%s,email=%s where cpf=%s',(nome2,senha2,telefone2,endereco2,email2,cpf2))
            con.commit()
            MessageBox.showinfo('Status inserido','Alteração realizada com sucesso!')
            con.close()
            
    botao = ctk.CTkButton(novaJanela, text = 'Alterar',height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = modificar_voluntario).place(x=10,y=240)





#Janela Voluntário - Consultar
def janelaConsultarVoluntario():
    novaJanela=Toplevel(window)
    novaJanela.title("Consulta de Voluntários")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Consulta Voluntários',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_cpf2=ctk.CTkLabel(novaJanela, text='Digite o CPF: ', font=('Arial',12), text_color='white')
    label_cpf2.place(x=10,y=90)
    
    e_cpf2=ctk.CTkEntry(novaJanela)
    e_cpf2.place(x=95, y=90)

    def consultar_voluntario():
        cpf2=e_cpf2.get()
        
    
        if(cpf2==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CPF.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('select * from voluntario where cpf='+cpf2)
            result = cursor.fetchall()#percorre toas as linhas da tabela
            for j in result:
                    MessageBox.showinfo("Status Inserido",result)
            con.close()


    botao = ctk.CTkButton(novaJanela, text = 'Consultar', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = consultar_voluntario)
    botao.place(x= 20, y = 150)






#-----------------------------------------------------------------------------------------------------------------------------------#        
#Janela Doador - Pessoa Jurídica 
def janelaDoadorPJ():
    novaJanela=Toplevel(window)
    novaJanela.title("Cadastro de Doadores - Pessoa Jurídica")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Cadastro de Doadores Pessoa Jurídica',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome.place(x=10,y=20)
    
    e_nome = ctk.CTkEntry( novaJanela,placeholder_text='Nome Completo')
    e_nome.place(x=75,y=20)

    label_email = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email.place(x=10, y=55)
    
    e_email = ctk.CTkEntry(novaJanela)
    e_email.place(x=75, y=55)

    label_cnpj=ctk.CTkLabel(novaJanela, text='CNPJ: ', font=('Arial',12), text_color='white')
    label_cnpj.place(x=10,y=90)
    
    e_cnpj=ctk.CTkEntry(novaJanela)
    e_cnpj.place(x=75, y=90 )

    label_senha=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha.place(x=10,y=125)
    
    e_senha = ctk.CTkEntry(novaJanela, show = '*')
    e_senha.place(x = 75, y = 125)

    label_telefone=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white')
    label_telefone.place(x=11,y=160)
    
    e_telefone = ctk.CTkEntry(novaJanela)
    e_telefone.place(x=75,y=160)

    label_endereco=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco.place(x=11,y=195)
    
    e_endereco = ctk.CTkEntry(novaJanela)
    e_endereco.place(x=75,y=195)

    label_doacao=ctk.CTkLabel(novaJanela, text='Doação: ', font=('Arial',12), text_color='white')
    label_doacao.place(x=10,y=230)
    
    e_doacao = ctk.CTkEntry(novaJanela)
    e_doacao.place(x=75,y=230)
  
    label_qtd=ctk.CTkLabel(novaJanela,text='Quantidade: ',font=('Arial',12), text_color='white')
    label_qtd.place(x=10,y=265)
    
    e_qtd=ctk.CTkEntry(novaJanela)
    e_qtd.place(x=75,y=265)

#Inserir na tabela doadores (Pessoa Jurídica)        
    def inserir_doador_pessoaPJ():
        cnpj=e_cnpj.get()
        nome=e_nome.get()
        senha=e_senha.get()
        telefone=e_telefone.get()
        endereco=e_endereco.get()
        email=e_email.get()
        doacao=e_doacao.get()
        qtd=e_qtd.get()
    
        if(nome =='' or cnpj=='' or email =='' or telefone=='' or senha=='' or endereco=='' or doacao=='' or qtd==''):
            MessageBox.showinfo('Status inserido','Todos os campos são obrigatórios')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('insert into doador_empresa values(%s,%s,%s,%s,%s,%s,%s,%s)',(cnpj,nome,senha,telefone,endereco,email, doacao, qtd))
            con.commit()
            MessageBox.showinfo('Status inserido','Cadastrado com sucesso!')
            con.close()
        
    botao = ctk.CTkButton(novaJanela, text = 'Cadastrar', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = inserir_doador_pessoaPJ)
    botao.place(x= 20, y = 320)




#Janela Doador - Excluir Pessoa Jurídica 
def janelaExcluirPJ():
    novaJanela=Toplevel(window)
    novaJanela.title("Exclusão de Doadores - Pessoa Jurídica")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Excluir Doadores Pessoa Jurídica',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_cnpj=ctk.CTkLabel(novaJanela, text='Digite o CNPJ: ', font=('Arial',12), text_color='white')
    label_cnpj.place(x=10,y=90)
    
    e_cnpj=ctk.CTkEntry(novaJanela)
    e_cnpj.place(x=95, y=90 )


#Exclusão na tabela doadores (Pessoa Jurídica)        
    def excluir_doador_pessoaPJ():
        cnpj=e_cnpj.get()
        
    
        if(cnpj==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CNPJ.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('delete from doador_empresa where cnpj='+cnpj)
            con.commit()
            MessageBox.showinfo("Status Inserido","Doador removido com sucesso!")
            con.close()
        
    botao = ctk.CTkButton(novaJanela, text = 'Excluir', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = excluir_doador_pessoaPJ)
    botao.place(x=20, y=150)




#Janela Doador - Consultar Pessoa Jurídica 
def janelaConsultarPJ():
    novaJanela=Toplevel(window)
    novaJanela.title("Consulta de Doadores - Pessoa Jurídica")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Consulta de Doadores Pessoa Jurídica',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_cnpj=ctk.CTkLabel(novaJanela, text='Digite o CNPJ: ', font=('Arial',12), text_color='white')
    label_cnpj.place(x=10,y=90)
    
    e_cnpj=ctk.CTkEntry(novaJanela)
    e_cnpj.place(x=95, y=90 )


#Consulta na tabela doadores (Pessoa Jurídica)        
    def consultar_doador_pessoaPJ():
        cnpj=e_cnpj.get()
        
        if(cnpj==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CNPJ.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo'
                )
            cursor = con.cursor()
            cursor.execute('select * from doador_empresa where cnpj='+cnpj)
            result = cursor.fetchall()#percorre toas as linhas da tabela
            for j in result:
                MessageBox.showinfo("Status Inserido",result)
            con.close()
        
    botao = ctk.CTkButton(novaJanela, text = 'Consultar', height=20, width=40, border_spacing=4, fg_color='white', text_color='black', command = consultar_doador_pessoaPJ)
    botao.place(x=20, y=150)
    

#Janela Doador Pessoa Jurídica - Alterar
def alterar_doador_pessoaPJ():
    novaJanela=Toplevel(window)
    novaJanela.title("Cadastro de Doadores - Pessoa Jurídica")
    novaJanela.geometry('1200x800')
    novaJanela.configure(bg='black')
    label_prin = ctk.CTkLabel(novaJanela,text='Alterar Cadastro de Doadores Pessoa Jurídica',font=('Arial',24,'bold'), text_color='white').place(x=390,y=0)

    label_nome = ctk.CTkLabel(novaJanela,text='Nome: ', font=('Arial',12), text_color='white')
    label_nome.place(x=10,y=20)
    
    e_nome = ctk.CTkEntry( novaJanela,placeholder_text='Nome Completo')
    e_nome.place(x= 75,y=20)

    label_email = ctk.CTkLabel(novaJanela, text='E-mail: ', font=('Arial',12), text_color='white')
    label_email.place(x =10, y = 55)
    
    e_email = ctk.CTkEntry(novaJanela)
    e_email.place(x = 75, y = 55)

    label_cnpj=ctk.CTkLabel(novaJanela, text='CNPJ: ', font=('Arial',12), text_color='white')
    label_cnpj.place(x=10,y=90)
    
    e_cnpj=ctk.CTkEntry(novaJanela)
    e_cnpj.place(x = 75, y=90 )

    label_senha=ctk.CTkLabel(novaJanela,text='Senha: ',font=('Arial',12), text_color='white')
    label_senha.place(x=10,y=125)
    
    e_senha = ctk.CTkEntry(novaJanela, show = '*')
    e_senha.place(x = 75, y = 125)

    label_telefone=ctk.CTkLabel(novaJanela,text='Telefone: ',font=('Arial',12), text_color='white').place(x=11,y=160)
    e_telefone = ctk.CTkEntry(novaJanela)
    e_telefone.place(x=75,y=160)

    label_endereco=ctk.CTkLabel(novaJanela,text='Endereço: ',font=('Arial',12), text_color='white')
    label_endereco.place(x=10,y=195)
    
    e_endereco = ctk.CTkEntry(novaJanela)
    e_endereco.place(x=75,y=195)

    label_doacao=ctk.CTkLabel(novaJanela, text='Doação: ', font=('Arial',12), text_color='white')
    label_doacao.place(x=10,y=230)
    
    e_doacao = ctk.CTkEntry(novaJanela)
    e_doacao.place(x=75,y=230)
  
    label_qtd=ctk.CTkLabel(novaJanela,text='Quantidade: ',font=('Arial',12), text_color='white')
    label_qtd.place(x=10,y=265)
    
    e_qtd=ctk.CTkEntry(novaJanela)
    e_qtd.place(x=75,y=265)

#Alterar Doador Pessoa Jurídica
    def modificar_doador_pessoaPJ():
        cnpj=e_cnpj.get()
        nome=e_nome.get()
        senha=e_senha.get()
        telefone=e_telefone.get()
        endereco=e_endereco.get()
        email=e_email.get()
        doacao=e_doacao.get()
        qtd=e_qtd.get()

        if(cnpj ==''):
            MessageBox.showinfo('Status inserido','É necessário preencher o CNPJ para alterar o cadastro.')
        else:
            con=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='casadoleo')
            cursor = con.cursor()
            cursor.execute('UPDATE doador_empresa set nome=%s, senha=%s,telefone=%s,endereco=%s,email=%s,doacao=%s,qtd=%s where cnpj=%s',(nome,senha,telefone,endereco,email,doacao,qtd,cnpj))
            con.commit()
            MessageBox.showinfo('Status inserido','Alteração realizada com sucesso!')
            con.close()
            
    botao = ctk.CTkButton(novaJanela, text = 'Alterar', height=20, width=40, border_spacing=4, border_width=2, fg_color='white', text_color='black', command = modificar_doador_pessoaPJ)
    botao.place(x=10,y=320)


btDoadorPF=ctk.CTkButton(window,text='Cadastrar Doador - Pessoa Física', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaDoadorPF)
btDoadorPF.place(x=300, y=26)

btExcluirPF=ctk.CTkButton(window,text='Excluir Doador - Pessoa Física', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaExcluirPF)
btExcluirPF.place(x=300, y=56)

btConsultarPF=ctk.CTkButton(window,text='Consultar Doador - Pessoa Física', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaConsultarPF)
btConsultarPF.place(x=300, y=86)

btAlterarPF=ctk.CTkButton(window,text='Alterar Doador - Pessoa Física', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=alterar_doador_pessoaPF)
btAlterarPF.place(x=300, y=116)




btDoadorPJ=ctk.CTkButton(window,text='Cadastrar Doador - Pessoa Jurídica', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaDoadorPJ)
btDoadorPJ.place(x=300, y=166)

btExcluirPJ=ctk.CTkButton(window,text='Excluir Doador - Pessoa Jurídica', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaExcluirPJ)
btExcluirPJ.place(x=300, y=196)

btConsultarPJ=ctk.CTkButton(window,text='Consultar Doador - Pessoa Jurídica', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaConsultarPJ)
btConsultarPJ.place(x=300, y=226)

btAlterarPJ=ctk.CTkButton(window,text='Alterar Doador - Pessoa Jurídica', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=alterar_doador_pessoaPJ)
btAlterarPJ.place(x=300, y=256)






btVoluntario=ctk.CTkButton(window,text='Cadastrar Voluntário', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaVoluntario)
btVoluntario.place(x=300, y=306)

btExcluirVoluntario=ctk.CTkButton(window,text='Excluir Voluntario', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaExcluirVoluntario)
btExcluirVoluntario.place(x=300, y=336)

btConsultarVoluntario=ctk.CTkButton(window,text='Consultar Voluntario', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=janelaConsultarVoluntario)
btConsultarVoluntario.place(x=300, y=366)

btAlterarVoluntario=ctk.CTkButton(window,text='Alterar Voluntário', height=20, width=240, border_spacing=4, fg_color='white', text_color='black', command=alterar_voluntario)
btAlterarVoluntario.place(x=300, y=396)


 
window.mainloop()
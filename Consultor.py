#conding: utf-8

#/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

import sys, json
import requests
from bs4 import BeautifulSoup
import base64
from Tkinter import *
import os
from time import sleep

header = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/10100101 Firefox/43.0 Iceweasel/43.0.4'}


def testar():
	loginn = ed1.get()
	password = ed2.get()
	if loginn and password == "adriel":
		print("[Logado!]\n")
		login.destroy()
		def Consultar():
			cpf = edi2.get()
			cnpj = edi1.get()
			if cpf:
				os.system('cls')
				url = 'aHR0cHM6Ly9jb25zdWx0YXJjcGYuZ3JhdGlzL21vYmlsZS9yZS5waHA/Y3BmPXswfSZjb25zdWx0YXI9T0s='
				enc = base64.b64decode(url)
				req = requests.get(enc.format(cpf), headers=header)
				code = req.status_code
				html = req.text
				if code == 200:
					bs = BeautifulSoup(html, 'lxml')
					proc = bs.find_all('strong')
					for procs in proc:
						print(procs.get_text())
						arq = open('dados.txt', 'w')
						try:
							arq.write(procs)
						except:
							pass
					arq.close()

			elif cnpj:
				os.system('cls')
				url = 'aHR0cHM6Ly93d3cucmVjZWl0YXdzLmNvbS5ici92MS9jbnBqL3swfQ=='
				enc = base64.b64decode(url)
				req = requests.get(enc.format(cnpj), headers=header)
				code = req.status_code
				if code == 200:
					html = req.text
					receita = json.loads(html)
					arq = open('dados.txt', 'w')
					try:
						arq.write(procs)
					except:
						pass
					print("\n\n")
					print("Atividade Principal: %s"%receita['atividade_principal'][0]['text'])
					print("Nome: %s"%receita['nome'])
					print("Complemento: %s"%receita['complemento'])
					print("UF: %s"%receita['uf'])
					print("Telefone: %s"%receita['telefone'])
					print("Email: %s"%receita['email'])
					print("(QSA) Nome: %s"%receita['qsa'][0]['nome'])
					print("(QSA) Nome: %s"%receita['qsa'][1]['nome'])
					print("Situacao: %s"%receita['situacao'])
					print("Bairro: %s"%receita['bairro'])
					print("Numero: %s"%receita['numero'])
					print("CEP: %s"%receita['cep'])
					print("Municipio: %s"%receita['municipio'])
					print("CNPJ: %s"%receita['cnpj'])
					print("Status: %s"%receita['status'])
				arq.close()

			else:
				adriellb = Label(window, text="Insira um CPF ou CNPJ valido!", fg="green", bg="black")
				adriellb.pack(side=TOP)
				adriellb.place(x=50, y=30)

		window = Tk()

		window.title('= Consultor by AdrielFreud =')


		lb = Label(window, text="Consultor CPF", fg="green", bg='black')
		lb.place(x=75, y=90)

		l2 = Label(window, text="Consultor CNPJ", fg="green", bg='black')
		l2.place(x=75, y=150)

		bt1 = Button(window, width=20, text="Consultar", command=Consultar, fg="Green", bg='black')
		bt1.place(x=75, y=220)

		#cnpj
		edi1 = Entry(window, width=24)
		edi1.place(x=75, y=180)

		#cpf
		edi2 = Entry(window, width=24)
		edi2.place(x=75, y=120)


		bot2 = Button(window, width=20, text="Sair!", command=sair, fg="Green", bg='black')
		bot2.place(x=75, y=250)

		adriellb = Label(window, text="==== Creditos Adriel Freud, Oto NK ====", fg="green", bg="black")
		adriellb.pack(side=TOP)
		adriellb.place(x=40, y=30)

		window['bg'] = 'black'
		window.geometry("300x300+200+200")

		window.mainloop()
	else:
		print("[!] login ou Password Invalidos, Tente Novamente!\n")


def sair():
	sys.exit()
	exit()


login = Tk()
login.title('Login Consultor - Freud')
login['bg'] = "black"

label1 = Label(login, text="Login: ", bg="black", fg="green")
label1.place(x=5, y=30)

label2 = Label(login, text="Senha: ", bg="black", fg="green")
label2.place(x=5, y=60)

ed1 = Entry(login)
ed1.place(x=60, y=30)
ed2 = Entry(login)
ed2.place(x=60, y=60)

bt1 = Button(login, text="Confirmar", bg="black", fg="green", command=testar, width=20)
bt1.place(x=60, y=100)
bt2 = Button(login, text="Sair", bg="black", fg="green", command=sair, width=20)
bt2.place(x=60, y=130)

cred = Label(login, text="Facebook: https://www.facebook.com/xrn401", fg="green", bg="black")
cred.place(x=10, y=170)

#label1.grid(row=0, column=0)
#label2.grid(row=1, column=0)
#ed1.grid(row=0, column=1)
#ed2.grid(row=1, column=1)
#bt1.grid(row=2, column=1)
#bt2.grid(row=3, column=1)

login.geometry("270x200+100+100")
login.mainloop()

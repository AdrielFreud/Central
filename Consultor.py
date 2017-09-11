#conding: utf-8

#/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

#conding: utf-8
import tempfile
import sys, json
import requests
from bs4 import BeautifulSoup
import base64
from Tkinter import *
import os
from time import sleep

header = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/10100101 Firefox/43.0 Iceweasel/43.0.4'}

def CleanTemp():
	temporario = tempfile.gettempdir()
	print("\n[!] Limpando arquivos temporario!\n")
	os.system('del %s /S /Q'%temporario)
	os.chdir('C:\\Windows\\Temp')
	os.system('del * /S /Q')
	os.chdir('C:\\Windows\\Prefetch')
	os.system('del * /S /Q')
	os.chdir('C:\\Windows\\SoftwareDistribution\\Download')
	os.system('del * /S /Q')
	os.chdir('C:\\Temp')
	os.system('del * /S /Q')
	os.system('cd %TEMP%')
	os.system('del * /S /Q')
	print("")
	print("\n[+] Diretorios Limpado com sucesso!")


def binchecker():
	def check():
		os.system('cls')
		biin = entrybin.get()
		url = "https://lookup.binlist.net/{0}".format(biin)
		req = requests.get(url, headers=header)
		code = req.status_code
		html = req.text
		if code == 200:
			jsbin = json.loads(html)
			print("\nNumber: \n")
			print("Lenght: %s"%jsbin['number']['length'])
			print("Prefix%s"%jsbin['number']['prefix'])
			print("Type: %s"%jsbin['type'])
			print("Brand: %s"%jsbin['brand'])
			print("Prepaid: %s"%jsbin['prepaid'])
			print("Bank Name: %s"%jsbin['bank']['name'])
			print("Bank Logo: %s"%jsbin['bank']['logo'])
			try:
				print("Bank City: %s"%jsbin['bank']['city'])
			except:
				pass
			print("Bank Phone: %s"%jsbin['bank']['phone'])
			print("Contry alpha: %s"%jsbin['country']['alpha2'])
			print("Contry Name: %s"%jsbin['country']['name'])
			print("Contry Numeric: %s"%jsbin['country']['numeric'])
		else:
			print("[!] Error ao requisitar!\n")

	menu.destroy()

	binnn = Tk()
	binnn.title('Bin Checker')
	binnn['bg'] = 'black'

	labelbin = Label(binnn, text="Insira a Bin", fg="green", bg='black')
	labelbin.place(x=30, y=100)

	entrybin = Entry(binnn, width=20)
	entrybin.place(x=75, y=130)


	checkbt = Button(binnn, width=20, text="Checkar!", command=check, fg="Green", bg='black')
	checkbt.place(x=75, y=160)

	exitbin = Button(binnn, width=20, text="Sair!", command=sair, fg="green", bg='black')
	exitbin.place(x=75, y=190)

	binnn.geometry("300x300+200+200")
	binnn.mainloop()


def main():
	global menu
	menu = Tk()
	menu.title("Menu")
	info = Label(menu, text="- Central feita por Adriel Freud - ")
	info.pack(side=TOP)

	con = Button(menu, text="Consultor", command=Consultar, bg="black", fg="green", width=20)
	con.place(x=75, y=60)
			
	bincheck = Button(menu, text="Validar Bin", command=binchecker, bg="black", fg="green", width=20)
	bincheck.place(x=75, y=100)

	clean = Button(menu, text="Limpar Arquivos Temp.", command=CleanTemp, bg="black", fg="green", width=20)
	clean.place(x=75, y=130)

	exitt = Button(menu, text="Sair!", command=sair, bg="black", fg="green", width=20)
	exitt.place(x=75, y=160)

	menu['bg'] = 'black'
	menu.geometry("300x300+200+200")
	menu.mainloop()

def Consultar():
	def requisitar():
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

		elif cnpj:
			os.system('cls')
			url = 'aHR0cHM6Ly93d3cucmVjZWl0YXdzLmNvbS5ici92MS9jbnBqL3swfQ=='
			enc = base64.b64decode(url)
			req = requests.get(enc.format(cnpj), headers=header)
			code = req.status_code
			if code == 200:
				html = req.text
				receita = json.loads(html)
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

		else:
			adriellb = Label(window, text="Insira um CPF ou CNPJ valido!", fg="green", bg="black")
			adriellb.pack(side=TOP)
			adriellb.place(x=50, y=30)

	menu.destroy()
	global window
	window = Tk()
	window.title('= Central by AdrielFreud =')

	lb = Label(window, text="Consultor CPF", fg="green", bg='black')
	lb.place(x=75, y=90)

	l2 = Label(window, text="Consultor CNPJ", fg="green", bg='black')
	l2.place(x=75, y=150)

	bt1 = Button(window, width=20, text="Consultar", command=requisitar, fg="Green", bg='black')
	bt1.place(x=75, y=220)

	#cnpj
	edi1 = Entry(window, width=24)
	edi1.place(x=75, y=180)

	#cpf
	edi2 = Entry(window, width=24)
	edi2.place(x=75, y=120)

	bot2 = Button(window, width=20, text="Sair!", command=sair, fg="Green", bg='black')
	bot2.place(x=75, y=250)

	adriellb = Label(window, text="==== Creditos Adriel Freud ====", fg="green", bg="black")
	adriellb.pack(side=TOP)
	adriellb.place(x=40, y=30)

	window['bg'] = 'black'
	window.geometry("300x300+200+200")

	window.mainloop()

def testar():
	loginn = ed1.get()
	password = ed2.get()
	passwd = base64.b64decode("YWRyaWVs")
	if (loginn and password == passwd):
		print("[Logado com Sucesso!]\n")
		arq = open('conf.deb', 'w')
		arq.close()
		login.destroy()
		main()

	else:
		print("[!] login ou Password Invalidos, Tente Novamente!\n")

def sair():
	sys.exit()
	exit()

def logar():
	global login
	login = Tk()
	login.title('Login Central - Freud')
	login['bg'] = "black"

	label1 = Label(login, text="Login: ", bg="black", fg="green")
	label1.place(x=5, y=30)

	label2 = Label(login, text="Senha: ", bg="black", fg="green")
	label2.place(x=5, y=60)

	global ed1
	global ed2
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

if (os.path.exists('conf.deb') == True):
	main()
else:
	logar()

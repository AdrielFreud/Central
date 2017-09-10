#conding: utf-8
import sys, json
import requests
from bs4 import BeautifulSoup
import base64
from Tkinter import *
import os

header = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/10100101 Firefox/43.0 Iceweasel/43.0.4'}


def Consultar():
	cpf = ed2.get()
	cnpj = ed1.get()

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
		enc = url.format(cnpj)
		req = requests.get(enc, headers=header)
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

def sair():
	sys.exit()
	exit()

window.title('= Consultor by AdrielFreud =')


lb = Label(window, text="Consultor CPF", fg="green", bg='black')
lb.place(x=75, y=90)

l2 = Label(window, text="Consultor CNPJ", fg="green", bg='black')
l2.place(x=75, y=150)

bt1 = Button(window, width=20, text="Consultar", command=Consultar, fg="Green", bg='black')
bt1.place(x=75, y=220)

#cnpj
ed1 = Entry(window, width=24)
ed1.place(x=75, y=180)

#cpf
ed2 = Entry(window, width=24)
ed2.place(x=75, y=120)


bt2 = Button(window, width=20, text="Sair!", command=sair, fg="Green", bg='black')
bt2.place(x=75, y=250)

adriellb = Label(window, text="==== Creditos Adriel Freud, Oto NK ====", fg="green", bg="black")
adriellb.pack(side=TOP)
adriellb.place(x=40, y=30)

window['bg'] = 'black'
window.geometry("300x300+200+200")

window.mainloop()

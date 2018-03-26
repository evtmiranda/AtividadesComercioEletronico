# views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "index.html")
	
def login(request):
	if request.method == "GET":
		print ("Acesso via GET")
		return render(request, "login.html")
	else:
		print("Acesso via POST")
		senha = request.POST.get("senha")
		if senha == "teste123":
			usuario = request.POST.get("usuario")
			print("Usuario ", usuario, " entrou com sucesso")
			return render(request, "index.html")
		else:
			print("Usuario digitou a senha errada")
		return render(request, "login.html")
		
def contato(request):
	if request.method == "GET":
		return render(request, "contato.html")
	else:
		nome = request.POST.get("nome")
		telefone = request.POST.get("telefone")
		print("Nome: ", nome, ". Telefone: ", telefone)
	return render(request, "index.html")
	


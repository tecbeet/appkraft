from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from decimal import Decimal

lista = []
produto = []
# Create your views here.
def home(request):
    global lista
    global produto
    """
    O Django segue o padrão MVC muito de perto, mas usa uma terminologia ligeiramente dierente. O django é 
    essencialmente um framework MTV(Model-Template-View). Usa o termo Templates para Views e Views para
    Controller. Em outras palavras, nas views do Django são chamados templates e controllers e são chamados 
    views. O código HTML estará em modelos e o código Python etará em Views e Models. 
    """
    # method GET
    search = request.GET.get('search')
    quantidade = request.GET.get('qnt')
    venda = request.GET.get('vnd')
        # get id produto
    if search:
        venda = int(venda)
        # try:
        vendas = Compra_Id.objects.get(pk=venda, status='Andamento')
        if vendas:
            produtos = Produtos.objects.filter(
                Q(codigo_produto=search) |
                Q(codigo_barras=search)
            )
            
            for p in produtos:
                quantidade = int(quantidade)
                if quantidade:
                    p.valor *= quantidade
                else:
                    quantidade = 1

                query = Compras.objects.create(
                    codigo_compra = vendas,
                    codigo_produto = p.codigo_produto,
                    nome = p.nome,
                    valor = p.valor,
                    quantidade = quantidade,
                ).save()

            return redirect('/', {'venda':vendas.pk})

        # except:
        #     pass

        
       
        
        

    compras = Compras.objects.all()

        # lista = [{'codigo':item['codigo_produto'], 'nome':item['nome'], 'valor':item['valor']}
        #     for item in produtos
        # ]
        
        # lista = [
        #     produto.append(produto_serializer(item))
        #     for item in produtos
        # ]
        
        # for l in lista:
        #     produto.append(l)



    

        # retornar persitencia do produto

        # adicionar em lista

    # method POST
        # retornar Total
        
        # persistir compra


    context = {'lista':compras, 'venda':venda}
    return render(request, 'appkraft/home.html', context)


def produto_serializer(item):
    return {'codigo':item['codigo_produto'], 'nome':item['nome'], 'valor':item['valor']}


def produtos(request):

    produtos = Produtos.objects.all()

    context = {'produtos':produtos}
    return render(request, 'appkraft/produtos.html', context)
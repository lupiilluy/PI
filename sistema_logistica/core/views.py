from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # <--- ESSA LINHA É A SOLUÇÃO
from django.http import HttpResponseForbidden
from .models import Entrega
from .forms import EntregaForm


@login_required
def lista_entregas(request):
    entregas = Entrega.objects.all()
    return render(request, 'core/lista_entregas.html', {'entregas': entregas})

@login_required
def editar_entrega(request, id):
    # Tenta pegar a entrega pelo ID, ou dá erro 404 se não existir
    entrega = get_object_or_404(Entrega, id=id)

    # SEGURANÇA: Verifica se o motorista é dono dessa rota
    # Se não for superuser E a entrega não for da rota dele -> PROIBIDO
    if not request.user.is_superuser:
        if not hasattr(request.user, 'motorista') or entrega.rota.motorista != request.user.motorista:
            return HttpResponseForbidden("Você não tem permissão para editar esta entrega.")

    # Processamento do Formulário
    if request.method == 'POST':
        form = EntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            return redirect('home') # Volta para a lista depois de salvar
    else:
        form = EntregaForm(instance=entrega) # Carrega os dados atuais

    return render(request, 'core/form_entrega.html', {'form': form, 'entrega': entrega})

def rastreamento(request):
    # Pega o código digitado na URL (ex: ?codigo=CX-01)
    codigo = request.GET.get('codigo')
    entrega = None
    
    if codigo:
        # Tenta achar a entrega (usa .first() para não dar erro se não achar)
        entrega = Entrega.objects.filter(codigo_rastreio=codigo).first()
    
    return render(request, 'core/rastreamento.html', {'entrega': entrega, 'codigo': codigo})
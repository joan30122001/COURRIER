from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from senat.forms import *
from datetime import datetime
import random
from .models import Courrier
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
# from urlparams.redirect import param_redirect
from django.template.response import TemplateResponse
import json
from django.db.models import Q # new
from django.views.generic import ListView






def chef_service(request):

    form = RegistrationForm(request.POST or None)
    chef_service = Courrier()

    if request.method == 'POST':
        # if code_unique:
        #     form = CiviliteForm(request.POST or None, instance=etudiant)
        #     if form.is_valid():
        #         form.save()
        #         messages.add_message(request, messages.SUCCESS, _(f"Informations de civilité modifiées avec succès."))
        #         return redirect('logement:filiation')
        #     else:
        #         messages.add_message(request, messages.ERROR, _('Veuillez vérifier les champs en rouge !!!'))
        #         return render(request, 'logement/civilite.html', {'form': form})
        # else:
        #     form = CiviliteForm(request.POST or None)
        #     etudiant = DemandeChambre()

        # form = RegistrationForm(request.POST or None)
        # chef_service = Courrier()

        if form.is_valid():
            # code_unique = generate_unique_code(str(form.cleaned_data['date_nais']))

            # etudiant.num_ordre = code_unique

            chef_service.transmetteur = form.cleaned_data['transmetteur']                
            chef_service.recepteur = form.cleaned_data['recepteur']                
            chef_service.code = form.cleaned_data['code']                
            chef_service.date = form.cleaned_data['date']                
            chef_service.objet = form.cleaned_data['objet']
            chef_service.structure = form.cleaned_data['structure']                
            chef_service.annee = form.cleaned_data['annee']
            chef_service.types = form.cleaned_data['types']
        
            chef_service.save()
            # request.session['code_logement'] = code_unique

            messages.add_message(request, messages.SUCCESS, (f"Informations du courrier enregistrées avec succès."))
            # return redirect('logement:filiation', request.session['ecole_code'] )
            return redirect('senat:chef_service')
        else:
            messages.add_message(request, messages.ERROR, ('Veuillez vérifier les champs en rouge !!!'))
            return render(request, 'chef_service.html', {'form': form})

    context = {
        'form': form,
    }
    return render(request,'chef_service.html', context)



def chef_depart(request):
    return render(request,'chef_depart.html')



def chef_arrive(request):
    return render(request,'chef_arrive.html')



def bureau_sg(request):
    
    # # code = request.session['code']
    # sg = get_object_or_404(Courrier)
    # form = MentionForm(instance=sg)

    # if request.method == 'POST':
    #     form = MentionForm(request.POST or None, instance=sg)
    #     if form.is_valid():
    #         # code_unique = generate_unique_code(str(form.cleaned_data['date_nais']))

    #         # etudiant.num_ordre = code_unique

    #         # sg.mention = form.cleaned_data['mention']                
    #         # sg.service_traitement = form.cleaned_data['service_traitement']  
        
    #         form.save()
    #         # request.session['code_logement'] = code_unique

    #         messages.add_message(request, messages.SUCCESS, (f"Informations du courrier enregistrées avec succès."))
    #         # return redirect('logement:filiation', request.session['ecole_code'] )
    #         return redirect('senat:chef_depart')
    #     else:
    #         messages.add_message(request, messages.ERROR, ('Veuillez vérifier les champs en rouge !!!'))
    #         return render(request, 'sg.html', {'form': form})

    # context = {
    #     'form': form,
    # }
    # return render(request,'sg.html', context)
    # code = DossierUniv.objects.get(code=code)
    # context = {
    #     'code': code,
    # }
    return render(request,'sg.html')

    # sg = get_object_or_404(Courrier, id=id)
    # if request.method == 'POST':
    #     if request.POST.get('service_traitement') and request.POST.get('mention'):
    #         Courrier.objects.filter(id = id).update(
    #             service_traitement= request.POST.get('service_traitement'), 
    #             mention= request.POST.get('mention'))
    #         messages.success(request, "Les informations du courrier ont été complétées.")

    #     context={'sg': sg}
    #     return render(request, 'sg.html')  
    # else:
    #     context={'sg': sg,
	# 	'error': "Les informations du courrier n'ont pas été complétées."}
    #     return render(request,'sg.html', context)




def usager(request):
    return render(request,'usager.html')



def search(request):
    
#     # clear_session(request)

#     # context = {}

#     # if request.method == 'POST':
#     #     code = request.POST['code']

#     #     if isinstance(code, str):
#     #         return redirect('senat:sg', code)
#     #     else:
#     #         messages.add_message(request, messages.ERROR, ('Mauvais format de code !!!'))
#     #         return render(request, 'search.html', {'code': code})

#     # return render(request, 'search.html', context)

#     # if request.method == 'GET':
#     #     query = request.GET.get('code')
#     #     if query:
#     #         courrier = Courrier.objects.filter(code__icontains=query) 
#     #         return render(request, 'sg.html', {'courrier':courrier})
#     #     else:
#     #         # messages.add_message(request, messages.ERROR, ('Mauvais format de code !!!'))
#     #         return render(request, 'search.html', {})

#     # if request.method == 'GET':
#     #     query = request.GET.get('code')
#     #     querys = request.GET.get('types')
#     #     if query:
#     #         courrier = Courrier.objects.raw('select * from courrier where code="'+query+'" and types="'+querys+'"') 
#     #         return render(request, 'sg.html', {'courrier':courrier})
#     #     else:
#     #         # messages.add_message(request, messages.ERROR, ('Mauvais format de code !!!'))
#     #         return render(request, 'search.html', {})

    if request.method == 'POST':
        query = request.POST.get('code')
        querys = request.POST.get('types')
        courrier = Courrier.objects.raw('select * from courrier where code="'+query+'" and types="'+querys+'"') 

        # return redirect('senat:bureau_sg', kwargs={'courrier':courrier})
        return render(request, 'sg.html', {'courrier':courrier})
        # return redirect(f'senat:bureau_sg/?query={query}/?querys={querys}')
        # return redirect('senat:bureau_sg')
    else:
        # messages.add_message(request, messages.ERROR, ('Mauvais format de code !!!'))
        return render(request, 'search.html')



# class SearchResultsList(ListView):
#     model = Courrier
#     template_name = "search.html"
#     context_object_name = "courrier"

#     def search(self):  # new
#         # if request.method == 'POST':
#         query = self.request.POST.get('code')
#         querys = self.request.POST.get('types')
#         courrier = Courrier.objects.filter(
#             Q(code__icontains=query) and Q(types__icontains=querys)
#         )
#         # courrier = Courrier.objects.raw('select * from courrier where code="'+query+'" and types="'+querys+'"') 
#         return courrier
#         # else:
#         #     # messages.add_message(request, messages.ERROR, ('Mauvais format de code !!!'))
#         #     return render(request, 'search.html')


# class SearchResultsList(ListView):
#     model = Courrier
#     context_object_name = "courrier"
#     template_name = "search.html"

#     def search(self):
#         # query = self.request.GET.get("q")
#         query = self.request.POST.get("code")
#         querys = self.request.POST.get("types")

#         return Courrier.objects.raw('select * from courrier where code="'+query+'" and types="'+querys+'"'
#         )
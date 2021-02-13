from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import NameForm
from .models import BankStatement, BankTransaction, Category, Expression


def statements(request):
    statements_list = BankStatement.objects.all()
    context = {'statements_list': statements_list}
    return render(request, 'finances/statements.html', context)


def transactions(request, statement_id):
    statement = get_object_or_404(BankStatement, pk=statement_id)
    transaction_list = BankTransaction.objects.filter(statement=statement)
    context = {'transaction_list': transaction_list, 'statement_name': statement}
    return render(request, 'finances/bank.html', context)


def categories(request):
    categories_list = Category.objects.all()
    context = {}
    form = None
    if request.method == 'GET':
        form = NameForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    context = {'categories_list': categories_list, 'form': form}
    return render(request, 'finances/categories.html', context)

def expressions(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    expressions_list = Expression.objects.filter(category=category)
    context = {'expressions_list': expressions_list, 'category': category}
    return render(request, 'finances/expressions.html', context)


def bills_by_category(request, statement_id, category_id):
    category = get_object_or_404(Category, pk=category_id)
    statement = get_object_or_404(BankStatement, pk=statement_id)
    expressions_list = Expression.objects.filter(category=category)
    total_amounts = {}
    for expression in expressions_list:
        transactions = BankTransaction.objects.filter(statement=statement)
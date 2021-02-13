from django.contrib import admin

from .models import BankStatement, BankTransaction, Category, Expression, StatementType


class ExprInline(admin.StackedInline):
    model = Expression
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = [
        (None,          {'fields': ['name']})
    ]
    inlines = [ExprInline]


class TransactionsInline(admin.StackedInline):
    model = BankTransaction
    extra = 4


class StatementInline(admin.StackedInline):
    model = BankStatement
    extra = 4

@admin.register(StatementType)
class StatementTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(BankStatement)
class StatementAdmin(admin.ModelAdmin):
    pass

@admin.register(BankTransaction)
class TransactionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

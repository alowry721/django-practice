from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Expression(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    regex = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StatementType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class BankStatement(models.Model):
    month = models.CharField(max_length=15)
    year = models.CharField(max_length=10)
    statement_type = models.ForeignKey(StatementType, on_delete=models.CASCADE)

    def __str__(self):
        return "{}/{} - {}".format(self.year, self.month, self.statement_type)


class BankTransaction(models.Model):
    trans_date = models.DateField('transaction date', blank=True)
    description = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    expression = models.ForeignKey(Expression, on_delete=models.CASCADE)
    statement = models.ForeignKey(BankStatement, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} ${}".format(self.trans_date, self.description, self.amount)

"""
The method at the bottom takes the above info and populates the database tables for categories and expressions.

Keeping this file around until there's a better way to add data to tables
"""
import os

from mysite import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from finances.models import Category, Expression
from collections import namedtuple

ExpressionTuple = namedtuple("ExpressionTuple", ["regex", "name"])


NETFLIX  = ExpressionTuple(regex="NETFLIX.COM ADAM LOWRY", name="Netflix")
DAN_LEWIS  = ExpressionTuple(regex="TRANSFER TO LEWIS DAN", name="Rent")
BRIDGECREST  = ExpressionTuple(regex="Bridgecrest DT RETAIL", name="Car")
APPLE  = ExpressionTuple(regex="APPLE.COM BILL", name="Apple Subscription")
WIKIPEDIA  = ExpressionTuple(regex="WIKIPEDIA", name="Wikipedia")
SAVINGS  = ExpressionTuple(regex="RECURRING TRANSFER TO LOWRY A SAVINGS", name="Savings")
ATXHS  = ExpressionTuple(regex="ATX HACKERSPACE ATXHS.ORG", name="ATXHS")
ATM_WITHDRAWAL  = ExpressionTuple(regex="ATM WITHDRAWAL", name="ATM Withdrawal")
SPOTIFY  = ExpressionTuple(regex="Spotify USA", name="Spotify")
GRANDE  = ExpressionTuple(regex="GRANDE COMMUNICATI", name="Internet")
TREND_PAYMENT  = ExpressionTuple(regex="TREND MICRO DIRECT DEP", name="Work Deposit")
SOUTHWEST  = ExpressionTuple(regex="SOUTHWEST ADAM LOWRY", name="Southwest Airlines")
LYFT  = ExpressionTuple(regex="LYFT RIDE", name="Lyft")
ZIPCAR  = ExpressionTuple(regex="ZIPCAR INC", name="Zipcar")
HBO_NOW  = ExpressionTuple(regex="HBO NOW", name="HBO Now")
NAVIENT_ED  = ExpressionTuple(regex="NAVI ED SERV", name="Student Loans")
NAVIENT_DEBIT  = ExpressionTuple(regex="NAVIENT NAVI DEBIT", name="Student Loans")
TEXAS_GAS  = ExpressionTuple(regex="TEXAS GAS", name="Texas Gas")
TEXAS_GAS_FEE  = ExpressionTuple(regex="UTL\*SERVICE FE", name="Texas Gas")
NYT  = ExpressionTuple(regex="NEW YORK TIMES DIG", name="NY Times")
CHS_CARD  = ExpressionTuple(regex="CHASE CREDIT CRD AUTOPAY", name="Chase CC")
HCRON  = ExpressionTuple(regex="HOUSTON CHRONICLE", name="Houston Chronicle")
SPRINT  = ExpressionTuple(regex="SPRINT8006396111 ACHBILLPAY", name="Spring")
VENMO  = ExpressionTuple(regex="VENMO CASHOUT", name="Venmo")
AA_STATESMEN  = ExpressionTuple(regex="AUSTIN AMER STATES 800-4459898", name="Austin American Statesmen")
OKC  = ExpressionTuple(regex="OKCUPID.COM", name="OKCupid")
RETURN_ITEM_FEE  = ExpressionTuple(regex="NSF RETURN ITEM FEE", name="Return Item Fee")
CREDIT_CARD  = ExpressionTuple(regex="WF Credit Card", name="CC Payment")
TX_PIRG  = ExpressionTuple(regex="TEXPIRG 8008386554", name="TxPirg")

INTEREST = ExpressionTuple(regex="INTEREST CHARGE", name="Interest")
AMZN_MKTPL = ExpressionTuple(regex="AMZN Mktp", name="Amazon Marketplace")
AMZN_DIGITAL = ExpressionTuple(regex="AMZN Digital", name="Amazon Marketplace")
AMZN = ExpressionTuple(regex="AMZNAMZN", name="Amazon")
HEB = ExpressionTuple(regex="H\-E\-B", name="H-E-B")
GAL = ExpressionTuple(regex="GENERATOR ATHLETE LAB", name="Generator Athlete Lab")
WHOLE_FOODS = ExpressionTuple(regex="WHOLEFDS", name="Whole Foods")
AMZN_PRIME = ExpressionTuple(regex="Amazon Prime", name= "Amazon")
CHIPOTLE = ExpressionTuple(regex="CHIPOTLE", name="Chipotle")
AUTO_PAYMNT = ExpressionTuple(regex="AUTOMATIC PAYMENT", name="Automatic Payment")
WALGREENS = ExpressionTuple(regex="WALGREENS", name="Walgreens")
TRADER_JOES = ExpressionTuple(regex="TRADER JOE", name="Trader Joe's")
CENTRAL_MARKET = ExpressionTuple(regex="CENTRAL MARKET", name="Central Market")
TACOS = ExpressionTuple(regex="TACO", name="Tacos")

GAS = [TEXAS_GAS, TEXAS_GAS_FEE]
HOUSE_BILLS = [GRANDE, DAN_LEWIS] + GAS
SUBSCRIPTIONS = [NETFLIX, AA_STATESMEN, SPOTIFY, HBO_NOW, APPLE, NYT, OKC]
NON_PROFIT = [WIKIPEDIA, TX_PIRG]
STUDENT_LOANS = [NAVIENT_ED, NAVIENT_DEBIT]
DEBT = [BRIDGECREST, CREDIT_CARD, CHS_CARD] + STUDENT_LOANS
TRANSFERS = [SAVINGS]
DEPOSITS = [VENMO, TREND_PAYMENT]
FEES = []

GROCERIES = [HEB, WHOLE_FOODS, TRADER_JOES, CENTRAL_MARKET]
FOOD = [CHIPOTLE, TACOS]
FITNESS = [GAL]
AMAZON = [AMZN_MKTPL, AMZN, AMZN_PRIME]

CATEGORIES = {"House Bills": HOUSE_BILLS, "Subscriptions": SUBSCRIPTIONS, "Causes/Non-Profits": NON_PROFIT, "Debts": DEBT,
              "Transfers": TRANSFERS, "Deposits": DEPOSITS, "Fees": FEES, "Groceries": GROCERIES, "Food": FOOD, "Fitness": FITNESS,
              "Amazon": AMAZON}
def add_categories():
    for name, expressions in CATEGORIES.items():
        c = Category(name=name)
        c.save()
        for expression in expressions:
            e = ExpressionTuple(category=c, name=expression.name, regex=expression.regex)
            e.save()
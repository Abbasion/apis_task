from app.models import Stock, InsiderTransaction, Valuation


def get_stock(symbol):
    try:
        cons = Stock.objects.get(symbol=symbol)
        return cons
    except:
        return None

def get_stock_by_Id(Id):
    try:
        cons = Stock.objects.filter().order_by("-symbol")[:10:-1]
        return cons
    except:
        return None

def get_insider_transaction(Id):
    try:
        list = InsiderTransaction.objects.select_related("symbol").filter().order_by("-symbol")[:10:-1]
        return list
    except:
        return None

def getValuation(Id):
    try:
        list = Valuation.objects.select_related("symbol").filter().order_by("-symbol")[:10:-1]
        return list
    except:
        return None
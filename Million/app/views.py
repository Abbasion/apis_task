from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from app.helper import get_stock, get_stock_by_Id, get_insider_transaction, getValuation
from app.models import Stock,InsiderTransaction


# Create your views here.
class StockListUpdate(ListCreateAPIView):
    # def get(self, request, *args, **kwargs):
    #     try:
    #         data = []
    #         stock = get_stock()
    #         if (stock is None):
    #             return JsonResponse({"data": "No record found", "status": status.HTTP_404_NOT_FOUND},
    #                                 status=status.HTTP_404_NOT_FOUND)
    #         else:
    #             for cons in stock:
    #                 con_data = model_to_dict(cons)
    #                 data.append(con_data)
    #
    #             return JsonResponse({"data": data, "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
    #     except Exception as ex:
    #         return JsonResponse({"data": str(ex), "status": status.HTTP_500_INTERNAL_SERVER_ERROR},
    #                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk):
        try:
            data = []
            stock = get_stock_by_Id(pk)
            if (stock is None):
                return Response({"data": "No record found", "status": status.HTTP_404_NOT_FOUND},
                                status=status.HTTP_404_NOT_FOUND)
            else:

                for cons in stock:
                    con_data = model_to_dict(cons)
                    data.append(con_data)


                return Response({"data": data, "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"data": str(ex), "status": status.HTTP_500_INTERNAL_SERVER_ERROR},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InsiderTransactionview(ListCreateAPIView):

        def get(self, request, pk, format=None):
            try:
                data = []
                cards = get_insider_transaction(pk)
                for card in cards:
                    cardData = model_to_dict(card)
                    cardData['symbol'] = model_to_dict(card.symbol)

                    data.append(cardData)

                return Response({"data": data, "status": status.HTTP_200_OK})
            except Exception as ex:
                return Response({"data": str(ex), "status": status.HTTP_403_FORBIDDEN},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # def get(self,pk, request,):
    #     try:
    #         data = []
    #         cards = getInsiderTransaction(pk)
    #         for card in cards:
    #             cardData = model_to_dict(card)
    #             cardData['symbol'] = model_to_dict(card.symbol)
    #             data.append(cardData)
    #
    #         return Response({"data": data, "status": status.HTTP_200_OK})
    #     except Exception as ex:
    #         return Response({"data": str(ex), "status": status.HTTP_403_FORBIDDEN})



class Valuation(ListCreateAPIView):

    def get(self, request, pk, format=None):
        try:
            data = []
            cards = getValuation(pk)
            for card in cards:
                cardData = model_to_dict(card)
                cardData['symbol'] = model_to_dict(card.symbol)
                data.append(cardData)
                market_cap_per_share = int(card.market_cap / card.symbol.price)
                data.append({'market_cap_per_share':str(market_cap_per_share)})



            return Response({"data": data, "status": status.HTTP_200_OK})
        except Exception as ex:
            return Response({"data": str(ex), "status": status.HTTP_403_FORBIDDEN},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostStock(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            dic = request.data

            if ('stock' not in dic.keys()):
                return Response(
                    {"data": "stock is required"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            if (dic['stock'] == True):
                sta = Stock(
                    name = dic['name'],
                    price = dic['price'],
                    change = dic['change']
                )
                sta.save()
                data = model_to_dict(sta)
                return Response({"data": data, "status": status.HTTP_201_CREATED},
                                status=status.HTTP_200_OK)
            else:
                if ('symbol' not in dic.keys()):
                    return Response(
                        {"data": "symbol must be stack table pk its is required"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
                sym=get_stock(dic['symbol'])
                tran = InsiderTransaction(
                    name=dic['name'],
                    cost=dic['cost'],
                    symbol=sym
                )
                tran.save()
                data = model_to_dict(tran)
                data['symbol'] = model_to_dict(tran.symbol)
                return Response({"data": data, "status": status.HTTP_201_CREATED},
                                status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"data": str(ex), "status": status.HTTP_403_FORBIDDEN},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

import requests
import configuration
import data

     #api
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


     #Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS, #подставляем полный url
                    json=body) #тело запроса


     #Получение заказа по треку заказа
def get_order_by_track_number(track_numder):
    response=requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER + track_numder)
    return response.status_code




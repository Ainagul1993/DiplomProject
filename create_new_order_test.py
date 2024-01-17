# Антипова Айнагуль, 12-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# Выполнение запроса на создание заказа
def create_new_order():
    # Формирование тело запроса
    request_body = data.order_body
    # Отправка запроса на создание заказа
    response_order = sender_stand_request.post_new_order(request_body)
    # Сохранение полученного номера трэк заказа
    return response_order.json()["track"]

    # Отправка запроса на получения информации о заказе по треку и проверка ответа


def test_get_info_order():
    current_track_number = create_new_order()
    response_status_code = sender_stand_request.get_order_by_track_number(str(current_track_number))
    assert response_status_code == 200

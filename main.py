import requests


# Функция удаления партнеров или партнера
def drop_partners(partner_ids: list) -> int:
    # Проверка списка id партнеров на пустоту
    if len(partner_ids) == 0:
        # Если список пуст, то выводится сообщение, функция завершается с кодом 1
        print("Списк id партнеров пуст")
        return 1
    # Если список не пуст, то начинается поочередное удаление партнеров с указанными id
    else:
        for p in partner_ids:
            try:
                # Удаление партнеров с указанными id в списке
                result = requests.delete(f"https://dev.admin.domka.shop/api/admin/partners/{p}")
                # Если код ответа равен 200 или 201 то выводится только код ответа
                if result.status_code == 200 or result.status_code == 201:
                    print(f"Партнер id: {p} Результат: {result.status_code}")
                # Если код ответа не равен 200 или 201 то кроме кода ответа выводится текст ответа сервера
                else:
                    print(f"Партнер id: {p} Результат: {result.status_code}\n{result.content.decode()}")
            except Exception as e:
                print(f'Не удалось удалить партнера, ошибка: {e}')
        return 0


if __name__ == '__main__':
    partners_ids = [12319]
    drop_partners(partners_ids)



import requests


# Функция удаления партнеров или партнера
def drop_partners(partners_id:list) -> int:
    # Проверка наличия списка id партнеров
    try:
        id_count = len(partners_id)
    except Exception as e:
        print(f"Не удалось получить количество ID партнеров\n{e}")
        return 1
    # Проверка списка id партнеров на пустоту
    if id_count == 0:
        # Если список пуст, то выводится сообщение, функция завершается с кодом 1
        print("Списк id партнеров пуст")
        return 1
    # Если список не пуст, то начинается поочередное удаление партнеров с указанными id
    else:
        print(f"Количество партнеров в списке: {id_count}")
        for p in partners_id:
            try:
                # Удаление партнеров с указанными id в списке
                result = requests.delete(f"https://dev.admin.domka.shop/api/admin/partners/{p}")
                # Если код ответа равен 200 или 201 то выводится только код ответа
                if result.status_code == 200 or result.status_code == 201:
                    print(f"Партнер ID: {p} Код ответа: {result.status_code}")
                # Если код ответа не равен 200 или 201 то кроме кода выводится текст ответа сервера
                else:
                    print(f"Партнер ID: {p} Результат: {result.status_code}\n{result.content.decode()}")
            except Exception as e:
                print(f'Не удалось удалить партнера, ошибка: {e}')
        return 0


if __name__ == '__main__':
    partners_id = [12356, 12357]
    drop_partners(partners_id)



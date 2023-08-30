from main import drop_partners


# Передан список с более чем одним элементом, партнеры с таким id удален
def test_partner_dropper_single() -> None:
    id_list = [457]
    assert drop_partners(id_list)[0] == 0


# Передан список с одним элементом, партнер с таким id удален
def test_partner_dropper_list() -> None:
    id_list = [123, 457]
    assert drop_partners(id_list)[1] == 404


# Передан пустой список
def test_partner_dropper_empty_list() -> None:
    id_list = []
    assert drop_partners(id_list) == 1


# Перадано число, а не список
def test_partner_dropper_int() -> None:
    id_list = 4
    assert drop_partners(id_list) == 1



from main import drop_partners


# Передан список с более чем одним элементом
def test_partner_dropper_list() -> None:
    id_list = [123]
    assert drop_partners(id_list) == 0


# Передан пустой список
def test_partner_dropper_empty_list() -> None:
    id_list = []
    assert drop_partners(id_list) == 1


# Перадано число, а не список
def test_partner_dropper_int() -> None:
    id_list = 4
    assert drop_partners(id_list) == 1



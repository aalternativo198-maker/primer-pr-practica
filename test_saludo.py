from saludo import saludar


def test_saludar_con_nombre():
    assert saludar("Ana") == "Hola, Ana!"

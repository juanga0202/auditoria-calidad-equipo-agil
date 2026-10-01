from src.citas import validar_cita


def test_hora_valida():
    assert validar_cita(10, True) is True


def test_hora_fuera_de_horario():
    assert validar_cita(20, True) is False


def test_hora_no_disponible():
    assert validar_cita(10, False) is False

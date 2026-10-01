def validar_cita(hora, disponible):
    """Valida si una cita puede ser agendada."""
    if hora < 8 or hora > 17:
        return False

    if not disponible:
        return False

    return True

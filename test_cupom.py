from cupom import desconto_valido, MAXIMO


def test_percentual_exatamente_limite_e_aceito():
    percentual = MAXIMO
    resultado = desconto_valido(percentual)
    assert resultado is True


def test_percentual_limite_mais_um_e_rejeitado():
    percentual = MAXIMO + 1
    resultado = desconto_valido(percentual)
    assert resultado is False


def test_percentual_zero_e_rejeitado():
    percentual = 0
    resultado = desconto_valido(percentual)
    assert resultado is False


def test_percentual_nao_inteiro_e_rejeitado():
    percentual = MAXIMO - 0.5
    resultado = desconto_valido(percentual)
    assert resultado is False

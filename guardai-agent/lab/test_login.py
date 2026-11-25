"""Valida o laboratório: mostra a falha na versão vulnerável e a mitigação na segura.

Rode com: python lab/test_login.py
"""
import app
import app_seguro

ENTRADA_MALICIOSA = "' OR '1'='1"  # exemplo didático clássico, só em código de laboratório


def testar(modulo, nome, esperado_burla):
    conn = modulo.criar_banco()
    normal = modulo.login(conn, "maria", "senha-da-maria")
    errada = modulo.login(conn, "maria", "senha-errada")
    burla = modulo.login(conn, "admin", ENTRADA_MALICIOSA)
    print(f"[{nome}] login normal={normal} | senha errada={errada} | entrada maliciosa={burla}")
    assert normal is True and errada is False
    assert burla is esperado_burla, f"{nome}: resultado inesperado"


if __name__ == "__main__":
    testar(app, "app.py (vulnerável)", esperado_burla=True)
    testar(app_seguro, "app_seguro.py (corrigido)", esperado_burla=False)
    print("OK: a falha existe no app.py e foi mitigada no app_seguro.py")

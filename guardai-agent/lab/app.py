"""Laboratório do GuardAI: login VULNERÁVEL a SQL Injection.

ATENÇÃO: código propositalmente inseguro, só para estudo em laboratório próprio.
Nunca use este código em produção nem teste a técnica em sistemas de terceiros.
"""
import sqlite3


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    conn.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha-do-admin')")
    conn.execute("INSERT INTO usuarios (usuario, senha) VALUES ('maria', 'senha-da-maria')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # FALHA: o SQL é montado juntando o que a pessoa digitou.
    consulta = (
        "SELECT * FROM usuarios WHERE usuario = '" + usuario +
        "' AND senha = '" + senha + "'"
    )
    return conn.execute(consulta).fetchone() is not None


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print("Login OK" if login(conn, usuario, senha) else "Login negado")

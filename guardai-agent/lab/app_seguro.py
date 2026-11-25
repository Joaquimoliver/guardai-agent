"""Laboratório do GuardAI: versão CORRIGIDA do login.

Correções: consulta parametrizada (contra SQL Injection) e senha guardada
com hash PBKDF2 e salt (nunca em texto puro).
"""
import hashlib
import hmac
import os
import sqlite3

ITERACOES = 200_000


def gerar_hash(senha, salt):
    return hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, ITERACOES)


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT UNIQUE, salt BLOB, hash BLOB)"
    )
    for usuario, senha in (("admin", "senha-do-admin"), ("maria", "senha-da-maria")):
        salt = os.urandom(16)
        conn.execute(
            "INSERT INTO usuarios (usuario, salt, hash) VALUES (?, ?, ?)",
            (usuario, salt, gerar_hash(senha, salt)),
        )
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # Parâmetros (?) separam o código SQL dos dados digitados.
    linha = conn.execute(
        "SELECT salt, hash FROM usuarios WHERE usuario = ?", (usuario,)
    ).fetchone()
    if linha is None:
        return False
    salt, hash_guardado = linha
    return hmac.compare_digest(gerar_hash(senha, salt), hash_guardado)


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print("Login OK" if login(conn, usuario, senha) else "Login negado")

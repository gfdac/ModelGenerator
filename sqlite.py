#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Convert file existing_db.db to SQL dump file dump.sql
import sqlite3

import exporter as ex

modelos = []

file = "example.sqlite"


# file = input("Nome do arquivo sqlite: ")
# recebe modelo e nome da tabela
def addProperties(modelo):
    # this works beautifully given that you know the table name
    conne = sqlite3.connect(file)
    # conn.row_factory = lambda cursor, row: row[0]
    c = conne.cursor()
    c.execute("PRAGMA table_info(" + modelo.name + ");")
    lista = []
    for row in c:
        p = ex.Propriedade()
        p.name = row[1]
        p.tipo = row[2]
        # TODO: get default value from database
        p.valor = str(0)

        lista.append(p)
        # print("Propriedade " + p.name + " foi criada.")
        ex.sucesso("Propriedade " + p.name + " foi criada.")

    modelo.propriedades = lista
    # modelo.addproperty(p)
    # print(row[1] + " - " + row[2])


con = sqlite3.connect(file)

con.row_factory = lambda cursor, row: row[0]
cc = con.cursor()
cc.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

for tabela in cc:
    # se for esta 'sqlite_sequence' pula
    if tabela.lower() != 'sqlite_sequence':
        modelo = ex.Modelo()
        modelo.name = tabela

        print("Class 'Model' chamada " + modelo.name + " foi criada.");

        addProperties(modelo)

        # for p in names:
        # print(p)

        modelos.append(modelo)

for modelo in modelos:
    ex.whileMethods(modelo)
    ex.gerarExport(modelo)

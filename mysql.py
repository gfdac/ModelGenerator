# !/usr/bin/env python
# -*- coding: utf-8 -*-

import exporter as ex

database = "exchange"

modelos = []

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursortabela:

        # Read a single record
        sql = "SHOW TABLES FROM %s" % database
        cursortabela.execute(sql)

        while True:
            tabela = cursortabela.fetchone()
            if tabela is None:
                break

            for k, v in tabela.items():
                modelo = ex.Modelo()
                modelo.name = v
                print("Class 'Model' chamada " + modelo.name + " foi criada.")
                modelos.append(modelo)

                # Read a single record
                sql = "SHOW COLUMNS FROM %s" % v

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                        lista = []

                        while True:
                            row = cursor.fetchone()
                            if row is None:
                                break

                            p = ex.Propriedade()
                            p.name = row['Field']
                            p.tipo = row['Type']
                            # TODO: get default value from database
                            p.valor = row['Default']

                            lista.append(p)
                            print("Propriedade " + p.name + " foi criada.")

                        modelo.propriedades = lista

                finally:
                    print("final")
                    # connection.close()

finally:
    connection.close()

for modelo in modelos:
    ex.whileMethods(modelo)
    ex.gerarExport(modelo)

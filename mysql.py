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


# Foreign KEY: TABLE_SCHEMA - exchange
# Foreign KEY: TABLE_NAME - UsuarioBanco
# Foreign KEY: CONSTRAINT_TYPE - FOREIGN KEY
# Foreign KEY: CONSTRAINT_NAME - TESTE_FK_1
# Foreign KEY: COLUMN_NAME - UsuarioID
# Foreign KEY: REFERENCED_TABLE_NAME - Usuario
# Foreign KEY: REFERENCED_COLUMN_NAME - ID
def foreignkey(tabela):
    try:
        with connection.cursor() as cursor:

            # Read a single record
            sql = "SELECT i.TABLE_SCHEMA, i.TABLE_NAME, i.CONSTRAINT_TYPE, i.CONSTRAINT_NAME, k.COLUMN_NAME, k.REFERENCED_TABLE_NAME, k.REFERENCED_COLUMN_NAME FROM information_schema.TABLE_CONSTRAINTS i LEFT JOIN information_schema.KEY_COLUMN_USAGE k ON i.CONSTRAINT_NAME = k.CONSTRAINT_NAME WHERE i.TABLE_SCHEMA = '%s' AND i.CONSTRAINT_TYPE = 'FOREIGN KEY' ORDER BY i.TABLE_NAME;" % tabela
            cursor.execute(sql)

            while True:
                chaves = cursor.fetchone()

                if chaves is None:
                    break

                for k, v in chaves.items():
                    print('Foreign KEY: ' + k + ' - ' + v)
    finally:
        # connection.close()
        print("")


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

                foreignkey(v)

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
                    print("")
                    # connection.close()

finally:
    connection.close()

for modelo in modelos:
    ex.whileMethods(modelo)
    ex.gerarExport(modelo)

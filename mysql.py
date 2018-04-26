# /*[[[cog
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import exporter as ex

modelos = []

import pymysql.cursors
import json, ast, sys, re


def converte(type):
    regex = re.compile('int')
    inteiro = regex.findall(type)

    regex = re.compile('double')
    duplo = regex.findall(type)

    regex = re.compile('float')
    floater = regex.findall(type)

    regex = re.compile('decimal')
    decimal = regex.findall(type)

    regex = re.compile('varchar')
    string = regex.findall(type)

    regex = re.compile('text')
    texto = regex.findall(type)

    if inteiro:
        return "int"
    if string:
        # if type == "varchar(255)":
        return "string"
    if texto:
        return "string"
    if duplo:
        return "double"
    if floater:
        return "float"
    if decimal:
        return "float"

    return type


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='exchange',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursortabela:

        # Read a single record
        sql = "SHOW TABLES FROM exchange"
        cursortabela.execute(sql)

        while True:
            tabela = cursortabela.fetchone()
            if tabela == None:
                break

            # json.dump(row, sys.stdout)

            # print(tabela['Tables_in_exchange'])


            for k, v in tabela.items():
                modelo = ex.Modelo()
                modelo.name = v
                print("Class 'Model' chamada " + modelo.name + " foi criada.");
                modelos.append(modelo)

                # Read a single record
                sql = "SHOW COLUMNS FROM %s" % v

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)

                        lista = []

                        while True:
                            row = cursor.fetchone()
                            if row == None:
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




# ]]]*/
# //[[[end]]]

# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os

tipos = ["Integer", "String", "Number", "Float", "Array[]", "Objeto{}", "Others..."]
exporters = ["Javascript CommonJS", "Javascript Simples", "Java", "TypeScript", "Todos"]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def isInt(val):
    return val == int(val)


class Modelo:
    name = ""
    propriedades = []
    metodos = []

    def __init__(self):
        # print("Model Class Inited")
        self.propriedades.clear()
        self.metodos.clear()

    def addproperty(self, p):
        self.propriedades.append(p)

    def addmethod(self, m):
        self.metodos.append(m)


class Propriedade:
    name = ""
    tipo = ""


class Metodo:
    name = ""
    parametros = []


class Parametro:
    name = ""
    tipo = ""
    valor = None
    valor = None


def gerarExport(modelo):
    num = None
    while True:  # This constructs an infinite loop
        # full exporter text options for user knowlegment
        e = ""
        count = 0
        for member in exporters:
            e = e + " - " + bcolors.OKBLUE + "[" + str(count) + "]" + bcolors.ENDC + member
            count = count + 1
        print("Escolha uma linguagem: " + e)
        num = input("")

        try:
            if isInt(int(num)) and int(num) < len(exporters):
                break
            else:
                print("Escolha um número válido! Tente novamente...")

        except ValueError:
            print("Oops!  Este não é um número válido! Tente novamente...")

    exportar = int(num)

    # Javascript CommonJS Exporter
    if exportar == 0:
        commonjsExporter(modelo)
    # Javascript Simplest Way
    elif exportar == 1:
        jssimplestExporter(modelo)
    # Java exporter
    elif exportar == 2:
        javaExporter(modelo)
    # TypeScript exporter
    elif exportar == 3:
        typeScriptExporter(modelo)
    # Todos
    elif exportar == 4:
        commonjsExporter(modelo)
        jssimplestExporter(modelo)
        javaExporter(modelo)
    else:
        print("Other typers soon")


def addProperty(modelo, p):
    num = None
    while True:  # This constructs an infinite loop
        t = ""
        count = 0
        for member in tipos:
            t = t + " - " + bcolors.OKBLUE + "[" + str(count) + "]" + bcolors.ENDC + member
            count = count + 1
        print("Escolha um tipo: " + t)
        num = input("")

        try:
            if isInt(int(num)) and int(num) < len(tipos):
                break
            else:
                print("Escolha um número válido! Tente novamente...")
        except ValueError:
            print("Oops!  Este não é um número válido! Tente novamente...")

    numerico = int(num)
    # obtem o item da lista de acordo com o indice inputado
    tipo = tipos.__getitem__(numerico)

    valor = input("Entre valor inicial para o campo " + p + ": ")

    property = Propriedade()
    property.name = p
    property.tipo = str(numerico)
    property.valor = valor

    # modelo.propriedades.append(property)
    modelo.addproperty(property)


def addMethod(modelo, m):
    modelo.addmethod(m)
    # modelo.metodos.append(m)
    # TODO: //ADD LOOP for add Parameter for this method


def isNotEmpty(s):
    return bool(s and s.strip())


def createPropertyTypeScript(p):
    r = ""
    if p.tipo is not None and p.valor is not None and p.valor is not "":
        r = r + "     " + p.name + ": " + tipos.__getitem__(int(p.tipo)).lower() + " = '" + p.valor + "';"
    elif p.tipo is not None:
        r = r + "     " + p.name + ": " + tipos.__getitem__(int(p.tipo)).lower() + " = null;"
    else:
        r = r + "     " + p.name + " : Any = null;"
    return r


def createPropertyCommonJS(p):
    # TODO: tratar ''' aspas quando for necessario.. criar lista de quem recebe?
    r = ""
    if p.tipo is not None and p.valor is not None and p.valor is not "":
        r = r + "     var " + p.name + " = '" + p.valor + "';"
    # elif p.tipo is not None:
    #     r = r + "     var " + p.name + " = '';"
    else:
        r = r + "     var " + p.name + " = null;"
    return r


def createDefinePropertyCommonJS(p):
    r = ""
    r = r + "     Object.defineProperty(this, '" + p.name + "', {" + "\n"
    r = r + "         get: function() {" + "\n"
    r = r + "             return " + p.name + ";" + "\n"
    r = r + "     }," + "\n"
    r = r + "     set: function(valor)" + "\n"
    r = r + "     {" + "\n"
    r = r + "     " + p.name + " = valor;" + "\n"
    r = r + "     }," + "\n"
    r = r + "         configurable: false," + "\n"
    r = r + "         enumerable: true" + "\n"
    r = r + "     });" + "\n"
    return r


def createMetodhsTypeScript(m):
    parametros = ""

    # TODO: get param type for Typescript export method correctly
    for param in m.parametros:
        # parametros = parametros + param.name + ": " + param.tipo + " = " + param.valor + ", "
        parametros = parametros + param.name + ": " + "Any" + " = " + "null" + ", "

    return "     " + m.name + "(" + parametros.rstrip(', ') + "){};" + "\n"


def createMetodhsCommonJS(m):
    parametros = ""

    for param in m.parametros:
        parametros = parametros + param.name + ", "

    return "     function " + m.name + "(" + parametros.rstrip(', ') + "){};" + "\n"


def commonjsExporter(modelo):
    print('*' * 50)
    # r = result
    r = ""
    r = r + "function " + modelo.name + "() {" + "\n"
    for p in modelo.propriedades:
        r = r + createPropertyCommonJS(p) + "\n"
    for p in modelo.propriedades:
        r = r + createDefinePropertyCommonJS(p) + "\n"
    for m in modelo.metodos:
        r = r + createMetodhsCommonJS(m) + "\n"
    r = r + "}\n"
    r = r + "module.exports = " + modelo.name + ";" + "\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_commonjs.js", r)


def jssimplestExporter(modelo):
    print('*' * 50)

    r = ""
    r = r + "function " + modelo.name + "() {" + "\n"
    for p in modelo.propriedades:
        r = r + createPropertyCommonJS(p) + "\n"
    # for p in modelo.propriedades:
    #     createDefinePropertyjsSimplest(p)
    for m in modelo.metodos:
        r = r + createMetodhsCommonJS(m) + "\n"
    r = r + "}" + "\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_simplest.js", r)


def typeScriptExporter(modelo):
    print('*' * 50)
    # r = result
    r = ""
    r = r + "class " + modelo.name + "{" + "\n"
    for p in modelo.propriedades:
        r = r + createPropertyTypeScript(p) + "\n"
    # for p in modelo.propriedades:
    #     r = r + createDefinePropertyCommonJS(p) + "\n"
    for m in modelo.metodos:
        r = r + createMetodhsTypeScript(m) + "\n"
    r = r + "}\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_typeScript.ts", r)


def javaExporter(modelo):
    print("Java exporter Under development")


def whileProperties(modelo):
    while True:
        p = input("Entre o nome da propriedade (ou Enter para sair): ").replace(" ", "").replace("\t", "")
        if not p:
            break
        # modelo.addproperty(p)
        # prop = Propriedade()
        # prop.name = p
        # prop.tipo = ""
        addProperty(modelo, p)
        # print("Property While loop has exited")


def whileMethodsParameters(metodo):
    lista = []
    while True:
        i = input("Entre o nome do parametro para o método " + metodo.name + ": ").replace(" ", "").replace("\t", "")
        if not i:
            break
        p = Parametro()
        p.name = i
        # TODO: get from user input!
        p.tipo = ""
        p.valor = ""

        lista.append(p)

    metodo.parametros = lista


def whileMethods(modelo):
    lista = []
    while True:
        i = input("Entre o nome do Metodo para a Classe " + modelo.name + " (ou Enter para sair): ").replace(" ",
                                                                                                             "").replace(
            "\t", "")
        # i = input("Entre o nome do Metodo: Metodo(Param1,Param2,ParamN, callback()) (ou Enter para sair): ")
        if not i:
            break
        m = Metodo()
        m.name = i

        whileMethodsParameters(m)

        lista.append(m)
        # modelo.addmethod(m)
        # print("Method While loop has exited")

    modelo.metodos = lista


def startAskForModel():
    modelo = Modelo()
    print('*' * 50)
    while True:
        modelo.name = input("Entre o Nome da Classe 'Model': ").replace(" ", "").replace("\t", "")
        if isNotEmpty(modelo.name):
            break

    whileProperties(modelo)
    whileMethods(modelo)
    gerarExport(modelo)


def createDirectory(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def write_file(file, data):
    """
    this function write data to file
    :param data:
    :return:
    """
    # file_name = r'D:\log.txt'
    file_name = "./exporter/" + file

    createDirectory("./exporter")

    with open(file_name, 'wb') as x_file:
        x_file.write(bytes(data, encoding="UTF-8"))

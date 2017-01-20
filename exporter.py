 #!/usr/bin/python3
 # -*- coding: utf-8 -*-

tipos = ["[0]Integer", "[1]String", "[2]Float", "[3]Array[]", "[4]Objeto{}", "[5]Others..."]
exporters = ["[0]Javascript CommonJS", "[1]Javascript Simples", "[2]Java", "[3]Todos"]


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

        for member in exporters:
            e = e + " - " + member
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
    # Todos
    elif exportar == 3:
        commonjsExporter(modelo)
        jssimplestExporter(modelo)
        javaExporter(modelo)
    else:
        print("Other typers soon")


def addProperty(modelo, p):
    num = None
    while True:  # This constructs an infinite loop
        t = ""
        for member in tipos:
            t = t + " - " + member
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


def createPropertyCommonJS(p):
    if p.tipo == "1" and p.valor is not None:
        print("     var " + p.name + " = '" + p.valor + "';")
    elif p.tipo == "1" and p.valor is None:
        print("     var " + p.name + " = '';")
    else:
        print("     var " + p.name + " = null;")


def createDefinePropertyCommonJS(p):
    print("     Object.defineProperty(this, '" + p.name + "', {")
    print("         get: function() {")
    print("             return " + p.name + ";");
    print("     },")
    print("     set: function(valor)")
    print("     {")
    print("     " + p.name + " = valor;")
    print("     },")
    print("         configurable: false,")
    print("         enumerable: true")
    print("     });")


def createMetodhsCommonJS(m):
    # TODO: obter a lista de parametros e montar com ela

    parametros = ""

    for param in m.parametros:
        parametros = parametros + param.name + ", "

    print("     function " + m.name + "(" + parametros.rstrip(', ') + "){};")


def commonjsExporter(modelo):
    print('*'*50)
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    for p in modelo.propriedades:
        createDefinePropertyCommonJS(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")
    print("module.exports = " + modelo.name + ";")
    print('*'*50)

def jssimplestExporter(modelo):
    print('*'*50)
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    # for p in modelo.propriedades:
    #     createDefinePropertyjsSimplest(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")
    print('*'*50)

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
        i = input("Entre o nome do Metodo (ou Enter para sair): ").replace(" ", "").replace("\t", "")
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
    print('*'*50)
    while True:
        modelo.name = input("Entre o Nome da Classe 'Model': ").replace(" ", "").replace("\t", "")
        if isNotEmpty(modelo.name):
            break

    whileProperties(modelo)
    whileMethods(modelo)
    gerarExport(modelo)

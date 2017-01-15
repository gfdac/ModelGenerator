def isInt(val):
    return val == int(val)


class Modelo:
    name = ""
    propriedades = []
    metodos = []

    def __init__(self):
        print("Model Class Inited")

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


modelo = Modelo()

tipos = ["[0]Integer", "[1]String", "[2]Float", "[3]Array[]", "[4]Objeto{}", "[5]Others..."]

exporters = ["[0]Javascript CommonJS", "[1]Javascript Simples", "[2]Java"]

modelo.name = input("Nome do Modelo")


# adicionar propriedade

# adicionar metodos

# expotar classe para a linguagem escolhida

def addProperty(i):
    t = ""

    print("Escolha um tipo:")
    for member in tipos:
        t = t + " - " + member
    print(t)

    numerico = int(input())
    # obtem o item da lista de acordo com o indice inputado
    tipo = tipos.__getitem__(numerico)

    # TODO: Verificar se int foi inputado, senao tentar de novo, modularizar trecho

    valor = input("Entre valor inicial para o campo " + i + ":")

    p = Propriedade()
    p.name = i
    p.tipo = tipo
    p.valor = valor

    # modelo.propriedades.append(p)
    modelo.addproperty(p)


while True:
    p = input("Entre o nome da propriedade (ou Enter para sair): ")
    if not p:
        break
    addProperty(p)
    # print("Property While loop has exited")


def addMethod(m):
    modelo.addmethod(m)
    # modelo.metodos.append(m)
    # TODO: //ADD LOOP for add Parameter for this method


while True:
    i = input("Entre o nome do Metodo (ou Enter para sair): ")
    # i = input("Entre o nome do Metodo: Metodo(Param1,Param2,ParamN, callback()) (ou Enter para sair): ")
    if not i:
        break
    m = Metodo()
    m.name = i
    addMethod(m)
    # print("Method While loop has exited")


def isNotEmpty(s):
    return bool(s and s.strip())


def createPropertyCommonJS(p):
    if p.tipo == "String" and not p.valor == None:
        print("     var " + p.name + " = '" + p.valor + "';")
    elif p.tipo == "String" and p.valor == None:
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
    print("     function " + m.name + "(){};")


def commonjsExporter():
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    for p in modelo.propriedades:
        createDefinePropertyCommonJS(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")


def jssimplestExporter():
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    # for p in modelo.propriedades:
    #     createDefinePropertyjsSimplest(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")


def javaExporter():
    print("Under development")


def gerarExport():
    # full exporter text options for user knowlegment
    e = ""
    print("Escolha uma linguagem:")
    for member in exporters:
        e = e + " - " + member
    print(e)

    exportar = int(input())

    # Javascript CommonJS Exporter
    if exportar == 0:
        commonjsExporter()
    # Javascript Simplest Way
    elif exportar == 1:
        jssimplestExporter()
    # Java exporter
    elif exportar == 2:
        javaExporter()
        gerarExport()
    else:
        print("Other typers soon")
        gerarExport()


gerarExport()

tipos = ["[0]Integer", "[1]String", "[2]Float", "[3]Array[]", "[4]Objeto{}", "[5]Others..."]
exporters = ["[0]Javascript CommonJS", "[1]Javascript Simples", "[2]Java", "[3]Todos"]


def isInt(val):
    return val == int(val)


class Modelo:
    name = ""
    propriedades = []
    metodos = []

    def __init__(self):
        print("Model Class Inited")
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
        print("Escolha uma linguagem:")
        for member in exporters:
            e = e + " - " + member
        print(e)
        num = input("")
        if isInt(int(num)):
            break

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
        gerarExport()


def addProperty(modelo, p):
    num = None
    while True:  # This constructs an infinite loop
        t = ""
        print("Escolha um tipo:")
        for member in tipos:
            t = t + " - " + member
        print(t)
        num = input("")

        if isInt(int(num)):
            break

    numerico = int(num)
    # obtem o item da lista de acordo com o indice inputado
    tipo = tipos.__getitem__(numerico)

    valor = input("Entre valor inicial para o campo " + p + ":")

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
    print("     function " + m.name + "(){};")


def commonjsExporter(modelo):
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    for p in modelo.propriedades:
        createDefinePropertyCommonJS(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")


def jssimplestExporter(modelo):
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createPropertyCommonJS(p)
    # for p in modelo.propriedades:
    #     createDefinePropertyjsSimplest(p)
    for m in modelo.metodos:
        createMetodhsCommonJS(m)
    print("}")


def javaExporter(modelo):
    print("Java exporter Under development")


def whileProperties(modelo):
    while True:
        p = input("Entre o nome da propriedade (ou Enter para sair): ")
        if not p:
            break
        # modelo.addproperty(p)
        # prop = Propriedade()
        # prop.name = p
        # prop.tipo = ""
        addProperty(modelo, p)
        # print("Property While loop has exited")


def whileMethods(modelo):
    lista = []
    while True:
        i = input("Entre o nome do Metodo (ou Enter para sair): ")
        # i = input("Entre o nome do Metodo: Metodo(Param1,Param2,ParamN, callback()) (ou Enter para sair): ")
        if not i:
            break
        m = Metodo()
        m.name = i
        lista.append(m)
        # modelo.addmethod(m)
        # print("Method While loop has exited")
    modelo.metodos = lista


def startAskForModel():
    modelo = Modelo()
    modelo.name = input("Nome do Modelo")

    whileProperties(modelo)

    whileMethods(modelo)

    gerarExport(modelo)

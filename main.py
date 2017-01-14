class Modelo:
    name = ""
    propriedades = []
    metodos = []

    def f(self):
        return 'hello world'


class Propriedade:
    name = ""
    tipo = ""
    valor = None

    def f(self):
        return 'hello world'


class Metodo:
    name = ""
    parametros = []

    def f(self):
        return 'hello world'


modelo = Modelo()

my_list = ["Integer", "String", "Float", "Array[]", "Objeto{}"]

exporters = ["Javascript", "Java"]

modelo.name = input("Nome do Modelo")


# adicionar propriedade

# adicionar metodos

# expotar classe para a linguagem escolhida

def addProperty(i):
    tipos = ""

    print("Escolha um tipo:")
    for member in my_list:
        tipos = tipos + " - " + member
    print(tipos)

    tipo = input()
    valor = input("Entre valor inicial para o campo " + i + ":")

    p = Propriedade()
    p.name = i
    p.tipo = tipo
    p.valor = valor

    modelo.propriedades.append(p)


while True:
    i = input("Entre o nome da propriedade (ou Enter para sair): ")
    if not i:
        break
    addProperty(i)
    # print("Property While loop has exited")


def addMethod(i):
    modelo.metodos.append(i)


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


def createProperty(p):
    if p.tipo == "String" and not p.valor == None:
        print("var " + p.name + " = '" + p.valor + "';")
    elif p.tipo == "String" and p.valor == None:
        print("var " + p.name + " = '';")
    else:
        print("var " + p.name + " = null;")


def createDefineProperty(p):
    print("Object.defineProperty(this, '" + p.name + "', {")
    print("     get: function() {")
    print("         return " + p.name + ";");
    print("},")
    print("set: function(valor)")
    print("{")
    print(p.name + " = valor;")
    print("},")
    print("configurable: false,")
    print("enumerable: true")
    print("});")


def createMetodhs(m):
    print("     function " + m.name + "(){};")


e = ""

print("Escolha uma linguagem:")
for member in exporters:
    e = e + " - " + member
print(e)

exportar = input()

if exportar == "Javascript":
    print("function " + modelo.name + "() {")
    for p in modelo.propriedades:
        createProperty(p)
    for p in modelo.propriedades:
        createDefineProperty(p)
    for m in modelo.metodos:
        createMetodhs(m)
    print("}")
elif exportar == "Java":
    print("Under development")
else:
    print("Other typers soon")

# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os

tipos = ["String", "Boolean", "Integer", "Number", "Float", "Array", "Object", "Others..."]
exporters = ["Javascript CommonJS", "Javascript Simples", "Java", "TypeScript", "Swift", "PHP", 'Laravel', "Todos"]

# CONSTANTS for exportes and Tipos
K_TIPO_STRING = 'String'
K_TIPO_VARCHAR = 'Varchar'
K_TIPO_TEXT = 'Text'
K_TIPO_BOOLEAN = 'Boolean'
K_TIPO_INTEGER = "Integer"
K_TIPO_DECIMAL = "Decimal"
K_TIPO_NUMBER = "Number"
K_TIPO_FLOAT = "Float"
K_TIPO_ARRAY = "Array"
K_TIPO_OBJETO = "Object"
K_TIPO_OTHERS = "Others..."

K_EXPORTER_COMMONJS = 0
K_EXPORTER_JAVASCRIPT_SIMPLES = 1
K_EXPORTER_JAVA = 2
K_EXPORTER_TYPESCRIPT = 3
K_EXPORTER_SWIFT = 4
K_EXPORTER_PHP = 5
K_EXPORTER_PHP_LARAVEL = 6
K_EXPORTER_TODOS = 7


class bcolors:
    def __init__(self):
        print("")

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
    valor = None


class Metodo:
    name = ""
    parametros = []


class Parametro:
    name = ""
    tipo = ""
    valor = None


def gerarExport(modelo):
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
    if exportar == K_EXPORTER_COMMONJS:
        commonjsExporter(modelo)
    # Javascript Simplest Way
    elif exportar == K_EXPORTER_JAVASCRIPT_SIMPLES:
        jssimplestExporter(modelo)
    # Java exporter
    elif exportar == K_EXPORTER_JAVA:
        javaExporter(modelo)
    # TypeScript exporter
    elif exportar == K_EXPORTER_TYPESCRIPT:
        typeScriptExporter(modelo)
    # swift exporter
    elif exportar == K_EXPORTER_SWIFT:
        swiftExporter(modelo)
    # php exporter
    elif exportar == K_EXPORTER_PHP:
        phpExporter(modelo)
    # laravel exporter
    elif exportar == K_EXPORTER_PHP_LARAVEL:
        laravelExporter(modelo)

    # Todos
    elif exportar == K_EXPORTER_TODOS:
        commonjsExporter(modelo)
        jssimplestExporter(modelo)
        javaExporter(modelo)
        swiftExporter(modelo)
        phpExporter(modelo)
        laravelExporter(modelo)
    else:
        print("Other languages types soon")
        gerarExport(modelo)


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
    # property.tipo = str(numerico)
    property.tipo = tipo
    property.valor = valor

    # modelo.propriedades.append(property)
    modelo.addproperty(property)


def addMethod(modelo, m):
    modelo.addmethod(m)


def isNotEmpty(s):
    return bool(s and s.strip())


def createPropertyTypeScript(p):
    r = ""
    # Strings
    if p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_STRING.lower() or p.tipo.lower() == K_TIPO_TEXT.lower() or p.tipo.lower() == K_TIPO_VARCHAR.lower()):
        r = r + "     " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_TYPESCRIPT) + " = '" + p.valor + "';"
    # Numbers
    elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_NUMBER.lower() or p.tipo.lower() == K_TIPO_FLOAT.lower() or p.tipo.lower() == K_TIPO_INTEGER.lower() or p.tipo.lower() == K_TIPO_DECIMAL.lower()):
        r = r + "     " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_TYPESCRIPT) + " = " + p.valor + ";"
    # Boolean
    elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_BOOLEAN.lower()):
        r = r + "     " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_TYPESCRIPT) + " = " + p.valor + ";"
    elif p.tipo is not None:
        r = r + "     " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_TYPESCRIPT) + " = null;"
    else:
        r = r + "     " + p.name + " : any = null;"
    return r


def createPropertySwift(p):
    r = ""
    # Strings
    if p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_STRING.lower() or p.tipo.lower() == K_TIPO_TEXT.lower() or p.tipo.lower() == K_TIPO_VARCHAR.lower()):
        r = r + "     var " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_SWIFT) + " = '" + p.valor + "';"
    # Numbers
    elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_NUMBER.lower() or p.tipo.lower() == K_TIPO_FLOAT.lower() or p.tipo.lower() == K_TIPO_INTEGER.lower() or p.tipo.lower() == K_TIPO_DECIMAL.lower()):
        r = r + "     var " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_SWIFT) + " = " + p.valor + ";"
    # Boolean
    elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
            p.tipo.lower() == K_TIPO_BOOLEAN.lower()):
        r = r + "     var " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_SWIFT) + " = " + p.valor + ";"
    elif p.tipo is not None:
        r = r + "     var " + p.name + ": " + converteTipos(p.tipo, K_EXPORTER_SWIFT) + " = nil;"
    else:
        r = r + "     var " + p.name + " = nil;"
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


# protected $_conn;
def createPropertyPHP(p):
    # TODO: tratar ''' aspas quando for necessario.. criar lista de quem recebe?
    r = ""
    if p.tipo is not None and p.valor is not None and p.valor is not "":
        r = r + "     public $_" + p.name + " = '" + p.valor + "';"
    # elif p.tipo is not None:
    #     r = r + "     var " + p.name + " = '';"
    else:
        r = r + "     public $_" + p.name + " = null;"
    return r

#protected $fillable = ['nome', ...];
def createPropertyLaravel(modelo):

    r = ""

    for p in modelo.propriedades:
        r = r + "'"  + p.name + "'" + ", "

    r = r.rstrip(', ')

    r = "   protected $fillable = [" + r + "];"

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


def createMetodhTypeScript(m):
    r = ""

    for param in m.parametros:

        if param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
                param.tipo.lower() == K_TIPO_STRING.lower() or param.tipo.lower() == K_TIPO_TEXT.lower() or param.tipo.lower() == K_TIPO_VARCHAR.lower()):
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_TYPESCRIPT) + " = '" + str(
                param.valor) + "', "

        elif param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
                param.tipo.lower() == K_TIPO_DECIMAL.lower() or param.tipo.lower() == K_TIPO_INTEGER.lower() or param.tipo.lower() == K_TIPO_NUMBER.lower() or param.tipo.lower() == K_TIPO_FLOAT.lower()):
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_TYPESCRIPT) + " = " + str(
                param.valor) + ", "


        elif param.tipo is not None and param.tipo is not "":
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_TYPESCRIPT) + " = " + "null" + ", "
        else:
            r = r + param.name + ": " + "any" + " = " + "null" + ", "

    return "     " + m.name + "(" + r.rstrip(', ') + "){};" + "\n"


def createMetodhSwift(m):
    r = ""

    for param in m.parametros:

        if param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
                param.tipo.lower() == K_TIPO_STRING.lower() or param.tipo.lower() == K_TIPO_TEXT.lower() or param.tipo.lower() == K_TIPO_VARCHAR.lower()):
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_SWIFT) + "', "

        elif param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
                param.tipo.lower() == K_TIPO_DECIMAL.lower() or param.tipo.lower() == K_TIPO_INTEGER.lower() or param.tipo.lower() == K_TIPO_NUMBER.lower() or param.tipo.lower() == K_TIPO_FLOAT.lower()):
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_SWIFT) + ", "


        elif param.tipo is not None and param.tipo is not "":
            r = r + param.name + ": " + converteTipos(param.tipo,
                                                      K_EXPORTER_SWIFT) + ", "
        else:
            r = r + param.name + ": " + "T" + ", "

    return "     func " + m.name + "(" + r.rstrip(', ') + "){};" + "\n"


def createMetodhsCommonJS(m):
    parametros = ""

    for param in m.parametros:
        parametros = parametros + param.name + ", "

    return "     function " + m.name + "(" + parametros.rstrip(', ') + "){};" + "\n"


#    public function ExecuteObject($sql, $data) {
#        // stuff
#    }
def createMetodhsPHP(m):
    parametros = ""

    for param in m.parametros:
        parametros = parametros + "$_" + param.name + ", "

    return "     public function " + m.name + "(" + parametros.rstrip(', ') + "){}" + "\n"


def createMetodhsLaravel(m):
    parametros = ""

    for param in m.parametros:
        parametros = parametros + "$_" + param.name + ", "

    return "     public function " + m.name + "(" + parametros.rstrip(', ') + "){}" + "\n"


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
        r = r + createMetodhTypeScript(m) + "\n"
    r = r + "}\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_typeScript.ts", r)


def swiftExporter(modelo):
    print('*' * 50)
    # r = result
    r = ""
    r = r + "class " + modelo.name + "{" + "\n"
    for p in modelo.propriedades:
        r = r + createPropertySwift(p) + "\n"
    for m in modelo.metodos:
        r = r + createMetodhSwift(m) + "\n"
    r = r + "}\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_typeScript.ts", r)


# class Database {
#    protected $_conn;
#
#    public function __construct($connection) {
#        $this->_conn = $connection;
#    }
#
#    public function ExecuteObject($sql, $data) {
#        // stuff
#    }
# }

# abstract class Model {
#    protected $_db;
#
#    public function __construct(Database $db) {
#        $this->_db = $db;
#    }
# }

def phpExporter(modelo):
    print('*' * 50)
    # r = result
    r = "<?php" + "\n"
    r = r + "class " + modelo.name + " extends Model {" + "\n"

    r = r + "   public function __construct() {" + "\n"
    # $this->_conn = $connection;
    r = r + "   }" + "\n"

    for p in modelo.propriedades:
        r = r + createPropertyPHP(p) + "\n"
    for m in modelo.metodos:
        r = r + createMetodhsPHP(m) + "\n"

    r = r + "}\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_php.php", r)


def laravelExporter(modelo):
    print('*' * 50)
    # r = result
    r = "<?php" + "\n"
    r = r + "namespace App;" + "\n"
    r = r + "use Illuminate\Database\Eloquent\Model;" + "\n"
    r = r + "class " + modelo.name + " extends Model {" + "\n"

    #  protected $table = 'fornecedores';
    r = r + "   protected $table = '" + modelo.name + "';" + "\n"
    r = r + "   public $timestamps = false;" + "\n"

    r = r + createPropertyLaravel(modelo) + "\n"

    for m in modelo.metodos:
        r = r + createMetodhsLaravel(m) + "\n"


    r = r + "   public function __construct() {" + "\n"
    # $this->_conn = $connection;
    r = r + "   }" + "\n"

    r = r + "}\n"

    print(r)
    print('*' * 50)
    write_file(modelo.name + "_laravel.php", r)


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

        # ok

        num = None
        while True:  # This constructs an infinite loop
            t = ""
            count = 0
            for member in tipos:
                t = t + " - " + bcolors.OKBLUE + "[" + str(count) + "]" + bcolors.ENDC + member
                count = count + 1
            print("Escolha um tipo para o parâmetro " + p.name + ": " + t)
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
        # p.tipo = str(numerico)
        p.tipo = tipo

        valor = input("Entre valor inicial para o parametro " + p.name + ": ")
        p.valor = valor

        # ok
        lista.append(p)

    metodo.parametros = lista


# recebe o tipo em texto e o exporter em indice do array
def converteTipos(tipo, exporter):
    # CommonJS
    if exporter == K_EXPORTER_COMMONJS:
        return ""
    # JS Simplest
    elif exporter == K_EXPORTER_JAVASCRIPT_SIMPLES:
        return ""
    # Java
    elif exporter == K_EXPORTER_JAVA:
        return ""
    # TypeScript
    elif exporter == K_EXPORTER_TYPESCRIPT:
        if tipo.lower() == K_TIPO_INTEGER.lower() or tipo.lower() == K_TIPO_FLOAT.lower() or tipo.lower() == K_TIPO_DECIMAL.lower() or tipo.lower() == K_TIPO_NUMBER.lower():
            return "number"
        elif tipo.lower() == K_TIPO_STRING.lower() or tipo.lower() == K_TIPO_VARCHAR.lower() or tipo.lower() == K_TIPO_TEXT.lower():
            return "string"
        elif tipo.lower() == K_TIPO_BOOLEAN.lower():
            return "boolean"
        else:
            return "any"
            # TODO: create for other types like tuples, arrays, enum, void, null and Undefined

    # Swift
    elif exporter == K_EXPORTER_SWIFT:
        if tipo.lower() == K_TIPO_INTEGER.lower():
            return "Int"
        if tipo.lower() == K_TIPO_FLOAT.lower() or tipo.lower() == K_TIPO_DECIMAL.lower() or tipo.lower() == K_TIPO_NUMBER.lower():
            return "Double"
        elif tipo.lower() == K_TIPO_STRING.lower() or tipo.lower() == K_TIPO_VARCHAR.lower() or tipo.lower() == K_TIPO_TEXT.lower():
            return "String"
        elif tipo.lower() == K_TIPO_BOOLEAN.lower():
            return "Boolean"
        else:
            return ""

    # Todos
    elif exporter == K_EXPORTER_TODOS:
        return ""
    else:
        return ""


def whileMethods(modelo):
    lista = []
    while True:
        try:
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
        finally:
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
    :param file:
    :param data:
    :return:
    """
    # file_name = r'D:\log.txt'
    file_name = "./exporter/" + file

    createDirectory("./exporter")

    with open(file_name, 'wb') as x_file:
        x_file.write(bytes(data, encoding="UTF-8"))

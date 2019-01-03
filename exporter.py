#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re


tipos = ["String",
         "Boolean",
         "Integer",
         "Number",
         "Float",
         "Array",
         "Object",
         "Other ->"]

exporters = ["JavaScript",
             "CommonJS",
             "TypeScript",
             "Java",
             "PHP",
             'Laravel',
             "C",
             "C++",
             "Python",
             "Swift",
             "Objective-C",
             "C#",
             "Todos"]

# CONSTANTS for Exporters and Tipos
K_TIPO_STRING = 'String'
K_TIPO_VARCHAR = 'Varchar'
K_TIPO_TEXT = 'Text'
K_TIPO_BOOLEAN = 'Boolean'
K_TIPO_INT = "Int"
K_TIPO_INTEGER = "Integer"
K_TIPO_DECIMAL = "Decimal"
K_TIPO_NUMBER = "Number"
K_TIPO_FLOAT = "Float"
K_TIPO_TIMESTAMP = "Timestamp"
K_TIPO_ARRAY = "Array"
K_TIPO_OBJETO = "Object"
K_TIPO_OTHERS = "Others..."

K_EXPORTER_JAVASCRIPT_SIMPLES = 0
K_EXPORTER_COMMONJS = 1
K_EXPORTER_TYPESCRIPT = 2
K_EXPORTER_JAVA = 3
K_EXPORTER_PHP = 4
K_EXPORTER_PHP_LARAVEL = 5
K_EXPORTER_C = 6
K_EXPORTER_CPP = 7
K_EXPORTER_PYTHON = 8
K_EXPORTER_SWIFT = 9
K_EXPORTER_OBJ_C = 10
K_EXPORTER_CSHARP = 11
K_EXPORTER_TODOS = 12


# Cores para o OUTPUT
class bcolors:
		def __init__(self):
				print("")
		
		HEADER = '\033[95m'
		TESTE = '\033[96m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'


# classe de Modelo
class Modelo:
		name = ""
		propriedades = []
		metodos = []
		
		def __init__(self):
				self.propriedades.clear()
				self.metodos.clear()
		
		def addproperty(self, p):
				self.propriedades.append(p)
		
		def addmethod(self, m):
				self.metodos.append(m)


# Classe Propriedade
class Propriedade:
		name = ""
		tipo = ""
		valor = None


# Classe Metodo
class Metodo:
		name = ""
		parametros = []


# Classe Parametro
class Parametro:
		name = ""
		tipo = ""
		valor = None


# Funcao gerarExport em cima de um Modelo Preenchido
def gerarExport(modelo):
		while True:  # This constructs an infinite loop
				# full exporter text options for user knowlegment
				e = ""
				count = 0
				for member in exporters:
						e = e + bcolors.WARNING + "[" + str(count) + "]" + bcolors.HEADER + member + bcolors.ENDC + " "
						count = count + 1
				# print("Escolha uma linguagem: " + e)
				info("Escolha uma linguagem: " + "\n" + e)
				abre()
				
				try:
						num = input("")
						
						if isInt(int(num)) and int(num) < len(exporters):
								break
						else:
								# print("Escolha um número válido! Tente novamente...")
								erro("Escolha um número válido! Tente novamente...")
				
				except ValueError:
						# print("Oops!  Este não é um número válido! Tente novamente...")
						erro("Oops!  Este não é um número válido! Tente novamente...")
		
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
				typeScriptExporter(modelo)
				swiftExporter(modelo)
				phpExporter(modelo)
				laravelExporter(modelo)
		else:
				aviso("Other languages types soon...")
				gerarExport(modelo)


# Funcao adiciona uma propriedade em um Modelo
def addProperty(modelo, p):
		while True:  # This constructs an infinite loop
				t = ""
				count = 0
				for member in tipos:
						t = t + bcolors.WARNING + "[" + str(count) + "]" + bcolors.HEADER + member + bcolors.ENDC + " "
						count = count + 1
				# print("Escolha um tipo: " + t)
				info("Escolha o tipo da propriedade " + p + "\n" + t)
				abre()
				num = input("")
				
				try:
						if isInt(int(num)) and int(num) < len(tipos):
								break
						else:
								erro("Escolha um número válido! Tente novamente...")
				except ValueError:
						erro("Oops!  Este não é um número válido! Tente novamente...")
		
		numerico = int(num)
		# obtem o item da lista de acordo com o indice inputado
		tipo = tipos.__getitem__(numerico)
		
		info("Informe o valor padrão da Propriedade " + p + " ou Enter para valor vazio:")
		abre()
		valor = input("")
		
		property = Propriedade()
		property.name = p
		# property.tipo = str(numerico)
		property.tipo = tipo
		property.valor = valor
		
		# modelo.propriedades.append(property)
		modelo.addproperty(property)
		
		sucesso("A propriedade " + p + " do tipo " + tipo + " foi incluida na classe " + modelo.name + ".")


# Funcao adiciona um metodo em um Modelo
def addMethod(modelo, m):
		modelo.addmethod(m)


# Funcao verifica se um valor é int
def isInt(val):
		return val == int(val)


# Funcao verifica se valor nao esta vazio
def isNotEmpty(s):
		return bool(s and s.strip())


# Funcao cria uma proppriedade em TypeScript
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


# Funcao cria uma proppriedade em Swift
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


# Funcao cria uma proppriedade em Javascript CommonJS
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


# Funcao cria uma proppriedade em Java
def createPropertyJava(p):
		r = ""
		try:
				# Strings
				if p.tipo is not None and p.valor is not None and p.valor is not "" and (
								p.tipo.lower() == K_TIPO_STRING.lower() or p.tipo.lower() == K_TIPO_TEXT.lower() or p.tipo.lower() == K_TIPO_VARCHAR.lower()):
						r = r + "     " + converteTipos(p.tipo, K_EXPORTER_JAVA) + " " + p.name + " = '" + p.valor + "';"
				# Numbers
				elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
								p.tipo.lower() == K_TIPO_NUMBER.lower() or p.tipo.lower() == K_TIPO_FLOAT.lower() or p.tipo.lower() == K_TIPO_INTEGER.lower() or p.tipo.lower() == K_TIPO_DECIMAL.lower()):
						r = r + "     " + converteTipos(p.tipo, K_EXPORTER_JAVA) + " " + p.name + " = " + p.valor + ";"
				# Boolean
				elif p.tipo is not None and p.valor is not None and p.valor is not "" and (
								p.tipo.lower() == K_TIPO_BOOLEAN.lower()):
						r = r + "     " + converteTipos(p.tipo, K_EXPORTER_JAVA) + " " + p.name + " = " + p.valor + ";"
				elif p.tipo is not None:
						r = r + "     " + converteTipos(p.tipo, K_EXPORTER_JAVA) + " " + p.name + " = " + " null " + ";"
				else:
						r = r + "     " + "Undefined " + p.name + " = null;"
		except TypeError as e:
				r = "ERRO " + str(e)
		
		finally:
				return r
		
		return r


# Funcao cria uma proppriedade em PHP
# EX.: protected $_conn;
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


# Funcao cria uma proppriedade em PHP Laravel
# EX.: protected $fillable = ['nome', ...];
def createPropertyLaravel(modelo):
		r = ""
		
		for p in modelo.propriedades:
				r = r + "'" + p.name + "'" + ", "
		
		r = r.rstrip(', ')
		
		r = "   protected $fillable = [" + r + "];"
		
		return r


# Funcao cria uma Define propriedade em Javascript CommonJS
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


# Funcao cria um Metodo em TypeScript
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


# Funcao cria um Metodo em Swift
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


# Funcao cria um Metodo em Javacript CommonJS
def createMetodhsCommonJS(m):
		parametros = ""
		
		for param in m.parametros:
				parametros = parametros + param.name + ", "
		
		return "     function " + m.name + "(" + parametros.rstrip(', ') + "){};" + "\n"


# Funcao cria um Metodo em Java
def createMetodhsJava(m):
		r = ""
		
		for param in m.parametros:
				
				if param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
								param.tipo.lower() == K_TIPO_STRING.lower() or param.tipo.lower() == K_TIPO_TEXT.lower() or param.tipo.lower() == K_TIPO_VARCHAR.lower()):
						r = r + converteTipos(param.tipo, K_EXPORTER_JAVA) + " " + param.name + " = '" + str(param.valor) + "', "
				
				elif param.tipo is not None and param.tipo is not "" and param.valor is not None and param.valor is not "" and (
								param.tipo.lower() == K_TIPO_DECIMAL.lower() or param.tipo.lower() == K_TIPO_INTEGER.lower() or param.tipo.lower() == K_TIPO_NUMBER.lower() or param.tipo.lower() == K_TIPO_FLOAT.lower()):
						r = r + converteTipos(param.tipo, K_EXPORTER_JAVA) + " " + param.name + " = " + str(param.valor) + ", "
				
				
				elif param.tipo is not None and param.tipo is not "":
						r = r + converteTipos(param.tipo, K_EXPORTER_JAVA) + " " + param.name + " = '" + "null" + ", "
				else:
						r = r + "Undefined " + param.name + " = '" + "null" + ", "
		
		return "     " + m.name + "(" + r.rstrip(', ') + "){};" + "\n"


# Funcao cria um Metodo em PHP
def createMetodhsPHP(m):
		parametros = ""
		
		for param in m.parametros:
				parametros = parametros + "$_" + param.name + ", "
		
		return "     public function " + m.name + "(" + parametros.rstrip(', ') + "){}" + "\n"


# Funcao cria um Metodo em Laravel
def createMetodhsLaravel(m):
		parametros = ""
		
		for param in m.parametros:
				parametros = parametros + "$_" + param.name + ", "
		
		return "     public function " + m.name + "(" + parametros.rstrip(', ') + "){}" + "\n"


# Funcao Exportar Javascript CommonJS
def commonjsExporter(modelo):
		info('*' * 50)
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
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".js", "commonjs", r)


# Funcao Exportar Javascript
def jssimplestExporter(modelo):
		info('*' * 50)
		
		r = ""
		r = r + "function " + modelo.name + "() {" + "\n"
		for p in modelo.propriedades:
				r = r + createPropertyCommonJS(p) + "\n"
		# for p in modelo.propriedades:
		#     createDefinePropertyjsSimplest(p)
		for m in modelo.metodos:
				r = r + createMetodhsCommonJS(m) + "\n"
		r = r + "}" + "\n"
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".js", "simplest", r)


# Funcao Exportar TypeScript
def typeScriptExporter(modelo):
		info('*' * 50)
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
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".ts", "typeScript", r)


# Funcao Exportar Swift
def swiftExporter(modelo):
		info('*' * 50)
		# r = result
		r = ""
		r = r + "class " + modelo.name + "{" + "\n"
		for p in modelo.propriedades:
				r = r + createPropertySwift(p) + "\n"
		for m in modelo.metodos:
				r = r + createMetodhSwift(m) + "\n"
		r = r + "}\n"
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".ts", "swift", r)


# Funcao Exportar PHP
def phpExporter(modelo):
		info('*' * 50)
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
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".php", "php", r)


# Funcao Exportar PHP Laravel
def laravelExporter(modelo):
		info('*' * 50)
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
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".php", "laravel", r)


# Funcao Exportar Java
def propriedadesConstrutorJava(modelo):
		# devolve em formato unico string concatenando tipo e nome do parametro
		# Ex: String nome, int idade
		r = ""
		for p in modelo.propriedades:
				r = r + converteTipos(p.tipo, K_EXPORTER_JAVA) + " " + p.name + ", "
		
		# remove o ultimo  ", "
		# r = r.replace(', ', '')[:-2]
		r = r[:-2]
		
		return r


def javaExporter(modelo):
		info('*' * 50)
		
		r = ""
		r = r + "public class " + modelo.name + " {" + "\n"
		for p in modelo.propriedades:
				r = r + createPropertyJava(p) + "\n"
		for m in modelo.metodos:
				r = r + createMetodhsJava(m) + "\n"
		
		##Linha vazia
		r = r + "\n"
		
		# Construtor default
		r = r + "     //Construtor default" + "\n"
		r = r + "     public " + modelo.name + " () {" + "\n"
		r = r + "     }" + "\n\n"
		
		# Construtor com os atributos
		r = r + "     //Construtor com os atributos" + "\n"
		r = r + "     public " + modelo.name + " (" + propriedadesConstrutorJava(modelo) + ") {" + "\n"
		
		for p in modelo.propriedades:
				r = r + "            this." + p.name + " = " + p.name + ";\n"
		r = r + "     }" + "\n\n"
		
		r = r + "}" + "\n"
		
		sucesso(r)
		info('*' * 50)
		write_file(modelo.name + ".java", "java", r)


# Funcao Loop Propriedades do Modelo
def whileProperties(modelo):
		info("Agora vamos definir as propriedades e atributos da classe " + modelo.name)
		while True:
				info("Informe o nome da propriedade ou Enter para encerrar as propriedades:")
				abre()
				p = input("").replace(" ", "").replace("\t", "")
				if not p:
						break
				# modelo.addproperty(p)
				# prop = Propriedade()
				# prop.name = p
				# prop.tipo = ""
				addProperty(modelo, p)
		# print("Property While loop has exited")


# Funcao Loop Parametros do Metodo
def whileMethodsParameters(metodo):
		info("Agora vamos definir os parametros do método " + metodo.name)
		lista = []
		while True:
				info("Informe o nome do parametro para o método " + metodo.name + ": ")
				abre()
				i = input("").replace(" ", "").replace("\t", "")
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
						info("Escolha um tipo para o parâmetro " + p.name + ": " + t)
						abre()
						num = input("")
						
						try:
								if isInt(int(num)) and int(num) < len(tipos):
										break
								else:
										erro("Escolha um número válido! Tente novamente...")
						except ValueError:
								erro("Oops!  Este não é um número válido! Tente novamente...")
				
				numerico = int(num)
				# obtem o item da lista de acordo com o indice inputado
				tipo = tipos.__getitem__(numerico)
				# p.tipo = str(numerico)
				p.tipo = tipo
				
				info("Informe valor inicial para o parametro " + p.name + ": ")
				abre()
				valor = input("")
				p.valor = valor
				
				# ok
				lista.append(p)
		
		metodo.parametros = lista


# Funcao Converte o tipo para a linguagem especifica
# recebe o tipo em texto e o exporter em indice do array
def converteTipos(tipo, exporter):
		# print ("converteTipos: " + tipo)
		
		#regex para remover innt(11) varchar(255) etc
		tipo = " ".join(re.findall("[a-zA-Z]+", tipo))
		# print ( tipo)
		
		# CommonJS
		if exporter == K_EXPORTER_COMMONJS:
				return ""
		# JS Simplest
		elif exporter == K_EXPORTER_JAVASCRIPT_SIMPLES:
				return ""
		# Java
		elif exporter == K_EXPORTER_JAVA:
				if tipo.lower() == K_TIPO_INTEGER.lower() or tipo.lower() == K_TIPO_INT.lower():
						return "int"
				if tipo.lower() == K_TIPO_FLOAT.lower() or tipo.lower() == K_TIPO_DECIMAL.lower() or tipo.lower() == K_TIPO_NUMBER.lower():
						return "java.math.BigDecimal"
				elif tipo.lower() == K_TIPO_STRING.lower() or tipo.lower() == K_TIPO_VARCHAR.lower() or tipo.lower() == K_TIPO_TEXT.lower():
						return "String"
				elif tipo.lower() == K_TIPO_BOOLEAN.lower():
						return "boolean"
				elif tipo.lower() == K_TIPO_TIMESTAMP.lower():
						return "Date"
				#tipo desconhecido
				elif tipo is not None:
						return tipo.lower()
				else:
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


# Funcao Loop Metodos do Modelo
def whileMethods(modelo):
		lista = []
		while True:
				try:
						
						info("Informe o nome do Metodo para a Classe " + modelo.name + " ou Enter para encerrar os métodos:")
						abre()
						i = input("").replace(" ", "").replace("\t", "")
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


def intro():
		header("Bem vindo ao Gerador de Modelos Versão 0.35Beta")
		header("")
		header("Siga as instruções conforme vão sendo solicitadas.")
		header("")


# Funcao Pergunta Nome do Modelo para input manual
def startAskForModel():
		intro()
		modelo = Modelo()
		# info('*' * 50)
		while True:
				
				info("Como irá chamar sua Classe?")
				abre()
				modelo.name = input("").replace(" ", "").replace("\t", "")
				fecha()
				if isNotEmpty(modelo.name):
						break
		
		whileProperties(modelo)
		whileMethods(modelo)
		gerarExport(modelo)


# Funcao cria diretorio
def createDirectory(dir):
		if not os.path.exists(dir):
				os.mkdir(dir)


def getDate():
		import time
		return time.strftime("%Y%m%d")


# Funcao escreve arquivo de output
def write_file(file, folder, data):
		"""
		this function write data to file
		:param file:
		:param data:
		:return:
		"""
		
		agora = getDate()
		# file_name = r'D:\log.txt'
		file_name = "./exporter/" + agora + "/" + folder + "/" + file
		
		createDirectory("./exporter")
		createDirectory("./exporter/" + agora)
		createDirectory("./exporter/" + agora + "/" + folder)
		
		with open(file_name, 'wb') as x_file:
				x_file.write(bytes(data, encoding="UTF-8"))


def header(mensagem):
		# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)
		print(bcolors.HEADER + mensagem + bcolors.ENDC)


# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)


def info(mensagem):
		# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)
		print(bcolors.OKBLUE + mensagem + bcolors.ENDC)


# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)


def sucesso(mensagem):
		# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)
		print(bcolors.TESTE + mensagem + bcolors.ENDC)


# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)


def erro(mensagem):
		# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)
		print(bcolors.FAIL + mensagem + bcolors.ENDC)


# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)


def aviso(mensagem):
		# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)
		print(bcolors.WARNING + mensagem + bcolors.ENDC)


# print(ex.bcolors.OKGREEN + "*" * 90 + ex.bcolors.ENDC)


def abre():
		print(bcolors.OKGREEN)


def fecha():
		print(bcolors.ENDC)

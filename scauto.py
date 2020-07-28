import os
import re
import json
import logging
import requests as rq
from selenium import webdriver
from selenium.common import exceptions
import time

dbpattern = re.compile(".*\.db$")

'''
Class containing the Selenium integration which executes JS to retrieve token
'''
class SessionStorage:

	def __init__(self, driver):
		self.driver = driver

	def keys(self):
		keys = self.driver.execute_script(
				"var ls = window.sessionStorage, keys = []; "
				"for (var i=0; i<ls.length; i++) " 
				"    keys[i] = ls.key(i); " 
				"return keys;")
		print(keys)
		return keys

	def get(self, key):
	   return self.driver.execute_script(f"return window.sessionStorage.getItem('{key}')")

	def __getitem__(self, key):
		if key in self.keys():
			return self.get(key)
		else:
			raise KeyError(key)

	def __len__(self):
		return self.driver.execute_script("return window.sessionStorage.length;")

'''
Function for retrieving token via login with azure
'''
def login_azure(url='https://software-catalog.cfapps.io/groups', max_time=60):
	token = None
	try:
		w = webdriver.Chrome()
		w.get(url)
		start_time = time.time()
		elapsed_time = time.time() - start_time
		while (w.current_url != url and elapsed_time <=max_time):
			elapsed_time = time.time()- start_time
			logging.info(f"Elapsed time: {elapsed_time}")
			time.sleep(1)
		session_store = SessionStorage(w)
		token = session_store['access_token']

	except KeyError as e:
		logging.error("Access token could not be found")

	except Exception as e:
		logging.error(e)

	#finally:
		#w.close()

	return token

'''
Function for uploading data to concert
'''
def uploadToCon(name, data, token):
	print("\n\nName: "+ str(name))
	print("Data: "+ json.dumps(data))

	cookies = {
	    'X-Authorization': str(token),
	}

	headers = {
	    'Connection': 'keep-alive',
	    'Accept': 'application/json, text/plain, */*',
	    'User-Agent': 'SCAUTO',
	    'Content-Type': 'application/json',
	    'Origin': 'https://software-catalog-dev.cfapps.io',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://software-catalog-dev.cfapps.io/groups',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Authorization': 'Bearer '+str(token),
	}

	data = '['+json.dumps(data)+']'

	response = rq.post('https://software-catalog-dev.cfapps.io/api/software-catalog/v1/groups', headers=headers, cookies=cookies, data=data)

	print("\n\nUpload response code:"+str(response))

def dbProcessor(path):
	path = path.replace(' ','\ ')
	result = {
				"classification": "UNCLASSIFIED",
				"metadata": {},
				"operatingSystem": "Android",
				"priority": 0,
				"source": "User Generated",
				"type": "FILE",
				"value": path
		}

	try:
		tablearray = os.popen("adb shell \"su -c 'sqlite3 "+path+" \".tables\"'\" ").read().split()
		for table in tablearray:
			#print("\tTable: " + table)
			columnarray = os.popen("adb shell \"su -c 'sqlite3 "+path+" \\\"PRAGMA table_info("+table+");\\\"'\" ").read().split()

			columnString = "Columns -"

			for column in columnarray:
				columnString = columnString + " " + column.split("|")[1]

			if len(columnString) > 450:
				columnString = columnString[:450] + " (continued) ..."

			result["metadata"]["Table - "+table] = columnString
	except:
		print("OMG something broke")
	return result

#
def extractor(token):
	outputArray = []

	#each element in pkgarray is an app name
	pkgarray = os.popen("adb shell \"su -c 'pm list packages -f'\" ").read().splitlines()
	print("Installed apps:" + str(pkgarray))

	for pkg in pkgarray:
		processedFiles = []

		pkgOutput = {}
		pkgOutput["classification"] = "UNCLASSIFIED"
		pkgOutput["entries"] = []
		pkgOutput["operatingSystem"] = "Android"
		pkgOutput["operatingSystemVersion"] = "Unspecified"
		pkgOutput["source"] = "User Generated"
		pkgOutput["type"] = "Application"
		pkgOutput["tags"] = ["Android"]

		apkPath = pkg.split(":")[1].split("=")[0]
		pkgName = pkg.split(":")[1].split("=")[1]

		version= "Unspecified"
		aptVersion = os.popen("adb shell \"su -c '/storage/emulated/0/Download/aapt-arm-pie d badging "+apkPath+"'\" | grep versionName").read()
		version_search = re.search('.*versionName=\'([\S]*)\'.*', aptVersion)
		if version_search:
			version = version_search.group(1)

		try:
			aptAppName = os.popen("adb shell \"su -c '/storage/emulated/0/Download/aapt-arm-pie d badging "+apkPath+"'\" | grep application-label\:").read().split("\'")[1]
		except:
			aptAppName = apkPath.split("/")[-1]

		pkgOutput["tags"].append(aptAppName)
		pkgOutput["name"] = aptAppName+" ("+pkgName+")"
		pkgOutput["version"] = version

		path = "/data/data/" + pkgName
		pkgfiles=os.popen("adb shell \"su -c 'find "+path+"' \" ").read().splitlines()

		result = None
		for pkgfile in pkgfiles:
			if pkgfile in processedFiles:
				continue

			if dbpattern.match(pkgfile):
				result = dbProcessor(pkgfile)

				if result is not None:
					pkgOutput["entries"].append(result)

			processedFiles.append(pkgfile)

		if len(pkgOutput["entries"]) > 0:
			uploadToCon(aptAppName, pkgOutput, token)

		outputArray.append(pkgOutput)

	print(outputArray)

if __name__ == "__main__":
	token = login_azure(max_time=60)
	print(f"Token: {token}")
	extractor(token)



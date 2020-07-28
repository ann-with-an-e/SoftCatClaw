import requests
import os
import re
import json

dbpattern = re.compile(".*\.db$")

def uploadToCon(name, data):
	print("\n\nName: "+ str(name))
	print("Data: "+ str(data))
#TODO Add functionality to directly upload
'''
	cookies = {
	'__VCAP_ID__': '75f031b9-1f99-4216-7339-1cc9',
	'JSESSIONID': '540FBE77FAD9D3999CC46',
	}

	headers = {
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'accept': '*/*',
	'authorization': 'Bearer .---',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
	'Content-Type': 'application/json',
	'Origin': 'https://software-catalog-rest.cfapps.io',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://software-catalog-rest.cfapps.io/swagger-ui.html',
	'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
	}

	params = (
	('merge', 'false'),
	)

	print("["+json.dumps(data)+"]")
	os.popen('curl -X POST "https://software-catalog-rest.cfapps.io/groups?merge=false" -H "accept: */*" -H "authorization: Bearer ..---" -H "Content-Type: application/json" -d "'+json.dumps(data).replace('"','\\"')+'"')
'''
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
def extractor():
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
			uploadToCon(aptAppName, pkgOutput)

		outputArray.append(pkgOutput)

	print(outputArray)
#
if __name__ == "__main__":
	extractor()



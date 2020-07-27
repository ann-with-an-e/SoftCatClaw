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
	'__VCAP_ID__': '75f031b9-1f98-4216-7339-1fc9',
	'JSESSIONID': '540FBE77FAD9D39F154C5C099999CC46',
	}

	headers = {
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'accept': '*/*',
	'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6Ik14eERYODgxUW9CZTZCRjBnSnRhbkpaVVpKM1kwRjYzVHBKdXUzLVlpLVEiLCJhbGciOiJSUzI1NiIsIng1dCI6IkN0VHVoTUptRDVNN0RMZHpEMnYyeDNRS1NSWSIsImtpZCI6IkN0VHVoTUptRDVNN0RMZHpEMnYyeDNRS1NSWSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83Y2MxMmQzOS01NTUyLTRiMjItODBiNi03MDI5NmNkZDMzMTIvIiwiaWF0IjoxNTg4MTkwNzY3LCJuYmYiOjE1ODgxOTA3NjcsImV4cCI6MTU4ODE5NDY2NywiYWNjdCI6MSwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhQQUFBQUcwanNxRnB3Q1l4eTQ3UWVCdEprbjhoMnFBTGZtd2NzdGRGWkpqU3FYVDNycW1PWXpwdGMvUGpaTDF6QUpnQmJMVGg2SDBQaTgvWUNBd3VnUXFlN1VnPT0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDEyMkY3OEU5NiIsImFtciI6WyJwd2QiXSwiYXBwX2Rpc3BsYXluYW1lIjoiVHJlY25vYyAtIEF1dGhlbnRpY2F0aW9uIiwiYXBwaWQiOiJmZTkzNGZhZS0xYWJjLTRhNDItODAwNS00ZWM4YzllYmI4ODgiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImEuZHVybmluZ0BvdXRsb29rLmNvbSIsImZhbWlseV9uYW1lIjoiRHVybmluZyIsImdpdmVuX25hbWUiOiJBbm5lIiwiaWRwIjoibGl2ZS5jb20iLCJpcGFkZHIiOiIyMTYuMTU0LjUuNjEiLCJuYW1lIjoiQW5uZSBEdXJuaW5nIiwib2lkIjoiZGY2OWRkZDctMGZjYy00MjkzLWIzZjYtOWY1YzU0ZDc3MjkwIiwicGxhdGYiOiI1IiwicHVpZCI6IjEwMDMyMDAwQTM2MzJBNkQiLCJyaCI6IjAuQVRZQU9TM0JmRkpWSWt1QXRuQXBiTjB6RXE1UGtfNjhHa0pLZ0FWT3lNbnJ1SWcyQUh3LiIsInNjcCI6IkRpcmVjdG9yeS5SZWFkLkFsbCBHcm91cC5SZWFkLkFsbCBvcGVuaWQgVXNlci5SZWFkIFVzZXIuUmVhZC5BbGwgcHJvZmlsZSBlbWFpbCIsInN1YiI6IkM5TTZTRlhlRC1YSmxRdFlsTWtpR081S0tFYjJKd0dJNVFwZEhHQXNLTFUiLCJ0aWQiOiI3Y2MxMmQzOS01NTUyLTRiMjItODBiNi03MDI5NmNkZDMzMTIiLCJ1bmlxdWVfbmFtZSI6ImxpdmUuY29tI2EuZHVybmluZ0BvdXRsb29rLmNvbSIsInV0aSI6ImVkMTJualNCcEUtSTltYmROR1NlQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfc3QiOnsic3ViIjoiLW1aVlF1Z2lOMTFQbWZ0cFdtaDFuY1Z3Rlc2czFZNjlBV0dJN2pJdm50YyJ9LCJ4bXNfdGNkdCI6MTU2MDI1OTIxM30.VLRKYJIiNsAqVM5rZhqn6nomLdXXpm1pf6yCI1FMxfsIbiBuwFEJKXe_zHwJeEglu0uAi6hZ31hTKEbdGTYCdc4vHIKm18m7TbLwW9u6VWzLMUYxR0oTR-1ocP5tBzyLvpIu5424hB88Qz27AAfqv7_P37R8NM0BgLCRmNL_DyjbDnHp9CeDQoYEaDb8t6UYrgD154ujQD5eEM7vQCFXm3zLE-t0ggzri7FjNIOuNm8PiAvUQDK5yMYwOgWdH9WyRxkSVCnBLwk1A0XagRStQ2ZHI7gnRQcn4lBKNuGAjq2-wGAOHfg2oltldM_3LeaMoKhbP1KsP7BCwl6gyfe00g',
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
	os.popen('curl -X POST "https://software-catalog-rest.cfapps.io/groups?merge=false" -H "accept: */*" -H "authorization: Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6Ik14eERYODgxUW9CZTZCRjBnSnRhbkpaVVpKM1kwRjYzVHBKdXUzLVlpLVEiLCJhbGciOiJSUzI1NiIsIng1dCI6IkN0VHVoTUptRDVNN0RMZHpEMnYyeDNRS1NSWSIsImtpZCI6IkN0VHVoTUptRDVNN0RMZHpEMnYyeDNRS1NSWSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83Y2MxMmQzOS01NTUyLTRiMjItODBiNi03MDI5NmNkZDMzMTIvIiwiaWF0IjoxNTg4MTkwNzY3LCJuYmYiOjE1ODgxOTA3NjcsImV4cCI6MTU4ODE5NDY2NywiYWNjdCI6MSwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhQQUFBQUcwanNxRnB3Q1l4eTQ3UWVCdEprbjhoMnFBTGZtd2NzdGRGWkpqU3FYVDNycW1PWXpwdGMvUGpaTDF6QUpnQmJMVGg2SDBQaTgvWUNBd3VnUXFlN1VnPT0iLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzQwMDEyMkY3OEU5NiIsImFtciI6WyJwd2QiXSwiYXBwX2Rpc3BsYXluYW1lIjoiVHJlY25vYyAtIEF1dGhlbnRpY2F0aW9uIiwiYXBwaWQiOiJmZTkzNGZhZS0xYWJjLTRhNDItODAwNS00ZWM4YzllYmI4ODgiLCJhcHBpZGFjciI6IjAiLCJlbWFpbCI6ImEuZHVybmluZ0BvdXRsb29rLmNvbSIsImZhbWlseV9uYW1lIjoiRHVybmluZyIsImdpdmVuX25hbWUiOiJBbm5lIiwiaWRwIjoibGl2ZS5jb20iLCJpcGFkZHIiOiIyMTYuMTU0LjUuNjEiLCJuYW1lIjoiQW5uZSBEdXJuaW5nIiwib2lkIjoiZGY2OWRkZDctMGZjYy00MjkzLWIzZjYtOWY1YzU0ZDc3MjkwIiwicGxhdGYiOiI1IiwicHVpZCI6IjEwMDMyMDAwQTM2MzJBNkQiLCJyaCI6IjAuQVRZQU9TM0JmRkpWSWt1QXRuQXBiTjB6RXE1UGtfNjhHa0pLZ0FWT3lNbnJ1SWcyQUh3LiIsInNjcCI6IkRpcmVjdG9yeS5SZWFkLkFsbCBHcm91cC5SZWFkLkFsbCBvcGVuaWQgVXNlci5SZWFkIFVzZXIuUmVhZC5BbGwgcHJvZmlsZSBlbWFpbCIsInN1YiI6IkM5TTZTRlhlRC1YSmxRdFlsTWtpR081S0tFYjJKd0dJNVFwZEhHQXNLTFUiLCJ0aWQiOiI3Y2MxMmQzOS01NTUyLTRiMjItODBiNi03MDI5NmNkZDMzMTIiLCJ1bmlxdWVfbmFtZSI6ImxpdmUuY29tI2EuZHVybmluZ0BvdXRsb29rLmNvbSIsInV0aSI6ImVkMTJualNCcEUtSTltYmROR1NlQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfc3QiOnsic3ViIjoiLW1aVlF1Z2lOMTFQbWZ0cFdtaDFuY1Z3Rlc2czFZNjlBV0dJN2pJdm50YyJ9LCJ4bXNfdGNkdCI6MTU2MDI1OTIxM30.VLRKYJIiNsAqVM5rZhqn6nomLdXXpm1pf6yCI1FMxfsIbiBuwFEJKXe_zHwJeEglu0uAi6hZ31hTKEbdGTYCdc4vHIKm18m7TbLwW9u6VWzLMUYxR0oTR-1ocP5tBzyLvpIu5424hB88Qz27AAfqv7_P37R8NM0BgLCRmNL_DyjbDnHp9CeDQoYEaDb8t6UYrgD154ujQD5eEM7vQCFXm3zLE-t0ggzri7FjNIOuNm8PiAvUQDK5yMYwOgWdH9WyRxkSVCnBLwk1A0XagRStQ2ZHI7gnRQcn4lBKNuGAjq2-wGAOHfg2oltldM_3LeaMoKhbP1KsP7BCwl6gyfe00g" -H "Content-Type: application/json" -d "'+json.dumps(data).replace('"','\\"')+'"')
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



import base64
import requests

class Mosyle:
	
	# Create Mosyle instance
	def __init__(self, key, url = "https://businessapi.mosyle.com/v1", user = "", password = "", dry_run=False):
		# Attribute the variable to the instance
		self.url = url
		self.request = requests.Session()
		self.request.headers["accesstoken"] = key
		self.request.headers["content-type"] = "application/json"
		loginResponse = self.request.post(self.url + "/login", json = {
			"email" : user,
			"password" : password
		}).headers
		self.request.headers["Authorization"] = loginResponse['Authorization']
		self.dry_run = dry_run

		
	# Create variables requests
	def list(self, os):
		print("Listing devices for OS:", os)
		params = {
			"operation": "list",
			"options": {
				"os": os
			}
		}
		# Concatanate url and send the request
		return self.request.post(self.url + "/devices", json = params )

	def listTimestamp(self, start, end, os):
		params = {
			"operation": "list",
			"options": {
				"os": os,
				"enrolldate_start": start,
				"enrolldate_end": end	
			}
		}
		return self.request.post(self.url + "/devices", json = params )

	def listmobile(self):
		params = {
			"operation": "list",
			"options": {
				"os": "ios"
			}
		}
		return self.request.post(self.url + "/devices", json = params )

	def listuser(self, iduser):
		params = {
			"operation": "list_users",
			"options": { "identifiers": [iduser]
				}
		}
		return self.request.post(self.url + "/users", json = params )
    
	def setAssetTag(self, serialnumber, tag):
		params = {
			"operation": "update_device",
			"serialnumber": serialnumber,
			"asset_tag": tag
		}
		if not self.dry_run:
			return self.request.post(self.url + "/devices", json = params )
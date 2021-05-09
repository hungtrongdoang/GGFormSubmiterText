import requests

url = "" #insert Google Form link vào đây, thay '/viewform' -> '/formResponse'

for i in range(0,10): # number responses
	submission = {"entry.<id>": "",
					"entry.<id>": ""
					} 
	print(submission)
	sent = requests.post(url, submission) # POST request
	if sent:
		print('success')
	else:
		print(' error')
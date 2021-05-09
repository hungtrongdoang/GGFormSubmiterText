import requests

url = "" #insert your Google Form link here, replace '/viewform' by '/formResponse'

for i in range(0,10): # set number of responses you wish to send
	submission = {"entry.<id>": "",
					"entry.<id>": ""
					} # get the entry id as explained in the README.md and fill the dictionary
	print(submission)
	sent = requests.post(url, submission) # store the outcome of POST request
	if sent:
		print('Success!')
	else:
		print('An error has occurred.')
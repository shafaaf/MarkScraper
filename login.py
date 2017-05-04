import requests
from requests import session


values = {
	'personId': 'xxx',
	'pin': 'xxx',
	'verify.dispatch' : '1'
}

# Log in to ROSI
# Resource: http://stackoverflow.com/questions/21928368/login-to-facebook-using-python-requests
url = 'https://sws.rosi.utoronto.ca/sws/auth/login/verify.do'
s = requests.session()
r = s.post(url, data=values)
print "status code for logging in: {}".format(r.status_code)

# Get recent transcripts
transcriptsUrl = "https://sws.rosi.utoronto.ca/sws/transcript/main.do?main.dispatch#/"
r = s.get(transcriptsUrl)
print "status code for recent transcripts page: {}".format(r.status_code)

f = open('recentTranscripts.html', 'w')
f.write(r.content)
f.close()

# Get all transcripts
transcriptsUrl = "https://sws.rosi.utoronto.ca/sws/transcript/academic/view.do?view.dispatch&mode=complete&displayName="
r = s.get(transcriptsUrl)
print "status code for all transcripts page: {}".format(r.status_code)

f = open('allTranscripts.html', 'w')
f.write(r.content)
f.close()


# Parse the html using beautiful soup
from parse import *
parse()

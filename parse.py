with open('transcripts.html') as f: 
	rawHTML = f.read()
#print rawHTML

# Extracting transcripts
from bs4 import BeautifulSoup
html_doc = rawHTML
soup = BeautifulSoup(html_doc, 'html.parser')

#print "=== pretty version is: \n"
#print(soup.prettify())

tbodyStatus0 = soup.find("tbody", {"id": "status0"})
#print tbodyStatus0

print "\n\n ===All tr tags"

#each tr is a different course under status0
trTags = tbodyStatus0.find_all("tr") # returns a list of all <tr> children of li
#print trTags
trTagsListLength = len(trTags)
print "trTagsListLength is: {}".format(trTagsListLength)

print "\n\n ===One by one tr tags"
for i, trTag in enumerate(trTags):
    if (i == 0) or (i == trTagsListLength -2):
    	continue
    if (i == trTagsListLength - 1):
    	tdTag = trTag.find("td")
    	gpas = tdTag.text
    	formattedGpas = "".join(gpas.split())
    	print "GPAs are: {}".format(formattedGpas)
    	continue

    #tdTags are course, weight etc for each tr
    tdTags = trTag.find_all("td")
    
    courseString = ""
    for j, tdTag in enumerate(tdTags): 
    	if (j == 0):
    		#print "Course: {}".format(tdTag.string)
    		courseString = courseString + "Course: " + str(tdTag.string)

    	elif (j == 1):
    		#print "Weight: {}".format(tdTag.string)
    		courseString = courseString + ", Weight: " + tdTag.string

    	elif (j == 2):
    		mark = tdTag.string
    		formattedMark = "".join(mark.split())
    		#print "Mark: {}".format(formattedMark)
    		courseString = courseString + ", Mark: " + formattedMark

    	elif (j == 3):
    		#print "Grade: {}".format(tdTag.string)
    		courseString = courseString + ", Grade: " + tdTag.string
    	
    	elif (j == 4):
    		#print "Avg: {}".format(tdTag.string)
    		courseString = courseString + ", Avg: " + tdTag.string
    	
    print courseString



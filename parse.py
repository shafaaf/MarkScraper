with open('transcripts.html') as f: 
	rawHTML = f.read()
#print rawHTML

# Extracting transcripts
from bs4 import BeautifulSoup
html_doc = rawHTML
soup = BeautifulSoup(html_doc, 'html.parser')

#print "=== pretty version is: \n"
#print(soup.prettify())

# For 1st semester of latest year transcripts
tbodyStatus0 = soup.find("tbody", {"id": "status0"})

print "\n===Extracting tr tags"

# Each tr is a different course under status0.
# There are also other tr tags which refer to other rows and need to be skipped
trTags = tbodyStatus0.find_all("tr") # returns a list of all <tr> children of id status0

# Get tr tags length to ensure removal of unwanted rows later
trTagsListLength = len(trTags)
print "trTagsListLength is: {}".format(trTagsListLength)

print "\n\n===Going through one by one each course (tr tag)"
for i, trTag in enumerate(trTags):
	# Skip over these tr tags as not needed
    if (i == 0) or (i == trTagsListLength -2):
    	continue
    # This tr tag contains gpa to handle case
    if (i == trTagsListLength - 1):
    	tdTag = trTag.find("td")
    	gpas = tdTag.text
    	formattedGpas = "".join(gpas.split())
    	print "GPAs are: {}".format(formattedGpas)
    	continue

    # Rest of the tr tags are each courses
    # tdTags are course, weight etc for each tr
    tdTags = trTag.find_all("td")
    
    # String to contain each course info like coursecode, marks, avg
    courseString = ""
    
    # Go through each td tag which is itself a course
    for j, tdTag in enumerate(tdTags): 
    	if (j == 0):	# Course code and name
    		#print "Course: {}".format(tdTag.string)
    		courseString = courseString + "Course: " + str(tdTag.string)

    	elif (j == 1): # Weight
    		#print "Weight: {}".format(tdTag.string)
    		courseString = courseString + ", Weight: " + tdTag.string

    	elif (j == 2):	# My mark
    		mark = tdTag.string
    		formattedMark = "".join(mark.split())
    		#print "Mark: {}".format(formattedMark)
    		courseString = courseString + ", Mark: " + formattedMark

    	elif (j == 3): #  My letter grade
    		#print "Grade: {}".format(tdTag.string)
    		courseString = courseString + ", Grade: " + tdTag.string
    	
    	elif (j == 4):	# Course avg
    		#print "Avg: {}".format(tdTag.string)
    		courseString = courseString + ", Avg: " + tdTag.string
    	
    # Print each course info
    print courseString



def main():
    from bs4 import BeautifulSoup

    # Extracting recent transcripts
    with open('recentTranscripts.html') as f: 
    	rawHTML = f.read()
    #print rawHTML

    html_doc = rawHTML
    global soup
    soup = BeautifulSoup(html_doc, 'html.parser')

    #print "=== pretty version is: \n"
    #print(soup.prettify())

    # Extracting all transcripts
    with open('allTranscripts.html') as f: 
        rawHTML = f.read()
    #print rawHTML

    html_doc = rawHTML
    global soup2
    soup2 = BeautifulSoup(html_doc, 'html.parser')

    # Parse recent transcripts
    parseRecentTranscripts("status0")
    parseRecentTranscripts("status1")

    # Parse all transcripts
    parseAllTranscripts()
    
#---------------------------------------------------------------------------------------------

def parseRecentTranscripts(status):
    print "\n===parseRecentTranscripts called"
    # For a semester of recent year transcripts
    tbodyStatus = soup.find("tbody", {"id": status})

    #print "\n===Extracting tr tags"

    # Each tr is a different course under status0.
    # There are also other tr tags which refer to other rows and need to be skipped
    trTags = tbodyStatus.find_all("tr") # returns a list of all <tr> children of id status0

    # Get tr tags length to ensure removal of unwanted rows later
    trTagsListLength = len(trTags)
    #print "trTagsListLength is: {}".format(trTagsListLength)

    print "Going through one by one for each course (tr tag)\n"
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

#---------------------------------------------------------------------------------------------

def parseAllTranscripts():
    print "\n\n===parseAllTranscripts called\n"
    courseDivs = soup2.findAll("div", { "class" : "courses blok" })
    #print "courseDivs is: \n{}".format(courseDivs)

    for course in courseDivs:
        print course.text

#---------------------------------------------------------------------------------------------

# To start up program, using: python parse.py
if __name__ == "__main__":
   main()

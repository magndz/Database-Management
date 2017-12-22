#Student ID: 230201072
import os #import os library
#------------------------------------
#General Commet:
    #Type of all parameters are string
#-------------------------------------

#getId function take one parameter that fileName and return numberOfLine for lineId 
def getId(fileName):
        with open(fileName, "r") as f: #read file and represent it with f
            numberOfLine = len(f.readlines()) #take len of lines of files
            return str(numberOfLine) #return numberOfLine 

#create function take two parameters which filenName and fields      
def create(fileName, fields):
    fieldsList = fields.split(",") #fields are divided by ,
    if(not("id" in fieldsList)): 
        fields = "id," + fields+"\n" #add fields line 
        fileName = fileName + ".hw3" #concatenate file name and extension 
        if not(fileName in os.listdir()): #if file name in current directory           
            with open(fileName, "w") as f: #open file in write mod
                f.write(fields) #write fileds in files
                f.close() #close file
            print("Corresponding file was successfully created.") #information message about if file create
        else: 
            print("There was already such a file. It is removed and then created again.") #information message about if file already exist
    else:
        print("You cannot create a file with attribute 'id'.")  #information message about wrong attribute

#deleteFile function take one parameter that fileName and remove that fileName removed from current path 
def deleteFile(fileName): 
    fileName = fileName+".hw3"
    if (fileName in os.listdir()):          
        os.remove(fileName)
        print("Corresponding file was successfully deleted.") #information message about if file deleted sucees successfully
    else:
        print("There is no such file.") #information message about if file not exist in current path

def displayFiles():
    counter = 0 #counter variable for how many file have file extension hw3
    listOfFile = os.listdir() #list of line in current directory
    print("Number of files:", len(str(listOfFile).split("hw3"))-2) #print number of file
    for i in listOfFile: #take all of filename one by one 
        if(len(i.split(".")) == 2): #if the file is not have file extesion like .txt, .jpeg, .xls etc. then program broken this condition to prevent this breakage  
            fileNamePart = i.split(".") #split part of file name by "." like student.txt => ["student","txt"]
            if fileNamePart[1] == "hw3": #this confition for show the user proper files
                counter += 1 #number of file
                print(counter,") "+fileNamePart[0]+": "+open(i,"r").readline().strip()) #finally, write that values

#addLine function take two parameters fileName, values aim of funciton append record in  file 
def addLine(fileName, values):
    fileName = fileName+".hw3"
    if (fileName in os.listdir()):
        lineId = getId(fileName) #take next id from function that getId (line: 9)
        values = lineId+","+values+"\n" #concatenate values of user and set them a variable that values
        attributesOfValue = values.split(",") #split values of user
        with open(fileName, "r") as f:  
            attributesOfFile = f.readlines()[0].strip().split(",") #read fields of file
        with open(fileName, "a") as f:             
            if(len(attributesOfValue) == (len(attributesOfFile))): #that condition for if user write more values over file of attribute
                f.write(values) #write values in the file
                f.close() #and we have to close file for add proceess that add to be permanent
                print("New line was successfully added to students with id =", lineId) #if proccess is right give information massage
            else:
                print("Numbers of attributes do not match.") #if numbers of attributes do not match
    else:
        print("There is no such file.") 

#removeLines function aim of function remove record(s) that match the condition, take four paramaters fileName, conditionField, conditionSign, condition
def removeLines(fileName, conditionField, conditionSign, condition):
    numberOfRowsAffected = 0 #this a counter for have many rows affected
    fileName = fileName+".hw3"
    if (fileName in os.listdir()):
        with open(fileName, "r") as f:
            fileFieldPart = f.readline().strip().split(",") 
            if (conditionField in fileFieldPart):
                coditionFieldIndex = fileFieldPart.index(conditionField) #this line for find index of condition field we have know that will we delete it according to what? 
                with open(fileName, "r") as lines:
                    linesOfFile = lines.readlines()
                    if len(linesOfFile) > 0 : #if there exist any records 
                        for i in linesOfFile[1:]: #take lines of file one by ne [1:] that means pass first line
                            partOfCurrentLine = i.strip().split(",")
                            if(conditionSign == "=="): # if condition is == (equal)
                                if(partOfCurrentLine[coditionFieldIndex] == condition): #condition for delete those that proper the condition
                                    numberOfRowsAffected += 1 #and add counter by 1
                                    linesOfFile.remove(i) #delete process
                            else:
                                 if(partOfCurrentLine[coditionFieldIndex] != condition): #condition is != (not equal)
                                    numberOfRowsAffected += 1
                                    linesOfFile.remove(i)                                    
                        fileTrancate = open(fileName, 'w') #drop all of lines of file 
                        for i in linesOfFile: #and write update lines with other again 
                            fileTrancate.write(i) #write process
                        fileTrancate.close() 
                        print("%d lines were successfully removed." % numberOfRowsAffected) #information message about process is done
                    else: 
                        print("0 lines were successfully removed.") #If there is no appropriate record for the message about 
                lines.close()
            else:
                print("Your query contains an unknown attribute.") #if attribute not exist in fields of file
        f.close()
    else:
        print("There is no such file.")

#modifyLines that modify lines of file accordoing to condition take six parameters those fileName, field, newValue, conditionField, conditionSign, condition
def modifyLines(fileName, field, newValue, conditionField, conditionSign, condition):
    numberOfRowsAffected = 0
    fileName = fileName+".hw3"
    if (fileName in os.listdir()):
        if(field != "id"): #in this project users cannot intervene id field this condition for avoid that
            with open(fileName, "r") as f:
                fileFieldPart = f.readline().strip().split(",") 
                if((field in fileFieldPart) and (conditionField in fileFieldPart)):
                    if (conditionField in fileFieldPart):
                        coditionFieldIndex = fileFieldPart.index(conditionField)
                        print(coditionFieldIndex)
                        fieldIndex = fileFieldPart.index(field) #for which field is modified
                    f.close()
                    with open(fileName, "r") as lines:
                        linesOfFile = lines.readlines()
                        for i in linesOfFile[1:]:
                            partOfCurrentLine = i.strip().split(",")
                            if(conditionSign == "=="):
                                if(partOfCurrentLine[coditionFieldIndex] == condition):
                                    numberOfRowsAffected += 1
                                    i = i.replace(partOfCurrentLine[fieldIndex], newValue) #replace line with new value
                                    linesOfFile[int(partOfCurrentLine[0])] = i #set update lines to list of file lines
                            else:
                                if(partOfCurrentLine[coditionFieldIndex] != condition):
                                    numberOfRowsAffected += 1 
                                    i = i.replace(partOfCurrentLine[fieldIndex], newValue)
                                    linesOfFile[int(partOfCurrentLine[0])] = i
                        lines.close()
                    fileTrancate = open(fileName, 'w')
                    for i in linesOfFile:
                        fileTrancate.write(i)
                    fileTrancate.close()
                    print("%d lines were successfully modified." % numberOfRowsAffected)
                else:
                    print("Your query contains an unknown attribute.")
        else:
            print("Id values cannot be changed.") #information message about changing id
    else:
        print("There is no such file.")

#fecthLines aim of function that List all of enteries by condition that function take five parameters (fileName, fields, conditionField, conditionSign, condition)
def fetchLines(fileName, fields, conditionField, conditionSign, condition):
    fileName = fileName+".hw3"
    indicesOfFields = [] #this array for we will store fields of file
    longestLineOfEnteries = [] #this array for long entries we will align records with that data
    temp = [] #temp array use for store length of fields entries 
    properCondition = 0 #for many records listed by condition
    fieldContains = True #boolean variable for chechk fields
    if (fileName in os.listdir()):
        with open(fileName, "r") as numberLinesFile:
            numberLines = len(numberLinesFile.readlines()) #how many lines exist in file
            numberLinesFile.close() #close file
        if(numberLines > 1 ): #if there is exist records
            with open(fileName, "r") as f:
                fieldsOfFile = f.readline().strip().split(",")
                partOfFields =  fields.split(",")
                f.close()
            for i in partOfFields:            
                if(not(i in fieldsOfFile)): #if attribute is not acceptable
                    fieldContains = False
                else: 
                    indicesOfFields.append(fieldsOfFile.index(i)) #find index of wihch fields are listed                   
            if((conditionField in fieldsOfFile) and fieldContains): 
                coditionFieldIndex = fieldsOfFile.index(conditionField)
                with open(fileName, "r") as f:
                    linesOfFile = f.readlines()
                    for i in indicesOfFields:
                        temp = []
                        for k in linesOfFile:
                            temp.append(len(k.strip().split(",")[i])) #split current line and take ([i] means which field) length of entries of fields and append them temp  
                        longestLineOfEnteries.append(max(temp)) #find max value in temp list
                with open(fileName, "r") as fp:
                    linesOfFp = fp.readlines()
                    print("Number of lines in file " +fileName.split(".")[0] +": ", len(linesOfFp)) #write number of lines
                    for x in linesOfFp[1:]:
                        partOfCurrentLine = x.strip().split(",")
                        if(conditionSign == "=="):
                            if(partOfCurrentLine[coditionFieldIndex] == condition):
                                properCondition += 1                                   
                        else:
                            if(partOfCurrentLine[coditionFieldIndex] != condition):
                                properCondition += 1
                    print("Number of lines that hold the condition: ", properCondition) #write number of lines that proper to condition 
                    for dash in range(sum(longestLineOfEnteries)+(len(longestLineOfEnteries)*3)+1):print("-", end="") #write "-" to head and fotter by most length line
                    print("")
                    for i in range(len(linesOfFp)):
                        partOfModify = linesOfFp[i].strip().split(",")
                        if(conditionSign == "==" and i != 0):
                            if(partOfModify[coditionFieldIndex] == condition):                    
                                for l in range(len(indicesOfFields)):
                                    print("| "+partOfModify[indicesOfFields[l]], end = "") #write fields with "|" concatenate them
                                    for k in range(longestLineOfEnteries[l]-len(partOfModify[indicesOfFields[l]])+1): # for from 0 to different current fields record and most length records in that fields
                                        if(k == longestLineOfEnteries[l]-len(partOfModify[indicesOfFields[l]]) and l == len(indicesOfFields)-1): # if is line end
                                            print(" | ", end = "") #put "|" that end of line
                                        else:
                                            print(" ", end = "")   #else put space                            
                                if(i == 0):
                                    print("")
                                    for dash in range(sum(longestLineOfEnteries)+(len(longestLineOfEnteries)*3)+1):print("-", end="")
                                    print("")
                                else:    
                                    print("")
                        else: #same thing do it for the other condition that "!=""
                            if(partOfModify[coditionFieldIndex] != condition):                 
                                for l in range(len(indicesOfFields)):
                                    print("| "+partOfModify[indicesOfFields[l]], end = "")
                                    for k in range(longestLineOfEnteries[l]-len(partOfModify[indicesOfFields[l]])+1):
                                        if(k == longestLineOfEnteries[l]-len(partOfModify[indicesOfFields[l]]) and l == len(indicesOfFields)-1):
                                            print(" | ", end = "")
                                        else:
                                            print(" ", end = "")                                
                                if(i == 0):
                                    print("")
                                    for dash in range(sum(longestLineOfEnteries)+(len(longestLineOfEnteries)*3)+1):print("-", end="")
                                    print("")
                                else:    
                                    print("")
                if properCondition != 0: 
                    for dash in range(sum(longestLineOfEnteries)+(len(longestLineOfEnteries)*3)+1):print("-", end="")               
            else:
                print("Your query contains an unknown attribute.")   
        else:
            print("No record in file.")                 
    else:
        print("There is no such file.")

#queryIsValid function is make decision about query is valid o not take one parameter that "query" and return decisionOfQuery
def queryIsValid(query):
    decisionOfQuery = "" #decision variable
    #dictionary of query which query must exist that part
    queryDic = {"create":{0:"create", 1:"file", 3:"with"},
                "delete":{0:"delete", 1:"file"},
                "display":{0:"display", 1:"files"},
                "add":{0:"add", 2:"into"},
                "remove":{0:"remove", 1:"lines", 2:"from", 4:"where"},
                "modify":{0:"modify", 2:"in", 4:"as", 6:"where"},
                "fetch":{0:"fetch", 2:"from", 4:"where"}}
    partOfQuery = query.strip().split(" ")
    dashExist = len(query.strip().split("-"))
    if(partOfQuery[0] in queryDic.keys() and dashExist == 1):
        #what kind of query get check of it with if blog
        if ((partOfQuery[0] == "create" and len(partOfQuery) == 5) or (partOfQuery[0] == "delete" and len(partOfQuery) == 3) or (partOfQuery[0] == "display" and len(partOfQuery) == 2) or (partOfQuery[0] == "add" and len(partOfQuery) == 4) or (partOfQuery[0] == "remove" and len(partOfQuery) == 8 and (partOfQuery[6] == "==" or partOfQuery[6] == "!=" )) or (partOfQuery[0] == "modify" and len(partOfQuery) == 10 and (partOfQuery[8] == "==" or partOfQuery[8] == "!=" )) or (partOfQuery[0] == "fetch" and len(partOfQuery) == 8) and (partOfQuery[6] == "==" or partOfQuery[6] == "!=" )):
            for i in queryDic[partOfQuery[0]]:
                if(queryDic[partOfQuery[0]][i] != partOfQuery[i]): #if not in part query dictionary
                    decisionOfQuery = "False"  #set false
                    break
                else:
                    decisionOfQuery = partOfQuery[0]
        else:
            decisionOfQuery = "False"
    else:
        decisionOfQuery = "False"
    return decisionOfQuery #return value store in decisionOfQuery
        
while True:
    query = input("\n\nWhat is your query?\n") #query request
    if query.lower() == "x": break #if query is "x" infinity loop broken
    returnValueOfQueryIsValid = queryIsValid(query) #return of queryIsValid is store in returnValueOfQueryIsValid
    if (returnValueOfQueryIsValid != "False"): #if query is valid
        partOfQueryMain = query.strip().split(" ") #split query by ,
        if(returnValueOfQueryIsValid == "create"): #if it "create" call function that create and give neccessary parameters from partOfQueryMain line(264)
            create(partOfQueryMain[2], partOfQueryMain[4]) #call and give parameter
        elif(returnValueOfQueryIsValid == "delete"): #if it "delete"
            deleteFile(partOfQueryMain[2]) 
        elif (returnValueOfQueryIsValid == "display"): #if it "display"
            displayFiles()
        elif (returnValueOfQueryIsValid == "add"): #if it "add"
            addLine(partOfQueryMain[3], partOfQueryMain[1])
        elif (returnValueOfQueryIsValid == "remove"): #if it "remove"
            removeLines(partOfQueryMain[3], partOfQueryMain[5], partOfQueryMain[6], partOfQueryMain[7])
        elif (returnValueOfQueryIsValid == "modify"): #if it "modify"
            modifyLines(partOfQueryMain[3], partOfQueryMain[1], partOfQueryMain[5], partOfQueryMain[7], partOfQueryMain[8], partOfQueryMain[9])
        elif (returnValueOfQueryIsValid == "fetch"): #if it "fetch"
            fetchLines(partOfQueryMain[3], partOfQueryMain[1], partOfQueryMain[5], partOfQueryMain[6], partOfQueryMain[7])
        else:
            print("Invalid query.")
    else:
        print("Invalid query.") #if query is invalid then show information message about that 
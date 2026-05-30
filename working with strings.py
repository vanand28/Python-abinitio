#WORKING WITH STRINGS

print("Rochester Institute of Technology, Dubai")
print("Rochester Institute of Technology\nDubai")                            #NEWLINE CHARACTER - \n

college = "Rochester Institute of Technology, Dubai"
print("I study in " +college)
print(college.lower())                                                           #CONVERTS STRING INTO LOWERCASE
print(college.upper())                                                           #CONVERTS STRING INTO UPPERCASE
print(college.title())                                                           #CONVERTS STRINGS INTO TITLE CASE
print(college.upper().isupper())                                                 #CHECKS IF THE STRING IS IN UPPERCASE
print(len(college))                                                              #DETERMINE THE LENGTH OF THE STRING
print(college[28])                                                               #PRINTS THE nth CHARACTER OF STRING - n is the index
print(college.index('T'))                                                        #PRINTS THE INDEX OF THE GIVEN CHARACTER
print(college.replace('Rochester Institute of Technology', 'RIT'))      #REPLACES WORDS/LETTERS IN A STRING

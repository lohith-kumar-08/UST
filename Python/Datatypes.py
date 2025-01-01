fname = "Lohith"
height = 5.10
lname = "Kumar"
age=24
fullname = fname + " " + lname


demarker = "*-*"

isMarried = True

print (fullname, "age is", age, "and height is", height)

print (demarker*30) 

print("First 3 characters from fullname:", fullname[:3]) #slicing

print("whole string after 3rd position from fullname:", fullname [3:]) #slicing

print("string between 3rd position to 6th position from fullname:", fullname [3:7]) #slicing

print("whole string except last 2 characters from the fullname:", fullname[:-2]) #slicing

print("last 2 characters from the fullname:", fullname [-2:]) #slicing

print("reversing of the string:", fullname[::-1]) #reversing of string

print("Character at the position 4:", fullname [3]) #indexing

print("Character at the 2nd last position of the string:", fullname [-2]) #indexing

print("number of a's in the fullname:", fullname, "is", fullname.count("a")) #counting of characte

Fullname = fullname.replace("Parag", "Prachi") #replacement

print("replace parag with prachi:", fullname)

print("find first i position in fullname:",fullname.find("i"))

print("find 2nd i position in fullname:", fullname.find("i", 6)) #find

print ("split the fullname into list based on the seperator", fullname.split(" "))#splitting

print("Maritial Status", isMarried)



# ASSESMENT


email = "ilearniexcel@gmail.com"

# 1) Find the position of '@'
at_position = email.find('@')
print("Position of '@':", at_position)

# 2) Extract only '.com' from the email string
dot_com = email[email.find('.com'):]
print("Extracted '.com':", dot_com)

# 3) Extract only 'gmail' from the email
gmail_part = email[email.find('@') + 1:email.find('.com')]
print("Extracted 'gmail':", gmail_part)

# 4) Split the string based on the separator '@'
split_email = email.split('@')
print("Split based on '@':", split_email)
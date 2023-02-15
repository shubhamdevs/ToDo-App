newMember = input("Enter name of the new member: ")
file = open("/Users/shubham/Code Block/ToDo-App/resources/Day6/members.txt", "r")
fileContent = file.readlines()
file.close()


fileContent.append(newMember + "\n")
writeFile = open("/Users/shubham/Code Block/ToDo-App/resources/Day6/members.txt", "w")
fileContent = file.writelines(fileContent)
file.close()

# https://github.com/GrandEmperorBinks

import json
output = []     #create output list for use later on

def altCaps():    #define the altCaps function
    messageList = []
    count = False
    newMessage = ''
    message = input('Enter text to be converted to Alt Caps (enter x to end program): ')      #prompt the user for input

    for character in message:   #convert the input (the message variable) to a list (the messageList) variable
        messageList.append(character.lower())

    for letter in messageList:  #iterate through messageList
        if letter.isalpha() == True:
            if count == False:
                newMessage = newMessage + letter
                count = True
            elif count == True:
                newMessage = newMessage + letter.upper()
                count = False
        else:                   #if the character isn't encodeable/decodeable, add it without encoding to the string
            newMessage = newMessage + letter

    return newMessage           #return the new message newMessage

file = open('data.txt', 'w')    #open the file data.txt


while True:                     #forever repeat
    text = altCaps()              #run the function and save the output as text
    if text == 'x':             #if the text is 'x', break out of infinite loop (ending program)
        break
    else:                       #else add message to a list of encoded/decoded messages
        output.append(text)

json.dump(output, file, indent = 2)     #write list of messages to the file in JSON format
file.close()

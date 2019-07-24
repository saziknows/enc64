import base64


#our logo


print('''
                               $$$$$$\  $$\   $$\ 
                              $$  __$$\ $$ |  $$ |
 $$$$$$\  $$$$$$$\   $$$$$$$\ $$ /  \__|$$ |  $$ |
$$  __$$\ $$  __$$\ $$  _____|$$$$$$$\  $$$$$$$$ |
$$$$$$$$ |$$ |  $$ |$$ /      $$  __$$\ \_____$$ |
$$   ____|$$ |  $$ |$$ |      $$ /  $$ |      $$ |
\$$$$$$$\ $$ |  $$ |\$$$$$$$\  $$$$$$  |      $$ |
 \_______|\__|  \__| \_______| \______/       \__|
                                                                           
''')
#encoding
def baseEncoding():
        #Our input
        data = input("What would you like to encode?: ")
        #We need to convert our data to bytes.
        data_bytes = base64.urlsafe_b64encode(data.encode('utf-8'))
        #Then we convert our byte to a string.
        bytes_str = str(data_bytes, 'utf-8')
        #finally we display our encoded data.
        print(bytes_str)


#decoding
def baseDecoding():
        #Our input again.
        data = input("What are you decoding today?: ")
        #We decode our input.
        data_decode = base64.urlsafe_b64decode(data)
        #Convert it to string.
        bytes_decode = str(data_decode, 'utf-8')
        #Display it as usual.
        print(bytes_decode)

#main menue.       
main = input('What would you like to do?:  \n 1.encode \n 2.decode \n ')
#convert our input to an int.
main_conversion = int(main)
#menue navigation.
if main_conversion == 1:
    baseEncoding()
elif main_conversion == 2:   
    baseDecoding()
else: 
    #just for kicks!
    print('Dont break the rules, fuck off you cunt...') 


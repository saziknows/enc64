import base64 

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

def baseEncoding():
        #Our input
        data = input("What would you like to encode?: ")
        #We need to convert our data to bytes.
        data_bytes = base64.urlsafe_b64encode(data.encode('utf-8'))
        #Then we convert our byte to a string.
        bytes_str = str(data_bytes, 'utf-8')
        #finally we display our encoded data.
        print(bytes_str)



def baseDecoding():
        data = input("What are you decoding today?: ")
        data_decode = base64.urlsafe_b64decode(data)
        bytes_decode = str(data_decode, 'utf-8')
        print(bytes_decode)
       
main = input('What would you like to do?:  \n 1.encode \n 2.decode \n ')

main_conversion = int(main)

if main_conversion == 1:
    baseEncoding()
elif main_conversion == 2:   
    baseDecoding()
else: 
    print('Dont break the rules, fuck off you cunt...') 


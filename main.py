# Generic Birthday attack against BadHash40 which is formed by truncating the first 40 bits of SHA256 has values
#It takes the length of the input /output list of badhash40 from command prompt or takes the default value of algorithm
# When it detects the same hash values found for two different inputs it print those inputs and hasvalue and terminates from the loop   
#importing random, sys and hashlib packages
import random 
from random import sample
import hashlib
import sys

def badhash40(input):                  #Defining Badhash method
    m = hashlib.sha256(input.encode()) # encoding the input and passing to sha256 hash function
    x = m.hexdigest()                  # generating the hexdigest of 256bits(64 digits, 1 digit-4bits )
    return x[:10]                      # returning first 10 digits of X i.e. 40bits


if __name__ == "__main__":#main method starts
    argslist = sys.argv
    if len(argslist) == 3: # checking if the list length is specifies
        print("Length of the input/output hash list is set to ", sys.argv[2])
        listlen = int((sys.argv[2]))
    else: #setting default list length if not specified in cmd
        listlen = int(1.2*(2**20))
    print("Running Generic Birthday attack on BadHash40")
    f = open("hash.data", "w") #opening file 
    found=False #loop variable
    k=1# variable to display number of iterations while loop executes
    while found==False : #while loop starts
        hashlist = {} # creating a dictionary, hast list to store all the hash values
        message = sample(range(2**30),listlen)# generating 2**30 random messages and assigning 2**20 unique values to message
        outputhash = ['']*listlen #declaring output variable of size same as message size
        for i in range(0,len(message)): # iterating over the message  
            outputhash[i] = str(badhash40(str(message[i]))) # Calling badhash40 function by passing each message as string and storing the hash value as a string in outputhash
            f.write('{} : {}\n'.format(message[i],outputhash[i]))# writing the formatted input and outputhash value to file
        j=0 # loop variable initilization
        for j in range(len(outputhash)): #ierating over outputhash list
            if outputhash[j] not in hashlist: #checking whether new hash value is present in haslist
                hashlist[outputhash[j]] = message[j]   #Adding the hash value and input message in hash list
            else: #hash value is already peresent in hashlist
                print("Collision found in",k,"iterations")
                print("Input values for which the hash values collided are ",hashlist[outputhash[j]],message[j])#printing the input messages for which hash value is same
                print("Hash value of the input in hex format is",hex(int(outputhash[j],16))) # printing the respective hash value in hex foramt by converting the string into integer with base 16
                found = True #changing the found variable to True 
        k=k+1#increment while loop
    f.close() # closing the file
        

    
import cv2
import os
import string

img=cv2.imread("tree.jpg")

msg=input("Enter the secret message:")
password=input("Enter password:")

d={}    #d is the dictionary is used for mapping characters intp string chr(i) to its integer ie i .This dictionary is used for encryption purpose to convert characters of the secret messages into integer values
c={}    #c is the dictionary is used for reverse mapping integers into character i to chr(i).This dictionary is used for descryption purpose to covert back integers into charcaters
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
    
m=0
n=0
z=0

for i in range(len(msg)):           #ENCRYPTING THE IMAGE:
     img[n,m,z]=d[msg[i]]           #this loop  converts the each charcters of the msg into intergers by using dictionary d and then stores that
     n=n+1                            #interger value in the corresponding pixel of the img.The specific postion in the image is determined n,m,z.
     m=m+1                           #THe indicies are incremented to move through the image pixel and simulate enconding the message acrosss the image chanels
     z=(z+1)%3

cv2.imwrite("Encrypted.jpg",img)     #the encrypted image is saved as "Encrypted.jpg". and default image viwer is opend to diplay the result
os.system("Start Encrypted.jpg")

message=""
m=0
n=0
z=0

pas=input("Enter the passcode for decryption:")
if password==pas:
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1                                   #it checks if password matches if it match it itirate through the encrypted image,converts the pixel values back to the characters using the
                                                    #dictionary  c and forms the decrypted message
        z=(z+1)%3
    print("Decryption messgae",message)
else:
    print("Not a valid pas")

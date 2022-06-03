#Imports
try:
    import qrcode
    import time
except ImportError as imp: 
    print("Error !")
    time.sleep(1)
    print("Please enter the command: pip3 install -r requirementsQ.txt")
    time.sleep(2)
    print("And execute again the program")
    time.sleep(1)
#End of Imports

#Main program
times=int(input("How many QR codes do you want to make ? "))
if times == 1:
    website=input("Please enter the link for the QR code: ")
    time.sleep(2)
    link=""+str(website)
    qrC = qrcode.QRCode(version = 2,
                    box_size = 10,
                    border = 10)
    qrC.add_data(link)
    qrC.make(fit=True)
    img = qrC.make_image(fill = "black")
    img.save("qrcode.png")
    print("Successfully saved at: qrcode.png")
else: 
    for i in range(int(times)):
        website=input("Please enter the link for the number "+str(i + 1)+" QR code: ")
        time.sleep(2)
        link=""+str(website)
        qrC = qrcode.QRCode(version = 2,
                        box_size = 10,
                        border = 10)
        qrC.add_data(link)
        qrC.make(fit=True)
        QRimg= qrC.make_image(fill = "black")
        QRimg.save("qrcode0000"+str(i)+".png")
        print("Successfully saved at: qrcode.png")

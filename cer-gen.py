#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw,ImageFont
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
 



def SendMail(ImgFileName,name,email):
    msg = MIMEMultipart()
    msg['Subject'] = 'Kampüs Gelişim Günleri 2018'
    msg['From'] = '****'
    msg['To'] = email


    message = """
    Merhabalar """ + name  + """,
    Kampüs Gelişim Günlerine geldiğiniz için teşekkür ederiz,
    Sertifikanız ektedir

    """

    text = MIMEText(message)
    msg.attach(text)


    fp = open(ImgFileName, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

    server = '***'
    port = 0
    user_name = "*****"
    password = "***"


    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user_name, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()



def create_Image(name):
    # Opening the file ser.png
    imageFile = "ser_last.jpg"
    im1=Image.open(imageFile)
    
    draw = ImageDraw.Draw(im1)
    
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)
    
    # Drawing the text on the picture
    draw.text((220, 170),name.decode("utf_8"),(0,0,0),font=fnt)
    draw = ImageDraw.Draw(im1)
    

    im1.close()

    # Save the image with a new name
    name_of_file = "./images/" + name.decode("utf_8") + ".png"
    im1.save(name_of_file)
    return name_of_file



datas = [
    {"name": "TEST","email": "test@test.com"},
   ]


for data in datas:
    
    image_path = create_Image(data["name"])
    SendMail(image_path,data["name"],data["email"])


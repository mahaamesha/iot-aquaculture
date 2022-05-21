import smtplib,ssl
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  


def send_an_email():  
    receiver_email = '10219084@mahasiswa.itb.ac.id'      # To id 
    sender_email = 'maraspi084@gmail.com'          # your id
    sender_pass = 'EsVd4A72_nhi7m!'
    subject = "dududu"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = sender_email  
    msg['To'] = receiver_email  
    msg.preamble = "test "   
    #msg.attach(MIMEText(text))  
  
    img_path = 'test/0511_01/image.jpg'
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open(img_path, "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
    msg.attach(part)  
  
    try:  
       server = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       server.ehlo()  
       server.starttls()  
       server.ehlo()  
       server.login(user = sender_email, password = sender_pass)  # User id & password
       #s.send_message(msg)  
       server.sendmail(sender_email, receiver_email, msg.as_string())  
       server.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception
  
send_an_email() 
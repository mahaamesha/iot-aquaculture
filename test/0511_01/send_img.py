#! / usr / bin / python3
 
# Sendmail file - photo .py
 
import smtplib, sys
 
from email. header import header
 
from email. mime. image import MIMEImage
 
from email. mime. multipart import MIMEMultipart
 
from email. mime. text import MIMEText
 
frm = 'maraspi084 <sender @ myhost .com>'
 
to = 'Another name <. anyone @ gmail .com> '
 
subj = 'photo'
 
msg = 'message text'
 
fn = 'photo. jpg '
 
try:
 
# Create photo
 
camera = picamera. PiCamera ()
 
camera. capture (fn, resize = (640, 480))
 
camera. close ()
 
# Compose email
 
mime = MIMEMultipart ()
 
mime ['From'] = frm
 
mime ['To'] = to
 
mime ['Subject'] = Header (subj, 'utf -8')
 
mime. attach (MIMEText (txt, 'plain', 'utf -8'))
 
# Add a picture
 
f = open (fn, 'rb')
 
img = MIMEImage (f. read ())
 
close ()
 
mime. attach (img)
 
# to ship
 
smtp = smtplib. SMTP ("...")
 
except:
 
print ("An error occurred while sending the e-mail:",
 
sys. exc_info ())
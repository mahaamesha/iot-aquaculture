from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os

def main(isTest=False):
	recever_email = '10219084@mahasiswa.itb.ac.id'
	sender_email = 'maraspi084@gmail.com'
	sender_pass = 'EsVd4A72_nhi7m!'
	subject = '[Report] IoT Aquaculture'

	# Build structure of email
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender_email
	msg['To'] = recever_email

	# Get running-file's path --> /send_email/ folder
	project_path = os.path.join( os.path.dirname(__file__), '../../')

	# Attach body of email
	html_path = 'src/send_email/body.html'		# Relative to working_path
	html_path = os.path.join(project_path, html_path)
	body = open(html_path, 'r').read()
	part_text = MIMEText(body, 'html')
	msg.attach(part_text)

	# Attach image to email
	if isTest:
		img_path = 'img_captured/1.jpg'
	else:
		img_path = '../fish-length-opencv/imgcv/final.jpg'	# relative from path of this file

	img_path = os.path.join(project_path, img_path)
	part_img = MIMEBase('image', 'jpg')
	part_img.set_payload( open(img_path, 'rb').read() )
	encoders.encode_base64(part_img)
	part_img.add_header('Content-Disposition', 'attachment', filename='final.jpg')
	msg.attach(part_img)

	# Send email
	try:
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()     #Identify ourselves with the mail server we are using. 
			smtp.starttls() #Encrypt our connection
			smtp.ehlo()     #Reidentify our connection as encrypted with the mail server
			smtp.login(sender_email, sender_pass)
			smtp.sendmail(sender_email, recever_email, msg.as_string())
		print('Email has been sent')
	except:
		print('Error: unable to send email')


if __name__ == '__main__':
	print('Sending email ...')
	main(isTest=True)
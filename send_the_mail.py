from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
import smtplib
import sys
from email.mime.application import MIMEApplication
from os.path import basename



#in this fun we check how old the kids
def check_age(list_ages):
    list1=list_ages.split()
    map_ob=map(int,list1)
    ls=list(map_ob)
    print(ls)
    for age in ls:
     if age in range(0,5):
            print ("the kids age between 0 to 4 years old")  
     else:
            print ("the kid is older than 4 years ")


def mail_sending(username,mail_server) :
    the_mail="sybertest06@gmail.com"
    password="mauernuhmqtxbflf"
    target=username+mail_server

    #msg = MIMEMultipart()
    msg = EmailMessage()

    msg['From'] = the_mail#the sender's email 
    msg['To'] = target#the recipient's email 
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Congratulation you win a car"# the subject of the mail
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    #https://docs.python.org/3/library/email.examples.html
    msg.add_alternative(f"""
        <blockquote><center><br />
<p style="font-size: 20px;"><img src="https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fwww.diabetes.ie%2Fhome%2Fwin-a-car-homepage%2F&amp;psig=AOvVaw0KjEBt4V7d1J45zKWFmrk3&amp;ust=1669831457317000&amp;source=images&amp;cd=vfe&amp;ved=0CBAQjRxqFwoTCIjA74j90_sCFQAAAAAdAAAAABAE" alt="" /><img style="font-size: 14px;" src="https://www.diabetes.ie/wp-content/uploads/2014/08/win-a-car-homepage.jpg" alt="" width="326" height="175" /></p>
<blockquote>
<h3 style="text-align: center;"><span style="color: #000000;"><strong>&nbsp;Hello Dear {username},</strong></span></h3>
<h3 style="text-align: center;"><span style="color: #000000;"><strong>Congratulations<img src="https://html-online.com/editor/tiny4_9_11/plugins/emoticons/img/smiley-smile.gif" alt="smile" /> {username}, you received a car gift from us<br />To collect your car please fill in your details in the following file<br /></strong></span></h3>
  </blockquote>
<p>&nbsp;</p>
<h3 style="text-align: center;"><span style="color: #000000;"><strong>Greetings from the Skoda company</strong></span></h3>
  
</blockquote>
<span style="color: #0000ff;">Skoda with you all the way</span></center>""", subtype='html')

 # open the file in python as a binary (r for read /// b for bunary)
    with open('attachment.py', 'rb') as f:
     #attach the body of the meddage   
     msg.attach(MIMEApplication(f.read(), Name=basename('attachment.py')))

    #msg.attach(MIMEText(message_text , 'plain'))#to add the message_text to msg with attach inclosure(type plain)
    # MIMEBase 
    #part = MIMEBase('application', "octet-stream")
    #part.set_payload(open("text.txt", "rb").read())
    # encode
    #Encoders.encode_base64(part)
   # part.add_header('Content-Disposition', 'attachment; filename="text.txt"')
   # msg.attach(part)
    try:
        with smtplib.SMTP(host="smtp.gmail.com", port= 587) as smtp:
             smtp.ehlo()
             smtp.starttls()
             smtp.login(the_mail,password)
             smtp.send_message(msg)
             print("sent the mail")
    except:
            print ('there somthing not true...')         



if __name__ == '__main__':
    username = sys.argv[1]#RAWAN
    mail_server = sys.argv[2]#@gmail.com...
    title = sys.argv[3]#MS /MR
    job_title = sys.argv[4]#student ...
    personal_status = sys.argv[5]#single...
    kids = sys.argv[6]
    
    #mail_to = str(username) + "@" + str(mail_server)
    print(f'username : {username}\n '
    f'mail_server : {mail_server}\n '
    f'title : {title}\n '
    f'job_title : {job_title}\n'
    f'personal_status : {personal_status}\n'
    f'kids : {kids}' )

    if sys.argv[6]== 'no' :
        print("")    
    else:
        list_ages=sys.argv[7]#we must to enter string
        print(f'list_ages : {list_ages}\n ')

        check_age(list_ages)

    mail_sending(username,mail_server)




#https://docs.python.org/3/library/email.examples.html


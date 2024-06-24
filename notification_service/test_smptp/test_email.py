import smtplib

email  = input("SENDER EMAIL ")

reeiver_email = input("RECEIVER EMAIL ")

subject = input("SUBJECT: ")

message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(email, "YOUR EMAIL APP PASSWORD SHOULD HERE = HINT: CAN BE CREATED BY USING 2 STEPS VERIFICATION")

server.sendmail(email, reeiver_email, text)

print("Email has been sen to +" +  reeiver_email)
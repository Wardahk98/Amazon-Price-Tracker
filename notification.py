import smtplib
from keys import my_email, password

class Notification:
    def __init__(self):
        self.my_email = my_email  
        self.password = password



    def send_email(self, email, product_name, product_price): 
        self.connection = smtplib.SMTP("smtp.gmail.com",port=587)   
        self.connection.starttls()
        self.connection.login(user=self.my_email,password=self.password)
        self.connection.sendmail(
             from_addr=self.my_email, 
             to_addrs=email,
             msg= f"The product you wanted: {product_name} is now priced {product_price}."
          )

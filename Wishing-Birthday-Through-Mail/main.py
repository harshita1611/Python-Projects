import datetime as dt
import pandas as pd
import random
import smtplib
today = (dt.datetime.now().month, dt.datetime.now().day)

# Assuming the "birthdays.csv" file is in the same directory as the script
data = pd.read_csv("birthday-wisher-normal-start/birthdays.csv")
birthday_dict = {(data_row.month , data_row["day"]): data_row for (index, data_row) in data.iterrows()}

relative_paths = ["birthday-wisher-normal-start/letter_templates/letter_1.txt", "birthday-wisher-normal-start/letter_templates/letter_2.txt","birthday-wisher-normal-start/letter_templates/letter_3.txt"]
if today in birthday_dict:
  with open(random.choice(relative_paths)) as letter_file:
    print("found\n")
    letter = letter_file.read()
    letter = letter.replace("[NAME]", birthday_dict[today]["name"])
  my_email="your mail@gmail.com"
  password="your password"
  with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
    connection.starttls()
    connection.login(user=my_email,password=password)
    from_add = my_email
    to_add = birthday_dict[today]["email"]
    message=f"Subject:Happy Birthday\n\n{letter}"
    connection.sendmail(from_add, to_add, message)
    print("Email sent")
else :
  print("not found")


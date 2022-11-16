##################### Hard Starting Project ######################
EMAIL = "foo"
PASS = "foo"


now = dt.datetime.now()

date = {
    "day": now.day,
    "month": now.month
}

birthday_df = pandas.read_csv("birthdays.csv")

for index, row in birthday_df.iterrows():
    if date["day"] == row.day and date["month"] == row.month:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as data:
            letter = data.read()
            generated_letter = letter.replace("[NAME]", str(row["name"]))

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASS)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg=f"Subject: HAPPY BIRTHDAY! \n\n {generated_letter}"
                                )



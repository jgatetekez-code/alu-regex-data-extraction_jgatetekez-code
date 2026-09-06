import re

with open("input/raw-text.txt", "r") as file:

    text = file.read()
print(text)


emails = re.findall(r"[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}", text)

print(emails)

valid_emails = []

for email in emails:
    if (
        email.endswith("@alueducation.com")
        or email.endswith("@alumni.alueducation.com")
        or email.endswith("@si.alueducation.com")
    ):
        valid_emails.append(email)

print(valid_emails)


            
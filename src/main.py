import re
import json

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

# Extract credit card numbers

credit_cards = re.findall(
    r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    text,
)

# Mask credit card numbers for security

masked_credit_cards = []

for card in credit_cards:
    digits = card.replace(" ", "").replace("-", "")
    masked_card = "*" * 12 + digits[-4:]
    masked_credit_cards.append(masked_card)

print(masked_credit_cards)

# Extract URLs

urls = re.findall(
    r"https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;=-]*)?",
    text,
)

print(urls)

# Extract phone numbers
phone_numbers = re.findall(
    r"(?:\+250[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}"
    r"|\(250\)[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3})",
    text,
)

print(phone_numbers)

# Security validation
safe_emails = []

for email in valid_emails:
    if len(email) <= 100 and " " not in email:
        safe_emails.append(email)

safe_urls = []

for url in urls:
    if len(url) <= 200 and " " not in url:
        safe_urls.append(url)

safe_phone_numbers = []

for phone in phone_numbers:
    if len(phone) <= 20:
        safe_phone_numbers.append(phone)

# Create structured output
results = {
    "emails": emails,
    "alu_emails": safe_emails,
    "credit_cards": masked_credit_cards,
   "urls": safe_urls,
    "phone_numbers": safe_phone_numbers,
}

# Save results as JSON
with open("output/sample-output.json", "w") as file:
    json.dump(results, file, indent=4)

print("Results saved to output/sample-output.json")

            
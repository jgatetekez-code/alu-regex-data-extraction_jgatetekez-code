DATA EXTRACTION AND SECURE VALIDAION
ABOUT PROJECT
This project is a Python program that extracts useful information from a messy customer support report.
I used Python and Regular Expressions (Regex) to find different types of structured data such as emails, credit card numbers, URLs, and phone numbers. I also added validation to make sure that invalid data is not included in the final results.

WHAT THE PROGRAM DOES:
The program extracts the following information:
•	Email addresses
•	Valid ALU email addresses
•	Credit card numbers
•	URLs
•	Rwandan phone numbers
For ALU emails, the program accepts these domains:
•	@alueducation.com
•	@alumni.alueducation.com
•	@si.alueducation.com
For example, an email such as:
jean.mugisha@alueducation.com
is accepted as a valid ALU email.
However:
sarah.mukamana@example.com
is extracted as an email but is not included in the ALU email list.

SECURITY:
Security was considered because the input contains sensitive information.
The program:
•	Ignores malformed email addresses.
•	Ignores invalid URLs.
•	Does not extract incomplete credit card numbers.
•	Masks credit card numbers before saving them.
•	Checks the length of extracted emails, URLs, and phone numbers.
•	Avoids saving the full credit card number.
For example, the credit card:
4111 1111 1111 1111
is saved as:
************1111
This helps protect sensitive payment information.

PROJECT STRUCTURE:
alu-regex-data-extraction_jgatetekez-code/
│
├── input/
│   └── raw-text.txt
│
├── src/
│   └── main.py
│
├── output/
│   └── sample-output.json
│
└── README.md

HOW TO RUN THE PROJECT:
First, make sure you are inside the project directory.
Run the program using:
py src/main.py
The program reads the raw information from:
input/raw-text.txt
and saves the extracted results in:
output/sample-output.json

EXAMPLE:
The program produces structured JSON output similar to:
{
    "emails": [
        "sarah.mukamana@example.com",
        "jean.mugisha@alueducation.com",
        "clara.niyonsenga@alumni.alueducation.com",
        "eric.hakizimana@si.alueducation.com"
    ],
    "alu_emails": [
        "jean.mugisha@alueducation.com",
        "clara.niyonsenga@alumni.alueducation.com",
        "eric.hakizimana@si.alueducation.com"
    ],
    "credit_cards": [
        "************1111"
    ],
    "urls": [
        "https://www.example.com/orders/4521",
        "https://portal.alueducation.com/login",
        "https://alumni.alueducation.com/events",
        "https://support.example.org/contact"
    ],
    "phone_numbers": [
        "+250 788 123 456",
        "+250 781 654 321",
        "+250-723-456-789",
        "(250) 788-987-654"
    ]
}

TECHNOLOGIES USED:
•	Python
•	Regular Expressions (Regex)
•	JSON
•	Git
•	GitHub
WHAT I LEARNED:
Through this project, I practiced using Regex to extract useful information from unstructured text. I also learned how to validate extracted data and how to protect sensitive information such as credit card numbers.

CONCLUSION:
This project shows how raw and messy text can be converted into structured data using Python. It also demonstrates the importance of validation and basic security when handling sensitive information.


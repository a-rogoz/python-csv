import csv


with open("contacts.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(row)

with open("contacts.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(",".join(row))

with open("contacts.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Name"], ":", row["Phone"])

with open("contacts.csv", newline="") as csvfile:
    fieldnames = ["Name", "Phone"]
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row["Name"], row["Phone"])

with open("exported_contacts.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")

    writer.writerow(["Name", "Phone"])
    writer.writerow(["mother", "222-555-101"])
    writer.writerow(["father", "222-555-102"])
    writer.writerow(["wife", "222-555-103"])
    writer.writerow(["mother-in-law", "222-555-104"])


with open("exported_contacts.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # csv.QUOTE_ALL – quotes all values
    # csv.QUOTE_NONNUMERIC – quotes only non-numeric values
    # csv.QUOTE_NONE – doesn't quote any values. It's not a good idea to set this value if you have special characters that require quoting, because this will raise an error

    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105'])

with open("exported_contacts.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Phone"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})


import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone:
    def __init__(self):
        self.contacts = []
    
    def load_contacts_from_csv(self):
        with open("contacts.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                contact = PhoneContact(row["Name"], row["Phone"])
                self.contacts.append(contact)
    
    def search_contacts(self):
        search_query = input("Type your search query: ")
        
        if search_query:
            counter = 0
            for contact in self.contacts:
                if search_query in contact.name or search_query in contact.phone:
                    print(f"{contact.name} {contact.phone}")
                    counter += 1
            if counter is 0:
                print("No contacts found")
        else:
            return "Enter a valid search query!"
        
        
phone = Phone()
phone.load_contacts_from_csv()

phone.search_contacts()


#####


import csv


data = [
    {
        "Exam Name": "Maths",
        "Number of Candidates": 8,
        "Number of Passed Exams": 4,
        "Number of Failed Exams": 6,
        "Best Score": 90,
        "Worst Score": 33
        
    },
    {
        "Exam Name": "Physics",
        "Number of Candidates": 3,
        "Number of Passed Exams": 0,
        "Number of Failed Exams": 3,
        "Best Score": 66,
        "Worst Score": 50
    },
    {
        "Exam Name": "Biology",
        "Number of Candidates": 5,
        "Number of Passed Exams": 2,
        "Number of Failed Exams": 3,
        "Best Score": 88,
        "Worst Score": 23
        
    }
]

with open("exam_results.csv", "w", newline="") as csv_file:
    fieldnames = [
        "Exam Name",
        "Number of Candidates",
        "Number of Passed Exams",
        "Number of Failed Exams",
        "Best Score",
        "Worst Score"
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)


with open("exam_results.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        print(row)
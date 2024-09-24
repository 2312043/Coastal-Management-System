from datetime import datetime
import csv


class Occupant:
    def __init__(self, occupant_ID, first_name, last_name, govt_ID, gender, email, phone, family_members, occupant_status,
                 payment_methods):
        self.occupant_ID = occupant_ID
        self.first_name = first_name
        self.last_name = last_name
        self.govt_ID = govt_ID
        self.gender = gender
        self.email = email
        self.phone = phone
        self.family_members = family_members
        self.occupant_status = occupant_status
        self.payment_methods = payment_methods

    @classmethod
    def fetch_occupant_by_id(cls, occupant_id):
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == occupant_id:
                    return cls(*row)
        return None

    def write_to_csv(self):
        fieldnames = ['Occupant ID', 'First Name', 'Last Name', 'Government ID', 'Gender', 'Email', 'Phone',
                      'Family Members', 'Occupant Status', 'Payment Methods']
        data = [self.occupant_ID, self.first_name, self.last_name, self.govt_ID, self.gender, self.email, self.phone,
                self.family_members, self.occupant_status, self.payment_methods]

        with open('../data/occupants.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(fieldnames)
            writer.writerow(data)

    def get_personal_details(self):
        occupant_data = self.fetch_occupant_data_from_csv()
        return occupant_data

    def fetch_occupant_data_from_csv(self):
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Occupant ID'] == self.occupant_ID:
                    details = (
                        f"Occupant ID: {row['Occupant ID']}\n"
                        f"First Name: {row['First Name']}\n"
                        f"Last Name: {row['Last Name']}\n"
                        f"Government ID: {row['Government ID']}\n"
                        f"Gender: {row['Gender']}\n"
                        f"Email: {row['Email']}\n"
                        f"Phone: {row['Phone']}\n"
                        f"Family Members: {row['Family Members']}\n"
                        f"Occupant Status: {row['Occupant Status']}\n"
                        f"Payment Methods: {row['Payment Methods']}\n"
                    )
                    return details
        return None

    def update_occupant_details(self, FirstName, LastName, GovernmentID, Gender, Email, Phone, FamilyMembers, OccupantStatus, PaymentMethods):
        occupants = []
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.reader(file)
            occupants = [row for row in reader]

        with open('../data/occupants.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for occupant in occupants:
                if occupant[0] == self.occupant_ID:
                    occupant[1] = FirstName
                    occupant[2] = LastName
                    occupant[3] = GovernmentID
                    occupant[4] = Gender
                    occupant[5] = Email
                    occupant[6] = Phone
                    occupant[7] = FamilyMembers
                    occupant[8] = OccupantStatus
                    occupant[9] = PaymentMethods
                writer.writerow(occupant)

    def delete_occupant(self):
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        with open('../data/occupants.csv', mode='w', newline='') as file:
            fieldnames = ['Occupant ID', 'First Name', 'Last Name', 'Government ID', 'Gender', 'Email', 'Phone',
                          'Family Members', 'Occupant Status', 'Payment Methods']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                if row['Occupant ID'] != str(self.occupant_ID):
                    writer.writerow(row)
import csv
from datetime import datetime


class Residence:
    def __init__(self, residence_ID, residence_type, occupant_ID, occupant_type):
        self.residence_ID = residence_ID
        self.residence_type = residence_type
        self.occupant_ID = occupant_ID
        self.occupant_type = occupant_type

    def write_to_csv(self):
        fieldnames = ['Residence ID', 'Residence Type', 'Occupant ID', 'Occupant Type']
        data = [self.residence_ID, self.residence_type, self.occupant_ID, self.occupant_type]

        with open('../data/residences.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(fieldnames)
            writer.writerow(data)

    @classmethod
    def fetch_residence_by_id(cls, residence_ID):
        with open('../data/residences.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Residence ID'] == residence_ID:
                    return cls(row['Residence ID'], row['Residence Type'], row['Occupant ID'].split(','),
                               row['Occupant Type'])
        return None

    def update_occupant(self, new_occupant_ID):
        self.occupant_ID = new_occupant_ID
        self.update_residence_details()

    def update_residence_details(self):
        residences = []
        with open('../data/residences.csv', mode='r') as file:
            reader = csv.reader(file)
            residences = [row for row in reader]

        for residence in residences:
            if residence[0] == self.residence_ID:
                residence[2] = ','.join(self.occupant_ID)
                residence[3] = self.occupant_type

        with open('../data/residences.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(residences)

    def get_residence_details(self):
        with open('../data/residences.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Residence ID'] == self.residence_ID:
                    return row
        return None

    def add_occupant(self, new_occupant_ID):
        occupant_exists = self.validate_occupant_id(new_occupant_ID)
        if occupant_exists and new_occupant_ID not in self.occupant_ID:
            self.occupant_ID.append(new_occupant_ID)
            self.update_residence_details()
            return True
        else:
            return False

    def delete_occupant(self, occupant_ID):
        if occupant_ID in self.occupant_ID:
            self.occupant_ID.remove(occupant_ID)
            self.occupant_type = ""  # Set the occupant ID to an empty string to indicate no type
            self.update_residence_details()
            return True
        else:
            return False

    def get_occupant(self):
        if self.occupant_ID:
            occupant_details = self.fetch_occupant_details(self.occupant_ID)
            return occupant_details
        else:
            return None

    @staticmethod
    def validate_occupant_id(occupant_ID):
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Occupant ID'] == occupant_ID:
                    return True
        return False

    def get_occupancy_status(self):
        if self.occupant_type == "Owner" or self.occupant_type == "Tenant":
            return "Occupied"
        else:
            return "Vacant"

    def set_ownership_type(self, ownership_type):
        self.occupant_type = ownership_type
        self.update_residence_details()

    @classmethod
    def fetch_occupant_details(cls, occupant_id):
        with open('../data/occupants.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Occupant ID'] == occupant_id:
                    occupant_details = {
                        'Occupant ID': row['Occupant ID'],
                        'First Name': row['First Name'],
                        'Last Name': row['Last Name'],
                        'Government ID': row['Government ID'],
                        'Gender': row['Gender'],
                        'Email': row['Email'],
                        'Phone': row['Phone'],
                        'Family Members': row['Family Members'],
                        'Occupant Status': row['Occupant Status'],
                        'Payment Methods': row['Payment Methods']
                    }
                    return occupant_details
        return None

    def generate_payment_receipt(self, payment_amount,occupant_ID):
        receipt = f"""
                    Payment Receipt
                    ------------------------
                    Residence ID: {self.residence_ID}
                    Occupant ID: {occupant_ID}
                    Payment Amount: ${payment_amount}
                    Date: {datetime.now()}
                    ------------------------
                    """

        return receipt

    def make_payment(self, amount, occupant_ID):
        if amount > 0:
            payment_details = {
                'residence_ID': self.residence_ID,
                'occupant_ID': occupant_ID,
                'amount': amount,
                'timestamp': datetime.now(),
                'status': 'Successful'
            }
            self.write_payment_to_csv(payment_details)
            return f"Payment of ${amount} successful. Thank you!"
        else:
            return "Payment failed. Invalid amount or payment method."

    @staticmethod
    def write_payment_to_csv(payment_details):
        with open('../data/payments.csv', mode='a', newline='') as file:
            fieldnames = ['residence_ID', 'occupant_ID', 'amount', 'timestamp', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(payment_details)

    def view_payment_history(self, occupant_id):
        with open('../data/payments.csv', mode='r') as file:
            reader = csv.DictReader(file)
            payment_history = [row for row in reader if row['occupant_ID'] == occupant_id]

        formatted_history = "\n".join(
            [
                f"OccupantID: {record['occupant_ID']}, Amount: {record['amount']}, Timestamp: {record['timestamp']}, Status: {record['status']}"
                for record in
                payment_history])
        return formatted_history

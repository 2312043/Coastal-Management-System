import csv
from classes.residence import Residence
from datetime import datetime


class Street:
    def __init__(self, street_name, representative, residences):
        self.street_name = street_name
        self.representative = representative
        self.residences = residences

    def write_to_csv(self):
        fieldnames = ['Street Name', 'Representative', 'Residences']
        data = [self.street_name, self.representative, self.residences]

        with open('../data/streets.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(fieldnames)
            writer.writerow(data)

    @classmethod
    def fetch_street_by_name(cls, street_name):
        with open('../data/streets.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Street Name'] == street_name:
                    return cls(row['Street Name'], row['Representative'], row['Residences'].split(','))
        return None

    def update_representative(self, new_representative):
        self.representative = new_representative
        self.update_street_details()

    def update_street_details(self):
        streets = []
        with open('../data/streets.csv', mode='r') as file:
            reader = csv.reader(file)
            streets = [row for row in reader]

        for street in streets:
            if street[0] == self.street_name:
                street[1] = self.representative
                street[2] = ','.join(self.residences)

        with open('../data/streets.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(streets)

    def get_street_details(self):
        with open('../data/streets.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Street Name'] == self.street_name:
                    return row
        return None

    def add_residence(self, residence_id):
        residence_exists = self.validate_residence_id(residence_id)
        if residence_exists and residence_id not in self.residences:
            self.residences.append(residence_id)
            self.update_street_details()
            return True
        elif residence_id in self.residences:
            print(f"Residence {residence_id} already exists in the street.")
        else:
            return False

    def remove_residence(self, residence_id):
        if residence_id in self.residences:
            self.residences.remove(residence_id)
            self.update_street_details()
            return True
        else:
            return False

    def get_residence(self, residence_id):
        if residence_id in self.residences:
            residence_details = self.fetch_residence_details(residence_id)
            return residence_details
        else:
            print(f"Residence {residence_id} not found in the street.")

    @staticmethod
    def validate_residence_id(residence_id):
        with open('../data/residences.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Residence ID'] == residence_id:
                    return True
        return False

    @staticmethod
    def fetch_residence_details(residence_id):
        with open('../data/residences.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Residence ID'] == residence_id:
                    residence_details = {
                        'Residence ID': row['Residence ID'],
                        'Residence Type': row['Residence Type'],
                        'Occupant ID': row['Occupant ID'],
                        'Occupant Type': row['Occupant Type']
                    }
                    return residence_details
        return None

    def notify_residents(self, message):
        notification_details = {
            'Street Name': self.street_name,
            'Representative': self.representative,
            'Notification': message,
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Time': datetime.now().strftime('%H:%M:%S')
        }

        self.write_notification_to_csv(notification_details)

    @staticmethod
    def write_notification_to_csv(notification_details):
        fieldnames = ['Street Name', 'Representative', 'Notification', 'Date', 'Time']
        with open('../data/notifications.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(notification_details)

    def get_notifications(self):
        notifications = []
        with open('../data/notifications.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Street Name'] == self.street_name:
                    notifications.append(row)
        return notifications

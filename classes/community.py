import csv


class Community:
    def __init__(self, community_name, community_manager, location, streets):
        self.community_name = community_name
        self.community_manager = community_manager
        self.location = location
        self.streets = streets

    def write_to_csv(self):
        fieldnames = ['Community Name', 'Community Manager', 'Location', 'Streets']
        data = [self.community_name, self.community_manager, self.location, self.streets]

        with open('../data/communities.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(fieldnames)
            writer.writerow(data)

    @classmethod
    def fetch_community_by_name(cls, community_name):
        with open('../data/communities.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Community Name'] == community_name:
                    return cls(row['Community Name'], row['Community Manager'], row['Location'],
                               row['Streets'].split(','))
        return None

    @classmethod
    def delete_community(cls, community_name):
        communities = []
        with open('../data/communities.csv', mode='r') as file:
            reader = csv.reader(file)
            communities = [row for row in reader if row[0] != community_name]

        with open('../data/communities.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(communities)

        print(f"Community '{community_name}' deleted.")

    def get_community_details(self):
        with open('../data/communities.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Community Name'] == self.community_name:
                    return row
        return None

    def update_community_detail(self, manager, location):
        communities = []
        with open('../data/communities.csv', mode='r') as file:
            reader = csv.reader(file)
            communities = [row for row in reader]

        with open('../data/communities.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for community in communities:
                if community[0] == self.community_name:
                    community[1] = manager
                    community[2] = location
                writer.writerow(community)

    def update_community_details(self):
        communities = []
        with open('../data/communities.csv', mode='r') as file:
            reader = csv.reader(file)
            communities = [row for row in reader]

        for community in communities:
            if community[0] == self.community_name:
                community[1] = self.community_manager
                community[2] = self.location
                community[3] = ','.join(self.streets)

        with open('../data/communities.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(communities)

    def add_street(self, street_name):
        street_exists = self.validate_street(street_name)
        if street_exists and street_name not in self.streets:
            self.streets.append(street_name)
            self.update_community_details()
            return True
        elif street_name in self.streets:
            print(f"Street '{street_name}' already exists in the community.")
        else:
            return False

    def remove_street(self, street_name):
        if street_name in self.streets:
            self.streets.remove(street_name)
            self.update_community_details()
            return True
        else:
            return False

    def get_street(self, street_name):
        if street_name in self.streets:
            street_details = self.fetch_street_details(street_name)
            return street_details
        else:
            print(f"Street '{street_name}' not found in the community.")

    @staticmethod
    def validate_street(street_name):
        with open('../data/streets.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Street Name'] == street_name:
                    return True
        return False

    @staticmethod
    def fetch_street_details(street_name):
        with open('../data/streets.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Street Name'] == street_name:
                    representative = row['Representative']
                    residences = row['Residences'].split(',')
                    return {
                        'Street Name': street_name,
                        'Representative': representative,
                        'Residences': residences
                    }
        return None

    @staticmethod
    def validate_login(community_name, manager_name):
        with open('../data/communities.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Community Name'] == community_name and row['Community Manager'] == manager_name:
                    return True
        return False
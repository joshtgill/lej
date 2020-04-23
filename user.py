import uuid


class User:

    def __init__(self, email = '', password = '', firstName = '', lastName = ''):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.uuid = uuid.uuid4()


    def serialize(self):
        return { 'email': self.email, 'password': self.password, 'firstName': self.firstName, 'lastName': self.lastName }


    def deserialize(self, data):
        self.email = data['email']
        self.password = data['password']
        self.firstName = data['firstName']
        self.lastName = data['lastName']

import uuid
from structures.active_term import ActiveTerm


class User:

    def __init__(self, email = '', password = '', firstName = '', lastName = ''):
        self.uuid = uuid.uuid4()
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.activeTerm = ActiveTerm()


    def serialize(self):
        return { 'email': self.email, 'password': self.password, 'firstName': self.firstName, 'lastName': self.lastName }


    def deserialize(self, data):
        self.email = data.get('email')
        self.password = data.get('password')
        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        self.activeTerm.deserialize(data.get('activeTerm'))

class User:

    def __init__(self, uuid=None, firstName='', lastName='', email=''):
        self.uuid = uuid
        self.firstName = firstName
        self.lastName = lastName
        self.email = email


    def serialize(self):
        return {'firstName': self.firstName, 'lastName': self.lastName, 'email': self.email}


    def deserialize(self, data):
        self.uuid = data.get('uuid')
        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        self.email = data.get('email')

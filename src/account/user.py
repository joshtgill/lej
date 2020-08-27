class User:

    def __init__(self, uuid=None, firstName='', lastName='', email='', typee=-1):
        self.uuid = uuid
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.type = typee


    def serialize(self):
        return {'firstName': self.firstName, 'lastName': self.lastName, 'email': self.email, 'type': self.type}


    def deserialize(self, data):
        self.uuid = data.get('uuid')
        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        self.email = data.get('email')
        self.type = data.get('type')

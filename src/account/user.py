class User:

    def __init__(self, uuid=None, idd="", firstName='', lastName='', email='', typee=-1):
        self.uuid = uuid
        self.id = idd
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.type = typee


    def serialize(self):
        return {'id': self.id, 'firstName': self.firstName, 'lastName': self.lastName, 'email': self.email, 'type': self.type}


    def deserialize(self, uuid, data):
        self.uuid = uuid
        self.id = data.get('id')
        self.firstName = data.get('firstName')
        self.lastName = data.get('lastName')
        self.email = data.get('email')
        self.type = data.get('type')

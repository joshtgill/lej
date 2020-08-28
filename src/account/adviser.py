from account.user import User


class Adviser(User):

    def __init__(self, uuid=None, idd='', firstName='', lastName='', email='', typee=-1, undergrads=[]):
        super().__init__(uuid, idd, firstName, lastName, email, typee)
        self.undergrads = undergrads


    def serialize(self):
        data = super().serialize()
        data.update({'undergrads': self.undergrads})

        return data


    def deserialize(self, uuid, data):
        super().deserialize(uuid, data)
        self.undergrads = data.get('undergrads')

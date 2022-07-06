# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    # OK
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """

        # check if param is an Account() instance
        if not isinstance(new_account, Account):
            return False

        # check if account with that name doesn't exit
        for acc in self.accounts:
            if acc.name == new_account.name:
                # print("Account with that name alredy exists")
                return False

        self.accounts.append(new_account)

    def accIsCorrupted(self, account):

        attributes = dir(account)

        if len(attributes) % 2 == 0:
            # print("ACC CORRUPT: has an even number of attributes")
            return True

        if any(attr.startswith('b') for attr in attributes):
            # print("ACC CORRUPT: has an attribute starting with b")
            return True

        if (not any(attr.startswith('zip') for attr in attributes)
           or any(attr.startswith('addr') for attr in attributes)):
            # print("ACC CORRUPT: hasn't an attribute with zip or addr")
            return True

        if (not hasattr(account, 'name')
           or not hasattr(account, 'value')
           or not hasattr(account, 'id')):
            # print("ACC CORRUPT: missing attribute name,value or id")
            return True

        if type(getattr(account, 'name')) != str:
            # print("ACC CORRUPT: name type error")
            return True

        if type(getattr(account, 'id')) != int:
            # print("ACC CORRUPT: id type error")
            return True

        if (type(getattr(account, 'value')) != int
           and type(getattr(account, 'value')) != float):
            # print("ACC CORRUPT: value type error")
            return True

        return False

    # I had to add 0 as default value to amount
    # cuz of that specification in the subject:

    # A transfer between the same account
    # (bank.transfer('Wiliam John', 'William John')) is valid but there is
    # no fund movement.
    def transfer(self, origin, dest, amount=0):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """

        # https://stackoverflow.com/questions/19162285/get-index-in-the-list-of-objects-by-attribute-in-python
        try:
            # get the Account() concerned by the the transfer
            index = [acc.name for acc in self.accounts].index(origin)
            origin = self.accounts[index]
            index = [acc.name for acc in self.accounts].index(dest)
            dest = self.accounts[index]

            if self.accIsCorrupted(origin) or self.accIsCorrupted(dest):
                # print("One of the account is corrupted")
                return False

            if type(amount) != float and type(amount) != int:
                return False

            if amount < 0:
                # print("Negative value transfer")
                return False

            if origin.value < amount:
                # print("Account doesn't have enough money")
                return False
        except ValueError:
            return False

        # avoid to make a transfer from the same account
        if dest == origin:
            return True

        # make the transfer
        dest.transfer(amount)
        origin.transfer(-amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if type(name) != str:
            return False
        try:
            index = [acc.name for acc in self.accounts].index(name)
            account = self.accounts[index]
            attributes = dir(account)

            # remove any attributes starting with b
            for attr in attributes:
                if attr.startswith('b'):
                    delattr(account, attr)
                    # print('FIX: must remove', attr, "attribute")

            # add a zip attribute if there is no attributes
            # starting with 'addr' or 'zip'
            if (not any(attr.startswith('zip') for attr in attributes)
               and not any(attr.startswith('addr') for attr in attributes)):
                setattr(account, "zipRandom", "000-000")
                # print('FIX: add zip random attribute')

            # add random attribute to have even number of attributes
            attributes = dir(account)
            if len(attributes) % 2 == 0:
                setattr(account, "randomForOdd", 42)
                # print('FIX: add random attribute to get odd number')

            # check if account is corrupted
            # (can't recover it if still corrupted)
            if self.accIsCorrupted(account):
                return False
            return True
        except ValueError:
            return False


# in the_bank.py
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

import re


class Transaction():
    def __init__(self, dat, description, to, amount, name):
        self.date = dat
        self.description = description
        self.to = to
        self.amount = amount
        self.name = name
        self.from_ = None

    def name_to(self):
        """Куда переводим"""
        return re.sub("[^a-zA-ZА-Яа-я\s]", "", self.to)

    def number_to(self):
        """Номер счета на который переводим"""
        return re.sub("[\D]", "", self.to)


    def card_name_from(self):
        """Название карты"""
        return re.sub("[^a-zA-ZА-Яа-я\s]", "", self.from_)

    def card_number_from(self):
        """Номер карты счета с которого переводим"""
        return re.sub("[\D]", "", self.from_)


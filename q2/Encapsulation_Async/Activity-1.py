class GameCharacter:
    def __init__(self, username):
        self.username = username  # Public

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode  # Protected

class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName  # Public

class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID  # Private

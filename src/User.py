from datetime import date

class User:
    def __init__(self, name:str, email:str, dob:date, education:str, courses:list[str]):
        self.name = name
        self.email = email
        self.dob = dob
        self.education = education
        self.courses = courses
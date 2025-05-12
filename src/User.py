from datetime import date

class User:
    def __init__(
            self,
            name: str = '',
            email: str = '',
            dob: date = date(2000, 1, 1),
            education: str = '',
            courses:list[str] = ['']
    ):
        self.name = name
        self.email = email
        self.dob = dob
        self.education = education
        self.courses = courses

    def add_course(self, course:str):
        self.courses.append(course)
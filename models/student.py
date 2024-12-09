class Student:
    _id_counter = 1

    def __init__(self, name, major, year):
        self.id = Student._id_counter
        self.name = name
        self.major = major
        self.year = year
        Student._id_counter += 1

    def to_dict(self):
        """Converts the student object to a dictionary for easier rendering."""
        return {"id": self.id, "name": self.name, "major": self.major, "year": self.year}


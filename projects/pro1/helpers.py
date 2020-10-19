import logging


class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        if not [self.name, self.marks]:
            logging.warning("Student name and marks are not defined")

    def result(self):
        if self.name:
            logging.warning(self.name)
        else:
            logging.warning("The name is not provided")


s=Students("Chaithanya", "500")
s.result()

class School:
    
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
       
    def add_student(self, name, grade_number):
        if grade_number not in self.roster.keys():
            self.roster.update({grade_number : [name]})
        else:
            self.roster[grade_number].append(name)
            
    def grade(self, grade_number):
        return self.roster[grade_number]

    def sort_roster(self):
        for grade_number in self.roster:
            self.roster[grade_number].sort()
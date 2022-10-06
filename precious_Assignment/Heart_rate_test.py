class MaxiHeart:
    def __init__(self, age):
        self.age = age

    def set_age(self, age):
        if age >= 0:
            self.age = age

    def get_age(self):
        return self.age

    def get_maximum_heart_rate(self):
        return 220 - self.get_age()

    def get_target_heart_rate(self):
        return self.get_maximum_heart_rate() - 0.85

 
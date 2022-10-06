class HeartRates:
    def __init__(self, age):
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self .age

    def get_maximum_heart_rates__(self):
        return 220 - self. get_age()

    def get_target_heart_rates(self):
        heart_rate_for_50 = 50 * self.get_maximum_heart_rates__()
        heart_rate_for_85 = 85 * self.get_maximum_heart_rates__()
        return heart_rate_for_50, heart_rate_for_85






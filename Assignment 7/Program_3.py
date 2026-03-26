class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 60
        self.travelled_distance = 2000

    def acceleration(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    
    def drive(self, time_driven):
        self.travelled_distance += self.current_speed * time_driven

car = Car("ABC-123", 142)

car.drive(1.5)

print(car.travelled_distance)
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    
    def drive(self, time_driven):
        self.travelled_distance += self.current_speed * time_driven

cars = []
race_finished = 0

for i in range(1, 11):
    car = Car(f"ABC-{i}", random.randint(150, 200))
    cars.append(car)

while True:
    for car in cars:
        car.acceleration(random.randint(-10, 16))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished += 1
    if race_finished != 0:
        break

for car in cars:
    print(f"Car_num: {car.registration_number}        Car max speed: {car.max_speed}          Current_speed: {car.current_speed}        Distance: {car.travelled_distance}")
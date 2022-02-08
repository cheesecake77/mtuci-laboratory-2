import constants
print(constants.HEIGHT)
step_length = constants.HEIGHT/4 + 0.37
distance = constants.STEPS * step_length / 1000
velocity = distance / constants.TIME
calories = 0.035 * constants.WEIGHT + velocity ** 2/ constants.HEIGHT * 0.029 * constants.WEIGHT
print(f'Distance: {distance} km Calories: {calories} ccal')
if (distance < 2):
    print("Недостаточная дистанция!")
elif (distance > 2 and distance < 4):
    print("Уже лучше")
else :
    print("Норма выполнена!")

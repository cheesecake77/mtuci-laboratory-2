import constants
print(constants.HEIGHT)
step_length = constants.HEIGHT/4 + 0.37
distance = constants.STEPS * step_length / 1000
velocity = distance / constants.TIME
calories = 0.035 * constants.WEIGHT + velocity ** 2/ constants.HEIGHT * 0.029 * constants.WEIGHT
print(f'Distance: {distance} km Calories: {calories} ccal')

height = 1.75
weight = 90
steps = 1000
time = 2

step_length = height/4 + 0.37
distance = steps * step_length
velocity = distance / time
calories = 0.035*weight + velocity**2/height*0.029*weight
print(f'Distance: {distance}, Calories: {calories}')

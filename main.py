import prob_calculator as pc

hat = pc.Hat(red=5, orange=4, black=1, blue=1, pink=2, striped=9)

color,amount = hat.unpack()

print('List of balls : \n')
for i,j in zip(color,amount):
  print(i,j)

hat, \
expected_balls, \
num_balls_drawn, \
num_experiments, \
prob = pc.experiment(hat=hat, expected_balls={"red":2,"orange":3, 'striped':1}, num_balls_drawn=6, num_experiments=101)

print('\nExpected balls: ', expected_balls)
print('Number balls drawn: ', num_balls_drawn)
print('Number experiments: ', num_experiments)
print("Probability: ", prob)



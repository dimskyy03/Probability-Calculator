import copy as cp
import random as rd
# Consider using the modules imported above.

class Hat:
  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs
  
  def unpack(self):
    self.color, self.amount = zip(*self.kwargs.items())
    return self.color , self.amount
    
  def content(self):
    self.color, self.amount = zip(*self.kwargs.items())
    self.string = []
    for i in range(len(self.color)) :
        self.string += [self.color[i]] * self.amount[i]
    return self.string
  
  def draw(self,drawn):
    self.draw_color = rd.sample(self.string, k = drawn)
    return self.draw_color
  
  def remaining(self):
    for i in self.draw_color :
      self.string.remove(i)
    return self.string
  
  def __str__(self):
    return str(self.content())

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
  copied_content = cp.copy(hat.content())
  color, amount = zip(*expected_balls.items())
  if num_balls_drawn >= len(hat.content()):
    return float(1)
  expected_color = []
  draw_color = []
  for i in range(len(color)) :
    expected_color += [color[i]] * amount[i]
  for i in range(num_experiments):
      draw = rd.sample(copied_content, k =num_balls_drawn)
      draw_color.append(draw)
  
  copied_expected_color = cp.deepcopy(expected_color)
  experiment_same = 0
  same_color = list()
  for x in draw_color:
    #print('x: ',x)
    for y in x :
      if y in copied_expected_color:
        copied_expected_color.remove(y)
        same_color.append(y)
        if len(same_color) == sum(amount):
          experiment_same += 1
    copied_expected_color = cp.deepcopy(expected_color)
    same_color.clear()
  
  prob = experiment_same/num_experiments

  return hat,expected_balls,num_balls_drawn,num_experiments,prob
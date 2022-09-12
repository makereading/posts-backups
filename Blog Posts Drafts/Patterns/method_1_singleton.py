def singleton(Class): 
  instances = {} 
  def getInstances(*args, **kwargs): 
    if Class not in instances: 
      instances[Class] = Class(*args, **kwargs) 
    return instances[Class] 
  return getInstances 

@singleton
class Test:
  def __init__(self):
    self.val = 10

obj1 = Test()
print(obj1.val)
obj1.val = 30

obj2 = Test()
print(obj2.val)
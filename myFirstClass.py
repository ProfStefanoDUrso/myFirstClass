class myFirstClass: 

  # only one costructor is allowed; it is possible to specify default values to "simulate" other ones
  def __init__(self, name='test', value=1): 
    self.name=name
    self.value=value

  # in order to use functions as class method, please specify "self"
  def setName(self,name):
    self.name=name;

  def setValue(self,value):
    self.value=value;

  def print(self):
    print("name is: "+self.name+" - my value is: "+str(self.value))
  
  def print_static():
    print("simulation of static function")
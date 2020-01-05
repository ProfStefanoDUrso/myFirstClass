from myFirstClass import myFirstClass

def test_main():
  print("hello")
  instance=myFirstClass()
  instance.print()
  instance=myFirstClass('stefano',0)
  instance.print()
  myFirstClass.print_static()
  print("good bye")

test_main()
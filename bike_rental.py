# 1. display available bikes
# 2. Request a bike for rent(100/- = 1qty)
# 3. exit

class Rent:
    def bikes(self):
        while True:
          choice=int(input("""
        1. Display available bikes
        2. Request a bike for rent(100/- = 1qty)
        3. Exit
        """))
          if choice == 1:
            print("Available bikes are:-", 1000)
          elif choice == 2:
            request=int(input("How many bikes you need or rent:=-"))
            print("you requested: ", request)
            print("available stocks left:--", 1000-request)
            print("1 unit price =", 100)
            print("you need to pay:", request * 100)
            #    if request >= 1000:
            #      print("sorry, available bikes are 1000")
            #      request = int(input("How many bikes you need or rent:=-"))
            #      print("you need to pay:",request*100)
            #    else:
            #      print("wrong input")

          elif choice!=1 and choice!=2 and choice!=3:
            print("wrong choice")
          else:
            print("")
            break

obj=Rent()
obj.bikes()
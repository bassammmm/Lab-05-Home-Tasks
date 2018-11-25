print("Muhammad Bassam")
print("18B-077-CS(A)")
print("Lab - 05")
print("Home Task - 6\n\n")

def first_law_motion():
    print("\nFirst Law Of Motion")
    print("Newton's first law is the law of inertia. It states that any object at rest or in motion will remain at rest or in motion unless acted upon by another force.")
    user_input()
def second_law_motion():
    print("\nSecond Law Of Motion")
    print("Newton's second law of motion pertains to the behavior of objects for which all existing forces are not balanced. The second law states that the acceleration of an object is dependent upon two variables - the net force acting upon the object and the mass of the object.")
    mass = float(input("To calculate the force enter these values:-\nMass        :"))
    acc  = float(input("Acceleration:"))
    force = mass*acc
    print("\nThe Force according to second law of motion is :{0:.1f}".format(force))
    user_input()
def third_law_motion():
    print("\nThird Law Of Motion")
    print("The third law states that for every action (force) in nature there is an equal and opposite reaction. In other words, if object A exerts a force on object B, then object B also exerts an equal and opposite force on object A. Notice that the forces are exerted on different objects.")
    force_1 = int(input("Please enter the force to calculate the resultant force :"))
    print("The resultant force is : -",force_1)
    user_input()
print("\n\nNEWTONS 3 Laws of Motion")
def user_input():
    user = input("\n\nWhich law do you want to learn? (enter only 'first','second','third' or 'end') : ")
    user = user.casefold()
    while user!='first' and user!='second' and user!='third' and user!='end':
        print("\nPlease only enter 'first','second','third' or 'end'!")
        user = input("Which law do you want to learn? (enter only 'first','second','third' or 'end') : ")
    else:
        if user=='first':
            first_law_motion()
        elif user=='second':
            second_law_motion()
        elif user=='third':
            third_law_motion()
        else:
            print("Thank you")

user_input()

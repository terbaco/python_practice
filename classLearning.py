class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.running = False
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name.title())
        print("It's type is " + self.cuisine_type)

    def open_status(self):
        if self.running == True:
            print("The restaurant is opening")
        else:
            print("The restaurant is closed")

    def close_restaurant(self):
        self.running == False

    def open_restaurant(self):
        self.running = True

    def set_number_served(self, number):
        if number < self.number_served:
            print("You can't decrease the number of served!")
        else:
            self.number_served = number
        print("Served " + str(self.number_served) + " peoples")

    def increase_number_served(self, number):
        self.number_served += number



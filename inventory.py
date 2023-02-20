#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''Prints the cost of the shoes multiplied by the quantity.'''
        return self.cost

    def get_quantity(self):
        '''Returns the quantity of the shoes.'''
        return self.quantity

    def __str__(self):
        '''Returns a string representation of a class.'''
        class_string = f'''Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}'''
        return class_string

#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inventory:
            # Skips header line in inventory.txt
            next(inventory)
            # Separate lines in txt file
            inventory_data = (inventory.read().splitlines(keepends=True))
            for line in inventory_data:
                # Seperate each word into a list using .split()
                separated_inventory = line.split(',')
                # Store all shoe data as objects of class Shoe
                shoe_list.append(Shoe(
                    separated_inventory[0],
                    separated_inventory[1],
                    separated_inventory[2],
                    separated_inventory[3],
                    separated_inventory[4],))
    except FileNotFoundError:
        # Create file if it does not exist
        inventory = open('inventory.txt', 'w+')
        inventory.close()

def capture_shoes():
    '''
    This function requests for the user to enter the necessary
    information to add a new shoe to the inventory and then
    adds the item to the inventory.
    '''
    country = input('Enter the shoes country: ')
    code = input('Enter the shoes code: ')
    product = input('Enter the product name: ')
    cost = input('Enter the price of the shoe: ')
    quantity = input('Enter the quantity of shoes: ')
    # Creates a new Shoe object and adds it to shoe_list
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    # Adds new shoe object to the end of inventory.txt
    with open('inventory.txt', 'a+') as inventory:
        inventory.write(f'\n{country},{code},{product},{cost},{quantity}')
    print('New product successfully added.')

def view_all():
    '''Prints the details of the shoes returned from the __str__ function'''
    for i in range(0, len(shoe_list)):
        print(shoe_list[i])

def re_stock():
    '''
    This function displays the product with the least stock
    then allows the user to enter a new amount of stock.
    '''
    shoe_quantity = []
    # Adds all quantities to a new list shoe_quantity
    for i in shoe_list:
        shoe_quantity.append(int(i.quantity.strip('\n')))
    # Finds and stores index of the smallest quantity into variable location
    location = shoe_quantity.index(min(shoe_quantity))
    # Call the object witht the smallest quantities index and displays its information
    print(shoe_list[location].product, 'has stock the least stock\nCurrent stock:', shoe_list[location].quantity.strip('\n'))
    while True:
        # Allows user to input a new quantity for the shoes with the lowest quantity
        add_stock_confirmation = input('Would you like to update the quantity? ').lower()
        if add_stock_confirmation == 'yes':
            try:
                add_quantity = int(input('Please enter the new amount of stock: '))
                shoe_list[location].quantity = str(add_quantity) + '\n'
                with open('inventory.txt', 'w') as inventory:
                    inventory.write('Country,Code,Product,Cost,Quantity\n')
                    for i in shoe_list:
                        inventory.write(f'{i.country},{i.code},{i.product},{i.cost},{i.quantity}')
                break
            except ValueError:
                print('Please enter a valid number')
        # Return user to menu
        elif add_stock_confirmation == 'no':
            break
        # Tells user the valid inputs and allows user to reenter input
        else:
            print('Please enter either yes or no.')
    
    # Adds the header to inventory.txt and overwrites the file

    # Success message if user chose to add stock otherwise returns to menu
    if add_stock_confirmation == 'yes':
        print('\nQuantity successfully updated.\n')

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code_list = []
    while True:
        try:
            product_code = input('Please input the product code or -1 to return to menu: ').upper()
            # Give user option to exit back to menu if they do not have a valid code
            if product_code == '-1':
                break
            else:
                # Adds all objects to code_list and searches for index of inputted product code if there is a match
                # then prints the details of that Shoe object.
                for i in shoe_list:
                    code_list.append(i.code)
                location = code_list.index(product_code)
                print(f'\nProduct details:\n{shoe_list[location]}')
                break
        except ValueError:
            # Error message if code is invalid. Allows user to reenter input
            print(f'Item with code {product_code} not found.')

def value_per_item():
    '''This function calculates the total value for each item.'''
    for i in shoe_list:
        cost = i.get_cost()
        quantity = i.get_quantity()
        value = int(cost)*int(quantity)
        print(f'The product {i.product} has a value of £{value}')


def highest_qty():
    '''
    Function determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''
    # Stores all quantities then looks for the highest quantity using max() and prints that this item is for sale
    shoe_quantity = []
    for i in shoe_list:
        shoe_quantity.append(int(i.quantity.strip('\n')))
    location = shoe_quantity.index(max(shoe_quantity))
    print(f'\n{shoe_list[location].product} is for sale\n')

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    # Function stores information from inventory.txt into objects and stores in shoe_list
    read_shoes_data()
    menu = input('''Choose one of the following options:
s - Search product by code
lq - Displays the product with the lowest stock and allows user to restock it
hq - Displays the product with the highesy quantity of stock
v - Calculate the total value of each stock item and displays them all
e - exit menu
''').lower()
    if menu == 's':
        search_shoe()
    
    elif menu == 'lq':
        re_stock()

    elif menu == 'hq':
        highest_qty()

    elif menu == 'v':
        value_per_item()

    elif menu == 'e':
        print('\nMenu closed\n')
        break

    else:
        print('\nInvalid choice. Try again.\n')
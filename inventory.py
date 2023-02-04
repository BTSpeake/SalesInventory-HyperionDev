import os.path

shoe_list = []

# Set up formatting for tabular prints
headings = ["Country", "Code", "Product", "Cost", "Quantity"]
rules = ["-"*10, "-"*20, "-"*8, "-"*15]
headingStr  = "\n{0[0]:15s} {0[1]:10s} {0[2]:20s} {0[3]:8s} {0[4]:10s}".format(headings)
rulesStr    = "{0[3]} {0[0]} {0[1]} {0[2]} {0[0]}".format(rules)
shoeStr     = "{0:15s} {1:10s} {2:20s} {3:8.2f} {4:10d}"

class Shoe:
    def __init__(self, country : str, code : str, product : str, cost : float, quantity : int):
        """ An object for storing the stock information for a given product. """
        self.country  = country 
        self.code     = code 
        self.product  = product
        self.cost     = cost 
        self.quantity = quantity
        self.saleItem = False
        return 

    def get_cost(self):
        """ Gets the cost of the shoe. """
        return self.cost

    def get_quantity(self):
        """ Gets the quantity of shoes available. """
        return self.quantity

    def get_name(self):
        """ Gets the product name. """
        return self.product

    def get_code(self):
        """ Gets the product code. """
        return self.code
    
    def get_tot_value(self):
        """ Calculates the total value of the stock available for this item. """
        tot_val = self.cost * self.quantity 
        return tot_val

    def update_quantity(self, inpQ : int):
        """ Updates the stock quantity for the given item. """
        self.quantity += inpQ 
        return

    def __str__(self):
        """ Generates a string representation of the class. """
        return shoeStr.format(self.country, self.code, self.product, self.cost, self.quantity)

    def getSaveFormat(self):
        return f"{self.country},{self.code},{self.product},{self.cost:.2f},{self.quantity}"


def read_shoes_data(fname="inventory.txt"):
    """ Read the data from the inventory.txt file creating Shoe instances for each entry. """
    
    print(f"Reading inventory form local file: {fname}")

    # First check if the file exists 
    if not os.path.isfile(fname):
        print(f"Error: File {fname} does not exist. ")
        return

    # Read the file 
    with open(fname, 'r') as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue 
            l = line.split(',')
                        
            # Check the numeric values for this entry and if they are valid create the Shoe instance
            try:
                cost = float(l[3])
                quantity = int(l[4])
            except:
                print(f"Error in line {line_num} of file {fname}, entry will be skipped.")
            else:
                shoe_list.append(Shoe(l[0], l[1], l[2], cost, quantity))

    return

def capture_shoes():
    """ 
    Create a single new shoe instance, ensuring the inputted cost and quantity values 
    are valid numerical inputs.
    """

    # Get user input
    print("\nEnter Shoe Information: ")
    country = input("Country:  ")
    code    = input("Code:     ")
    product = input("Product:  ")
    while True:
        try:
            cost = float(input("Cost:     "))
        except:
            print("Invalid Input. Cost input must be a valid number, please try again.")
        else:
            break 
    while True:
        try:
            quantity = int(input("Quantity: "))
        except:
            print("Invalid Input. Quantity input must be a valid number, please try again.")
        else:
            break 
    
    # Create the item and print an overview of the new item
    print(f"Creating stock item for {product}.")
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("\nOverview:")
    print(shoe_list[-1].__str__())

    return 

def view_all():
    """ Generate a table of all stock items. """
    
    print(headingStr)
    print(rulesStr)
    for item in shoe_list:
        print(item.__str__())
    return

def re_stock():
    """
    Finds the product with the lowest quantity of available stock and allows the user to 
    purchase a specified amount to re-stock that item. 
    """
    # find item with lowest stock
    minQuantity = shoe_list[0].get_quantity()
    minIndex = 0
    for i, item in enumerate(shoe_list):
        if item.get_quantity() < minQuantity:
            minQuantity = item.get_quantity() 
            minIndex = i 
    print("\nThe item with the lowest stock is:")
    print("  Product: {0:s}  Quantity: {1:d}".format(shoe_list[minIndex].get_name(), shoe_list[minIndex].get_quantity()))
    
    # update the stock
    while True:
        try:
            inpQuant = int(input("\nHow much stock do you wish to purchase? "))
        except:
            print("Invalid input!")
        else:
            shoe_list[minIndex].update_quantity(inpQuant)
            break
    print("\nUpdated item stock: ")
    print("  Product: {0:s}  Quantity: {1:d}".format(shoe_list[minIndex].product, shoe_list[minIndex].get_quantity()))
    return 

def search_shoe():
    """ Gets the full stock information for a given product code. """
    
    code = input("Enter shoe code: ")
    for item in shoe_list:
        if item.code == code:
            print(headingStr + "\n" + rulesStr)
            print(item.__str__())
            break
    return

def value_per_item():
    """ Get the total stock value per item. """
    
    print("\nGetting total stock value per item in inventory. \n")
    # Print out headings 
    print("{0:10s} {1:10s}".format("Code", "Value"))
    print("{0:10s} {0:10s}".format("-"*10))
    
    # Get stock value for each item 
    for item in shoe_list:
        print("{0:10s} {1:10.2f}".format(item.get_code(), item.get_tot_value()))
    return 

def highest_qty():
    """
    Finds the product with the highest quantity of available stock and allows the user to 
    purchase a specified amount to re-stock that item. 
    """
    # find item with lowest stock
    maxQuantity = shoe_list[0].get_quantity()
    maxIndex = 0
    for i, item in enumerate(shoe_list):
        if item.get_quantity() > maxQuantity:
            maxQuantity = item.get_quantity() 
            maxIndex = i 
    print("\nThe item with the lowest stock is:")
    print("  Product: {0:s}  Quantity: {1:d}".format(shoe_list[maxIndex].get_name(), shoe_list[maxIndex].get_quantity()))

    while True:
        yn = input("Do you want to mark this as a sale item? (y/n)")
        if yn == 'y':
            shoe_list[maxIndex].saleItem = True
            print("\nThis item has now been marked as a sale item. \n")
            break 
        elif yn == 'n':
            shoe_list[maxIndex].saleItem = False
            print("Returning to main menu...")
            break 
        else:
            print("Invalid input!")
    return 

def saveInventory():

    print("\nSaving inventory data to inventory.txt")
    with open("inventory.txt", 'w') as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for item in shoe_list:
            f.write(item.getSaveFormat())
            f.write("\n")
    return



def mainMenu():
    """ Display the programs menu and allow the user to input an option. """
    while True:
        print("\nMain Menu:")
        print("----------")
        print(" 1. Append stock list from file. ")
        print(" 2. Enter new stock item. ")
        print(" 3. View all stock.")
        print(" 4. Re-stock item. ")
        print(" 5. Search for item. ")
        print(" 6. Get total stock value. ")
        print(" 7. Create new sale item. ")
        print(" 8. Save inventory to file.")
        print(" 9. Exit. ")
        try:
            opt = int(input("Enter option: "))
        except:
            print("\nInvalid input option.")
            print("Input must be a number. ")
            continue 
        
        # process the options
        if opt == 1:
            read_shoes_data(input("Path to file: ")) 
        elif opt == 2:
            capture_shoes() 
        elif opt == 3:
            view_all() 
        elif opt == 4: 
            re_stock() 
        elif opt == 5:
            search_shoe()
        elif opt == 6:
            value_per_item() 
        elif opt == 7:
            highest_qty() 
        elif opt == 8:
            saveInventory()
        elif opt == 9:
            break
    return 


if __name__ == "__main__":
    print("Running Inventory Program...\n")
    read_shoes_data() 
    mainMenu() 
    print("Exiting Inventory Program...")
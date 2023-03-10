# SalesInventory-HyperionDev
HyperionDev software developer bootcamp task to create a sales inventory manager program. 
This program simulates a shoe stores inventory and allows a user to interact with it. 

## Running the Program
This program is written entirely in python and requires a valid python environment to run, preferably python 3 or above.
It provides only a text based command line interface, so requires a terminal to run.
It can be downloaded from GitHub and run through the command line with;
    
```
python inventory.py
```

Once run the program will display the following menu.

```
Main Menu:
----------
 1. Append stock list from file.
 2. Enter new stock item.
 3. View all stock.
 4. Re-stock item.
 5. Search for item.
 6. Get total stock value.
 7. Create new sale item.
 8. Save inventory to file.
 9. Exit.
Enter option:
```

Here the user can enter the number corresponding the the menu option they desire, enabling them to interact with the loaded inventory (default loaded from inventory.txt). The options include;

* Adding stock from a local text file.
* Adding a new stock item directly by hand.
* View the full inventory list. 
* Update the stock quantity for the item with the lowest available stock. 
* Search for a specific item via its  product code. 
* Get the total value of the available stock per item. 
* Create a new sale item if it has excess stock. 
* Save the inventory to a text file so it can be opened and edited again. 

The inventory itself is organised and displayed in a table;

```
Country         Code       Product              Cost     Quantity
--------------- ---------- -------------------- -------- ----------
South Africa    SKU44386   Air Max 90            2300.00         20
China           SKU90000   Jordan 1              3200.00         50
Vietnam         SKU63221   Blazer                1700.00         19
```


## Credits
This program was written by Dr. Benjamin T. Speake as part of the HyperionDev software engineering bootcamp course supported by the UK department of education. 

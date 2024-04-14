from json import loads
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def save_data(json_data, delete=False):
    '''saves recived data to file'''
    if delete:
        # this part will delete the content of file if need
        with open("data.txt", 'w', encoding="utf-8") as file:
            pass

    data = str(json_data)+'\n'
    
    with open("data.txt", 'a', encoding="utf-8") as file:
        file.write(data)
        return True

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def search_data(name, password = "", admin = False):
    if not admin:
        with open("data.txt", 'r', encoding="utf-8") as file:
            for line in file.readlines():
                if name in line and password in line: # if data are found in any line
                    return line
    else:
        with open("data.txt", 'r', encoding="utf-8") as file:
            for line in file.readlines():
                if name in line : # if data are found in any line
                    return line
        return None
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def all_data():
    with open("data.txt", 'r', encoding="utf-8") as file:
        for line in file.readlines():
            try:      
                show_data(line)
                print("---")
            except (ValueError): # if a line is empty or is containing spaces it will remove them and passes
                line.strip()
                continue
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def show_data(detilas: dict, admin: bool = False ):
    '''gets details and shows it'''
    detilas = loads(detilas.replace("\'", "\""))
    print(f"   neme     : {detilas['name']}")

    if admin == True: # if an admin was requesting 
        print(f"   password : {detilas['password']}")

    print(28*"-")
    print("   products")
    if detilas['products'] != {}: # if user has products
        for pr, price in zip(detilas['products'].keys(),detilas['products'].values()):
            print("   name : %-14s | price : %-14s"%(pr,price))
    else:
        print(f"      user {detilas['name']} has no products")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def delete_data(name, password):
    '''gets details of a user and delete the data from file'''
    with open("data.txt", 'r', encoding="utf-8") as file:
        all_data = file.read() # all datas will be in all_data

    all_data = all_data.split("\n") # it will split each data as a list member and puts them in all data as a list
    all_data.pop() # it deletes the last element of list wich is a \n

    found = False # the part to remove the data wanted
    for data in all_data:
        if name in data and password in data:
            print(f"data was found\n   name : {name}\n   password : {password}")
            all_data.remove(data)
            found = True

    if found == False: # if details not found in data
        print(f"user {name} was not found to delete")
        return None

    for data in all_data:
        try:
            if all_data.index(data) == 0: # for the first element it will clear the file (opens file with w mode and closes)
                delete = True
            else:
                delete = False

            data.replace('\'','"') 
            save_data(data, delete)

        except ValueError: # if data was a space or empty. (data is missing)
            save_data("") # just save an empty character
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def add_product_to_sell(name, password, **pr_detail):
    '''it recieves the data coming from add product in command class and makes it ready to save to file'''

    with open("data.txt", 'r+', encoding="utf-8") as file:
        for line in file.readlines():
            if name in line and password in line:
                data = line # all datas are inside the data

    data = loads(data.replace("\'", '"')) # make it ready for json using
    # TODO adding the pr details wich is a dictionary as a key to the previous value of the products
    data['products'].update(pr_detail) # new product is added to list of products
    delete_data(name, password) # all previous data will be removed
    save_data(data) # new datas are saved
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def product_shower():
    '''it will show all products with name and price and maybe name of producer'''
    with open("data.txt", 'r+', encoding="utf-8") as file:
        print("   name       price      producer ") # the header of table
        print(36*"_")
        print()
        for line in file.readlines():
            data = line
            data = loads(data.replace('\'', '"'))
            prs = data['products']
            for name, price in zip(prs.keys(), prs.values()): # we will have key and value together
                print("   %-11s%-11s%-10s"%(name, price, data['name']))
    print()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def delete_all():
    '''deletes all saved data'''
    while True:
        insur = input("   are you sure? [y/n]")
        if insur == "y":
            with open("data.txt", 'w', encoding="utf-8") as file:
                    pass
            print("all data removed succesjuly")
            break
        elif insur == 'n':
            break
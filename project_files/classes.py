from project_files.functions import *

class Customer:
    '''usting this class the users can be added'''
    counter = 0
    def __init__(self, status = True) -> None:
        if status == True:self.counter += 1
        self.Name = None
        self.Pass = None
        self.saved = False
    # ------------------------------------------------------------------------------
    def register(self, name, password):
        '''a user is created by its name and password'''
        self.Name = name
        self.Pass = password
    # ------------------------------------------------------------------------------
    def gether_details(self):
        det = {
            'name': self.Name,
            'password': self.Pass,
            'products': {}
        }
        return det
    # ------------------------------------------------------------------------------
    def clear(self):
        '''when a user is created and saved it will empty the sample user object'''
        self.__init__(False)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class command:
    def __init__(self, cmd) -> None:
        self.tmp_user = Customer()
    # ------------------------------------------------------------------------------
    def register(self, cmd):
        '''recives the details and then put it in the sample object'''
        if len(cmd)<3: print(f"missing {3-len(cmd)} items (passeord or name)")
        else:
            self.tmp_user.clear()
            self.tmp_user.register(cmd[1], cmd[2])
            print(f"user {self.tmp_user.Name} succesfully created")
            if len(cmd)==4 and cmd[3]=='s': # if user wanted to save data now
                self.tmp_user.saved = True
                save_data(self.tmp_user.gether_details())
                print(f"user {self.tmp_user.Name} saved")
        return self.tmp_user
    # ------------------------------------------------------------------------------
    def admin_reg(self, cmd):
        '''the same register but for admins'''
        return self.register(cmd[1:3])
    # ------------------------------------------------------------------------------
    def show(self, cmd):
        '''it will call the show data function if details are ok then it will show its details'''
        if len(cmd)<2: print("name is missing")
        else:
            d = search_data(cmd[1], cmd[2])
            if d != None:
                show_data(d)
            else:
                print("no user or data was found")
    # ------------------------------------------------------------------------------
    def admin_show(self, cmd):
        d = search_data(cmd[2], admin=True)
        if d != None:
            show_data(d, admin=True)
        else:
            print("no user or data was found")
    # ------------------------------------------------------------------------------
    def show_all_products(self):
        product_shower()
    # ------------------------------------------------------------------------------
    def show_all(self):
        '''jusr for admin user, it will show all users'''
        all_data()
    # ------------------------------------------------------------------------------
    def save(self,cmd, tmp_user):
        '''this method saves and imports the details into a file'''
        if len(cmd)<3: print(f"missing {3-len(cmd)} items (passeord or name)")
        else: 
            if tmp_user.Name != None:
                if cmd[1] == tmp_user.Name and cmd[2] == tmp_user.Pass:
                    data = str(tmp_user.gether_details())
                    save_data(data)
                    tmp_user.clear()
                else :
                    print("unvalid information")
            else:
                print("register first")
        return tmp_user
    # ------------------------------------------------------------------------------
    def add_product(self, cmd ):
        '''this method is for adding products for a user'''
        if search_data(cmd[1], cmd[2]) == None:
            print(f"user {cmd[1]} not found , register first")
            return None
        
        data = {}
        product_name = input("   name of product:")
        while True:
            try:
                product_price = int(input("   enter price of product:"))
                break
            except:
                print("    wrong amount") # if price is not a number

        data[product_name] = product_price # TODO the key can be name and the value a list with amount like a date or ...
        add_product_to_sell(cmd[1], cmd[2], **data)
        print(f"product {product_name} added")
    # ------------------------------------------------------------------------------
    def delete(self, cmd):
        '''calls delet data function'''
        delete_data(cmd[2], cmd[3])
    # ------------------------------------------------------------------------------
    def delete_a(self):
        delete_all()
    # ------------------------------------------------------------------------------
    def help(self):
        '''shows help'''
        print("   %-15s %-20s"%("register", "reg <name> <password> [s]"))
        print(15*" ", "   <s> to save the user")
        print("   %-15s %-20s"%("new product", "add <name> <password>"))
        print("   %-15s %-20s"%("user details", "show <name> <password>"))
        print("   %-15s %-20s"%("see products", "all"))
        print("   %-15s %-20s"%("help", "help"))
        print("   %-15s %-20s"%("exit", "exit"))
        print("   %-15s %-20s"%("clear screen", "cls"))
    # ------------------------------------------------------------------------------
    def admin_help(self):
        '''shows help'''
        print("   %-15s %-20s"%("user details", "show <name>"))
        print("   %-15s %-20s"%("all suers", "showall"))
        print("   %-15s %-20s"%("delete user", "del <name> <password>"))
        print("   %-15s %-20s"%("register", "reg <name> <password> [s]"))


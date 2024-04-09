'''
the main structure is gonna be like cmd in windows or terminal in linux

<command> <input>

every command can have several parts and several inputs

after main part of project is completed I will add options to commands


this app is like a online shop , each user has a username and password , prudoctions to watch and prudoctions to sell
also wishlist and ...
let'ls start:
'''
# from sys import getsizeof as sizeof
from json import loads, load
from os import system
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Customer:
    counter = 0
    def __init__(self, status = True) -> None:
        if status == True:self.counter += 1
        self.Name = None
        self.Pass = None
        self.saved = False
    # ------------------------------------------------------------------------------
    def register(self, name, password):
        self.Name = name
        self.Pass = password
    # ------------------------------------------------------------------------------    
    def show_details(self):
        det = {'name': self.Name,}
        return det
    # ------------------------------------------------------------------------------
    def gether_details(self):
        det = {
            'name': self.Name,
            'password': self.Pass,
        }
        return det
    # ------------------------------------------------------------------------------
    def clear(self):
        self.__init__(False)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class command:
    def __init__(self, cmd) -> None:
        self.tmp_user = Customer()
    # ------------------------------------------------------------------------------
    def register(self, cmd):
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
        return self.register(cmd[1:3])
    # ------------------------------------------------------------------------------
    def show(self, cmd):
        if len(cmd)<2: print("name is missing")
        else:
            d = search_data(cmd[1], cmd[2])
            if d != None:
                show_data(d)
            else:
                print("no user or data was found")
    # ------------------------------------------------------------------------------
    def show_all(self):
        all_data()
    # ------------------------------------------------------------------------------
    def save(self,cmd, tmp_user):
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
    def delete(self, cmd):
        delete_data(cmd[2], cmd[3])
    # ------------------------------------------------------------------------------
    def help(self):
        print("%-15s %-20s"%("register", "reg <name> <password> [s]"))
        print(15*" ", "<s> to save the user")
        print("%-15s %-20s"%("user details", "show <name> <password>"))
        print("%-15s %-20s"%("help", "help"))
        print("%-15s %-20s"%("exit", "exit"))
    # ------------------------------------------------------------------------------
    def admin_help(self):
        print("%-15s %-20s"%("user details", "show <name>"))
        print("%-15s %-20s"%("all suers", "showall"))
        print("%-15s %-20s"%("register", "reg <name> <password> [s]"))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def save_data(json_data):
    data = str(json_data)+'\n'
    with open("c:\\Users\\SADAF COMPUTER\\Desktop\\data.txt", 'a', encoding="utf-8") as file:
        file.write(data)
        return True
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def search_data(name, password):
    with open("c:\\Users\\SADAF COMPUTER\\Desktop\\data.txt", 'r', encoding="utf-8") as file:
        for line in file.readlines():
            if name in line and password in line:
                return line
        return None
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def all_data():
    with open("c:\\Users\\SADAF COMPUTER\\Desktop\\data.txt", 'r', encoding="utf-8") as file:
        for line in file.readlines():
            try:      
                show_data(line)
                print("---")
            except (ValueError):
                line.strip()
                continue
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def show_data(detilas):
    detilas = loads(detilas.replace("\'", "\""))
    print(f"neme : {detilas['name']}")
    print(f"password : {detilas['password']}")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def delete_data(name, password):
    character_counter = 0
    print("I am deleting")
    with open("c:\\Users\\SADAF COMPUTER\\Desktop\\data.txt", 'r+', encoding="utf-8") as file:
        for line in file.readlines():
            print(repr(line))
            print(f"for this line chars are {character_counter}")
            if name in line and password in line:
                print(character_counter)
                file.seek(character_counter, 0)
                for __ in line:
                    file.write(" ")
            for _ in line:
                character_counter += 1
    print("deleting is finished")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def commander():
    tmp_user = Customer()
    while True:
        cmd = input(">>>").split(" ")
        cm = command(cmd)
            # ------------------------------------------------------------------------------       
        if cmd[0] != "admin" and cmd[0] != "cls":
            # ------------------------------------------------------------------------------
            if "reg" in cmd :
                tmp_user = cm.register(cmd)
            # ------------------------------------------------------------------------------
            elif "show" in cmd: # <show> <name> <password>
                cm.show(cmd)
            # ------------------------------------------------------------------------------
            elif "save" in cmd: # <save> <name> <password>
                tmp_user = cm.save(cmd, tmp_user)
            # ------------------------------------------------------------------------------
            elif "help" in cmd:
                cm.help()     
            # ------------------------------------------------------------------------------
            elif "exit" in cmd:
                break
            # ------------------------------------------------------------------------------
            else:
                print("unvalid command")
            # ------------------------------------------------------------------------------       
        elif cmd[0] == "admin":
            # ------------------------------------------------------------------------------       
            if cmd[1] == "showall":
                cm.show_all()
            # ------------------------------------------------------------------------------
            elif cmd[1] == "show": # <show> <name>
               tmp_user = cm.admin_reg(cmd) 
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "reg":
               tmp_user = cm.admin_reg(cmd) 
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "del":
                cm.delete(cmd)
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "help":
                cm.admin_help()
            #TODO:set access for admin, set more properties, design better 
        elif cmd[0] == "cls" or cmd[0] == "clear":
            system("cls")
            

if __name__ == "__main__":
    commander()
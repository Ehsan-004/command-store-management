from os import system
from project_files.classes import *

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
            elif "add" in cmd: # <add> <name> <password>
                cm.add_product(cmd)
            # ------------------------------------------------------------------------------
            elif "all" in cmd:
                cm.show_all_products()
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
               cm.admin_show(cmd) 
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "reg":
               tmp_user = cm.admin_reg(cmd) 
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "del":
                try:
                    if cmd[2] == "all":
                        cm.delete_a()
                except(IndexError):
                    cm.delete(cmd)
                    print("done")
            # ------------------------------------------------------------------------------       
            elif cmd[1] == "help":
                cm.admin_help()
            #TODO:set access for admin, set more properties, design better 
        elif cmd[0] == "cls" or cmd[0] == "clear":
            system("cls")
            

if __name__ == "__main__":
    commander()
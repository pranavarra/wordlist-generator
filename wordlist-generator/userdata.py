from functions import *

class UserData:
    def __init__(self, data=None):
        self.data = data

    def birthday_check(self):
        bd = input("Birthday (DD/MM/YYYY): ").split("/")
        
        if(len(bd) == 3 or bd == [""]):
            if(bd==[""]):
                return ""
            else:
                if((int(bd[0])<=31 and int(bd[0])>0) and (int(bd[1])<=12 and int(bd[1])>0) and (int(bd[2])<=datetime.datetime.now().year and int(bd[2]>1900))):
                    return bd
        else:
            print("Invalid birthday date format. The format of the date should be in DD/MM/YYYY.")
            self.birthday_check()

    def check_integer(self, prompt):
        input_data = input(prompt)
        try:
            return int(input_data)
        except:
            print("Invalid input. The input must be an integer.")
            self.check_integer(prompt, input(prompt))

    def remove_spaces_from_csv(self, raw_input):
        csv_data = raw_input.split(",")
        data = []
        for item in csv_data:
            data.append(item.strip())

    def add_relation(self, arr):
        relation_data = {
            'first_name':input("First Name: "),
            'last_name':input("Last Name: "),
            'birthday':self.birthday_check(),
            'keywords':self.remove_spaces_from_csv(input("Keywords (Seperate words using commas): "))
        }
        arr.append(relation_data)

    def others_data(self):
        others_data_arr = []
        print_break()
        if(boolean_check("Do you want to include any other relations?")):
            for i in range(int(self.check_integer("How many do you want to include in the wordlist? "))):
                print_break()
                print("Relation " + str(i+1) + ": ")
                self.add_relation(others_data_arr)
            return others_data_arr
        else:
            return None

    def key_relation_data(self, prompt):
        print_break()
        print(prompt + " \n")
        data = {
                'first_name':input("First Name: "),
                'last_name':input("Last Name: "),
                'birthday':self.birthday_check(),
                'keywords':self.remove_spaces_from_csv(input("Keywords (Seperate words using commas): "))
            }
        return data
    
    def save_json_file(self):
        if(boolean_check("Do you want to save the data?")):
            file = tkinter.filedialog.asksaveasfile(title="Save User Data File", initialfile="Untitled.json", defaultextension=".json", filetypes=[("Json Files", "*.json")])
            try:
                json.dump(self.data, file)
                print("User data has been successfully saved to " + file.name + ".")
            except:
                print("Error occurred while trying to save user data to json file.")
                self.save_json_file()
        else:
            return None

    def new_data(self):
        self.data = {
            'first_name':input("First Name: "),
            'middle_name':input("Middle Name: "),
            'last_name':input("Last Name: "),
            'birthday':self.birthday_check(),
            'keywords':self.remove_spaces_from_csv(input("Keywords (Seperate words using commas): ")),
            'partner_data':self.key_relation_data("Partner's Data:"),
            'child_data':self.key_relation_data("Child's Data:"),
            'others_data':self.others_data()
        }

        self.save_json_file()

        return self.data
        
    def initialize_user(self):
        return self.new_data()

    def get_user_data(self):
        return self.data
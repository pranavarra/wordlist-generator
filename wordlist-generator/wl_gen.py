import datetime
import json

print("Wordlist Generator!")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters = ["!", "@", "#", "$", "%", "&"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special_payloads = ["123", "00", "11", "!123", "@123", "#123", "&&", "!@#", "321", "@321", "!321", "abc", "xyz", "@abc", "!abc", "@xyz", "!xyz", "$123", "$321"]

payloads = special_payloads + characters + numbers

word_comb_limit = 2

yes_key = "Y"
no_key = "N"

def boolean_check(prompt):
    boolean_input = input(prompt + " [Y/N] ")
    if(boolean_input.upper() != yes_key and boolean_input.upper() != no_key):
        print("Invalid input. The input must either be a Y for Yes and N for No.")
        boolean_check(prompt)
    if(boolean_input.upper() == "Y"):
        return True
    else:
        return False
    
def print_break():
    print("\n---------------------------------------\n")

class WordListGen:
    def __init__(self):
        print("PSYCH GEN!!!")
        print("\nWelcome to psych generator!!!\n")
        self.user_data = None
        self.types = {"int":12345,"string":"abcdef","bool":True,"list":[],"dict":{}}
        modes = ["1","2","3"]
        def mode_input():
            print("Following are the available commands:\n[1] Create New Wordlist\n[2] Use Existing User Data for Wordlist\n[3]Exit")
            mode = input("Enter command number (The number corresponding to command is to the left of the command) : ")
            if(mode not in modes):
                print("Invalid mode input. Please try again with a valid input.")
                mode_input()
            else:
                if(mode == "1"):
                    print_break()
                    min = self.check_integer("Minimum word length (Default set to 1) : ")
                    max = self.check_integer("Maximum word length (Default set to 10) : ")
                    user = UserData()
                    user.initialize_user()
                    wordlist = self.wordlist_gen(user.get_user_data(), min, max)
                    file_name = input("File Name of the wordlist: ")
                    self.save_file(file_name, wordlist)
                    mode_input
                elif(mode == "2"):
                    print("To be Done")
                    #CODE HERE
                elif(mode == "3"):
                    quit()

        mode_input()

    def save_file(self, file_name, wordlist):
        if(file_name == ""):
            file_name = "Wordlist"
        try:
            with open(file_name+".txt", "w") as wordlist_file:
                for word in wordlist:
                    wordlist_file.write(word+"\n")
            
            print("Successfully saved the wordlist to " + file_name + ".txt with " + str(len(wordlist)) + " words.")
        except:
            print("Error occurred while trying save the wordlist to " + file_name + ".txt.")
            if(boolean_check("Do you want to try again?")):
                self.save_file(file_name, wordlist)
            else:
                return


    def get_words_from_data(self, dict):
        words_arr = []
        for item in dict:
            item = dict[item]
            if(type(item) == type(self.types["string"])):
                words_arr.append(item)
            elif(type(item) == type(self.types["list"])):
                words_arr += item
            elif(type(item) == type(self.types["dict"])):
                words_arr += self.get_words_from_data(item)
            elif(type(item) == type(self.types["int"])):
                words_arr.append(str(item))
        
        return words_arr

    def remove_unwanted_data(self, data):
        ndata = []
        for item in data:
            if(len(item) > 0 and item != None):
                if(item not in ndata):
                    ndata.append(item)
        return ndata
    
    def word_combinations(self, words_data):
        words_data = self.remove_unwanted_data(words_data)
        words_arr = words_data
        len_words_arr = len(words_data)
        for word_one in range(len_words_arr):
            for word_two in range(len_words_arr):
                if(words_data[word_one]!=words_data[word_two]):
                    words_arr.append(words_data[word_one]+words_data[word_two])
        
        words_arr = self.remove_unwanted_data(words_arr)
        print(words_arr)
        return words_arr
    
    def payload_combinations(self, word_combinations):
        payloads_combinations_arr = word_combinations
        for word in range(len(word_combinations)):
            for payload in range(len(payloads)):
                payloads_combinations_arr.append(word_combinations[word]+payloads[payload])
                payloads_combinations_arr.append(payloads[payload]+word_combinations[word])
        return payloads_combinations_arr

    def in_size_words(self, wordlist, min, max):
        for word in wordlist:
            if(len(word) < min or len(word) > max):
                wordlist.remove(word)
        return wordlist
    
    def wordlist_gen(self, user_data, min, max):
        if(min == None):
            min = 1
        if(max == None):
            max = 10
        
        words_data = self.get_words_from_data(user_data)
        word_combinations = self.word_combinations(words_data)
        payload_combinations = self.payload_combinations(word_combinations)
        wordlist = self.in_size_words(payload_combinations, min, max)

        return wordlist

    def check_integer(self, prompt):
        input_data = input(prompt)
        try:
            return int(input_data)
        except:
            if(input_data.strip()==""):
                return None
            else:    
                print("Invalid input. The input must be an integer.")
                self.check_integer(prompt, input(prompt))

class UserData:
    def __init__(self):
        self.yes_key = "Y"
        self.no_key = "N"

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
    
    def save_json_file(self):
        if(boolean_check("Do you want to save the data?")):
            filename = self.data['first_name'] + ".json"
            try:
                with open(filename, "w") as json_file:
                    json.dump(self.data, json_file)
                print("User data has been successfully saved to " + filename + ".")
            except:
                print("Error occurred while trying to save user data to json file.")
                self.save_json_file()
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
    
WordListGen()
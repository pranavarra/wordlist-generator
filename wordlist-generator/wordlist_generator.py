from functions import *
import userdata

class WordListGen:
    def __init__(self):
        self.user_data = None
        self.types = {"int":12345,"string":"abcdef","bool":True,"list":[],"dict":{}}
        modes = ["1","2","3"]
        def mode_input():
            print_break()
            print("Following are the available commands:\n[1] Create New Wordlist\n[2] Use Existing User Data for Wordlist\n[3] Exit")
            mode = input("Enter command number (The number corresponding to command is to the left of the command) : ")
            if(mode not in modes):
                print("Invalid mode input. Please try again with a valid input.")
                mode_input()
            else:
                if(mode == "1"):
                    print_break()
                    min = self.check_integer("Minimum word length (Default set to 1): ")
                    max = self.check_integer("Maximum word length (Default set to 10): ")
                    print_break()
                    user = userdata.UserData()
                    user.initialize_user()
                    wordlist = self.wordlist_gen(user.get_user_data(), min, max)
                    self.save_file(wordlist)
                    print_break()
                    input("Press any key to continue...")
                    mode_input()

                elif(mode == "2"):
                    file = tkinter.filedialog.askopenfile(title="Open Existing Data File")
                    data = self.existing_data(file)
                    user = userdata.UserData(data)
                    min = self.check_integer("Minimum word length (Default set to 1) : ")
                    max = self.check_integer("Maximum word length (Default set to 10) : ")
                    print_break()
                    wordlist = self.wordlist_gen(user.get_user_data(), min, max)
                    self.save_file(wordlist)
                    print_break()
                    input("Press any key to continue...")
                    mode_input()

                elif(mode == "3"):
                    quit()

        mode_input()
    
    def existing_data(self, file):
        data = json.load(file)
        return data

    def save_file(self, wordlist):
        print_break()
        input("Press any key to continue to saving the wordlist in a text file...")
        try:
            wordlist_file = tkinter.filedialog.asksaveasfile(title="Save Wordlist File", initialfile="Untitled", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

            for word in wordlist:
                wordlist_file.write(word+"\n")
            print_break()
            print("Successfully saved the wordlist to " + wordlist_file.name + " with " + str(len(wordlist)) + " words.")
        except:
            print("Error occurred while trying save the wordlist.")
            if(boolean_check("Do you want to try again?")):
                self.save_file(wordlist)
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
    
    def capitalize_string(self, words_arr):
        capitalized_arr = words_arr
        for i in range(int((len(words_arr)/2))+1):
            start = words_arr[i]
            end = words_arr[len(words_arr)-1-i]
            capitalized_arr += [start.capitalize(), start.upper(), start.lower()]
            capitalized_arr += [end.capitalize(), end.upper(), end.lower()]
        return capitalized_arr

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
        capitalized_combinations  = self.capitalize_string(payload_combinations)
        wordlist = self.in_size_words(capitalized_combinations, min, max)
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
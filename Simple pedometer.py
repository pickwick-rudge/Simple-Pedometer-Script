import os

class Day():
    #Create class constructor
    def __init__(self, steps):
        self.steps = steps

    def get_steps(self): #accessor method for steps taken
        return self.steps

    def __str__(self): #display info for both after user input
        Daily_Info = "Steps Taken: " + self.get_steps()

def steps_calculations(steps_entry):
    infile = open("number_of_steps.txt", "r")
    total_steps = infile.readline()
    total_steps = int(total_steps)

    miles = (total_steps + steps_entry)/2000
    kilometers = (total_steps + steps_entry)/1250

    print("\nYou have taken {0:,} total steps.".format(total_steps + steps_entry))
    print("That is", miles,"miles or", kilometers,"kilometers.")
    print("You were", 10000-steps_entry,"steps from your daily goal and you attained {0:.0%}".format(steps_entry/10000), "of your daily goal.")

def main():
    steps_entry = int(input("Please enter your steps today: ")) #collect steps
    daily_steps = Day(steps_entry) #return today's data with class instance
    steps_calculations(steps_entry)
    
    save_input = input("\nWould you like to save your input? ").lower()
    if save_input == 'y':
        infile = open("number_of_steps.txt", "r") #readfile
        temp_working_file = open("temp.txt", "w") #create temp file to update steps with today's count - write file

        steps = infile.readline() #read the single line of steps
        new_steps = int(steps) + steps_entry #update the steps with today's count
        temp_working_file.write(str(new_steps)) #write the new total to the temp file

        infile.close() #close both files
        temp_working_file.close()

        os.remove("number_of_steps.txt") #remove the original file
        os.rename("temp.txt", "number_of_steps.txt") #swap names with the original file

if __name__ == '__main__':
    main()

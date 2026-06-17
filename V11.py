import csv
import os

def valid_int(min_value = None, max_value = None):
    
    '''
    This function gets a min and a max value and checks the integer type value that user puts in. 
    '''
    while True:

        try:
            n = int(input())
            if min_value is not None and n < min_value :
                print(f"Value at least must be{min_value}")
                continue

            if max_value is not None and n > max_value :
                print(f"Value can't be higher than {max_value}")
                continue
            return n
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def valid_float(min_value = None, max_value = None) :
    
    '''
    This function gets a min_value and a max_value and checks the floating type value that user puts in.
    '''

    while True :

        try:
            n = float(input())
            if min_value is not None and n < min_value :
                print(f"Value at least must be {min_value}")
                continue
            if max_value is not None and n > max_value :
                print(f"Value at most must be {max_value}")
                continue
            
            return n
        
        except ValueError :
            print("Invalid input! Please enter a valid number.")

def valid_strings(min_length = None, max_length = None) :

    '''
    This function validates the string inputs by checking their length.
    '''

    while True:

        s = input().strip()

        if min_length is not None and len(s) < min_length :
            print(f"Input must at least be {min_length} characters.")
            continue

        if max_length is not None and len(s) > max_length :
            print(f"Input must at most be {max_length} characters.")
            continue

        return s

def get_name() :

    '''
    this function is for getting user's name and separating into two parts called first_name and last_name. 
    '''

    full_name = valid_strings(min_length = 3)
    parts = full_name.split()

    first_name = parts[0]
    last_name = " ".join(parts[1:]) if len(parts) > 1 else None

    user_name = {
        'first_name' : first_name.capitalize(), 
        'last_name' : last_name
    }

    return user_name

def get_age() :
    
    '''
    this function calls the function called valid_int, to get users' age and check if that is correct and saves it and returns it.
    '''

    user_age = valid_int()
    return user_age

def get_gender() :
    
    '''
    This function uses valid_strings function to get users' gender and validate it.
    The input must be only one letter long.
    '''

    while True :
        g = valid_strings(min_length = 1, max_length = 1).upper()
        
        if g in ('M', 'F') : 
            return g
        else:
            print("Invalid input! Please enter your gender only as 'F' for 'Female' and 'M' for 'Male'.")
            continue

def get_unit() :

    '''
    This function uses valid_strings function to get an accurate measurement unit from user, and like get_gender function, the only acceptable input is between 'I' and 'M'.
    '''

    while True:
        measurement_unit = valid_strings(min_length = 1, max_length = 1).upper()
        
        if measurement_unit in ('M', 'I') :

            if measurement_unit == 'M' :
                unit = 'Metric'
                return unit
            
            elif measurement_unit == 'I' :
                unit = 'Imperial'
                return unit
            
        else :
            print("Invalid input! Please enter your preferred measurement unit as 'I' for 'Imperial' or 'M' for 'Metric' measurement unit.")
            continue

def get_height(unit, part = None, foot = None) :
    
    '''
    This function receives 3 variables, measurement unit or unit as named here, and two other variables named part and foot that by default have no type or value.
    If the measurement unit is 'Metric', since it is in centi-meters, it will divide it by 100 to change it to meters and saves it as use_height;
    If the measurement unit is 'Imperial', it will separate the users' input in two different variables parts named foot and part, foot for integer part and is between 1 to 9 since no one is shorter than 1 foot and taller than 9 feet, and the variable named part is for decimal part of the users' height; then the height will be calculated and turned into inches and saved as user_height.
    '''

    if unit == 'Metric' :
        user_height = (valid_float(min_value = 1.00, max_value = 275.00)) / 100
    
    elif unit == 'Imperial' :
        
        if part == 'feet' :
            foot = valid_int(min_value = 1, max_value = 9)
            return foot
        
        elif part == 'inch' :
            inch = valid_int(min_value = 0, max_value = 11)
        
        user_height = (foot * 12) + inch
    
    return user_height

def get_weight(unit):

    '''
    This function gets users' weight based on the specified measurement unit
    '''

    if unit == 'Metric' :
        user_weight = valid_int(min_value = 1, max_value = 400)
    
    elif unit == 'Imperial' :
        user_weight = valid_int(min_value = 1, max_value = 600)
    
    return user_weight

def calc_bmi (unit, user_height, user_weight) :
    
    '''
    This function receives three variables and calculates the users' BMI score.
    '''

    if unit == 'Metric' : 
        bmi_score = user_weight / (user_height ** 2)
        final_bmi_score = round(bmi_score, 2)

    elif unit == 'Imperial' :
        bmi_score = (user_weight / ( user_height ** 2)) * 703
        final_bmi_score = round(bmi_score, 2)
    
    return final_bmi_score

def bmi_status(final_bmi_score) :

    '''
    This function categorizes the users' based on their BMI score into 5 different classes.
    '''

    if final_bmi_score < 18.5 :
        bmi_status = 'Underweight'

    elif 18.5 <= final_bmi_score < 25 :
        bmi_status = 'Normal'

    elif 25 <= final_bmi_score < 30 : 
        bmi_status = 'Overweight'
    
    elif 30 <= final_bmi_score < 35 :
        bmi_status = 'Obese'

    elif final_bmi_score >= 35 : 
        bmi_status = 'Extremely Obese'
    
    return bmi_status

def measurement_unit(unit) :
    
    '''
    a function that tells the program to show which measurement units based on the users' preferred unit.
    '''

    if unit == 'Metric' :
        return 'meters', 'kilograms'
    
    if unit == 'Imperial' :
        return 'inches', 'pounds'
    
def show_summary(user_data) :
    
    '''
    This function is for showing summery of user info, it receives a dictionary called user_data containing all the info the program has on each user.
    '''

    h,w = measurement_unit(user_data["unit"])

    print(f""" Your name was {user_data["first_name"].capitalize()} and You are {user_data["age"]} years old,
             Your preferred measurement unit was {user_data["unit"]}, your height was {user_data["height"] :.2f} {h} and your weight was {user_data["weight"] :.1f} {w}.
              Your BMI score is {user_data["bmi_score"] :.2f} and based on that you are {user_data["bmi_status"]}
            """)

def build_data_dictionary(name, age, gender, unit, height, weight, bmi_score, bmi_status) :
    
    '''
    This function receives the data user put in so far and make one dictionary containing all the info.
    '''

    user_data = {
        "first_name" : name['first_name'],
        "last_name" : name['last_name'],
        "age" : age,
        "gender" : gender,
        "unit" : unit,
        "height" : height,
        "weight" : weight,
        "bmi_score" : bmi_score,
        "bmi_status" : bmi_status
    }

    return user_data

def check_to_save(user_data) :
    
    '''
    This function asks users to check before saving their information to stop wasting space saving unwanted or wrong information.
    It will first ask users to see if they want their information saved, if yes, returns the dictionary called user_data as is, but will recall another function to ask whether the user wants to put another user info or not, and if not, it will ask to change which part of the information to change.
    '''

    while True:

        #shows the summery of the info user put in so far to check for changing or saving the data
        print("Here is your information so far:")
        show_summary(user_data)

        # asking for confirmation
        print("Does everything look okay or do you want make some changes?")
        print("Press 'Y' for saving and 'N' to make changes.")
        user_input = valid_strings(min_length = 1, max_length = 1)

        if user_input in ('Y', 'N') :
            
            if user_input == 'Y' :
                
                new_user()
                return user_data
            
            elif user_input == 'N' :
                
                choice = options()


                if choice == 0 :
                        
                    return 'restart'
                    
                elif choice == 1 :

                    print("Please enter your name:")
                    print("example : John Smith")

                    new_name = get_name()
                    user_data["first_name"] = new_name["first_name"]
                    user_data["last_name"] = new_name["last_name"]

                elif choice == 2 :

                    print("Please enter your age:")
                    print("'M' for 'Male' and 'F' for 'Female'")
                    user_data["age"] = get_age()

                elif choice == 3 :

                    print("Please choose your gender:")
                    print("Example : 26")
                    user_data["gender"] = get_gender()
                    
                elif choice == 4 :

                    print("Which measurement units do you prefer for your height & weight?")
                    print("'M' for 'Metric system(kg/m)' and 'I' for 'Imperial system(lb/ft)'")
                    print("Example : M")

                    user_data["unit"] = get_unit()
                    user_data["height"] = get_height(user_data["unit"])
                    user_data["weight"] = get_weight(user_data["unit"])
                    
                elif choice == 5 :
                        
                    user_data["height"] = get_height(user_data["unit"])
                    
                elif choice == 6 :

                    user_data["weight"] = get_weight(user_data["unit"])
                    
                if choice == 4 or choice == 5 or choice == 6 :
                        
                    new_bmi_score = calc_bmi(user_data["unit"], user_data["height"],user_data["weight"])

                    new_bmi_status = bmi_status(new_bmi_score)
                        
                    user_data["bmi_score"] = new_bmi_score
                    user_data["bmi_status"] = new_bmi_status

                    return user_data
        else :
            print("Invalid input! Please try again.")
            continue

def options() :

    '''
    This function will be called in case the user wants to change some or all of their information entered so far.
    '''

    print("Please choose one of the options: \n")
    print("Press 0 to re-enter your information")
    print("Press 1 to change your name")
    print("Press 2 to change your age")
    print("Press 3 to change your gender")
    print("Press 4 to change your preferred measurement unit")
    print("Press 5 to change your height")
    print("Press 6 to change your weight")

    option = valid_int(min_value = 0, max_value = 6)

    return option

def new_user() :

    '''
    This function asks user to check whether they want to add in another user or not.
    '''

    while True :

        print("Do you want to add another user?")
        print("Press 'Y' to add a new user and 'N' for skipping this.")

        nuser = valid_strings(min_length = 1, max_length = 1)

        if nuser in ('Y', 'N') :
            
            if nuser == 'Y' :
                
                return True
            
            elif nuser == 'N' :

                print("Alrighty! Thanks for your time so far😊")
                return False
            
        else :
            
            print("Invalid input! Please choose between 'Y' or 'N'.")
            continue

def data_file_path(filename) :

    '''
    This function has only one job, and that is to save uses' data next to the same script.
    This function receives a parameter called "filename" which is the name of the file the data will be saved on and returns the intended path for the said file.
    '''

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename)

    return file_path

def check_existence(filename) :

    '''
    This function uses built-in os module to check for existence of any file, in this case, any '.csv' file and it's size to tell this script whether to create a new file or add the data to the existing file.
    This function receives the file name and returns a boolean value.
    '''

    file_path = data_file_path(filename)
    file_existence = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    return file_existence

def dict_to_list(all_user) :

    '''
    This function receives the info as a dictionary, then saves each user as a list in a list called row, and then appends row to a list called user_info, so in other words, row1 is a user, row2 is another user and so on.
    '''

    user_info = []
    for user in all_user :

        row = [
            user["first_name"],
            user["last_name"],
            user["age"],
            user["gender"],
            user["unit"],
            user["height"],
            user["weight"],
            user["bmi_score"],
            user["bmi_status"]
        ]
        user_info.append(row)

    return user_info

def save_to_csv(all_user) :

    '''
    This function is called when the info is collected and used to save the info in a csv format file.
    '''


    full_list = dict_to_list(all_user)
    user_data = collect_latest(full_list)
    headers = ["First Name", "Last Name", "Age", "Gender", "Measurement Unit", "Height", "Weight", "BMI Score", "BMI Status"]

    filename = 'udata.csv'
    with open(data_file_path(filename), "a+", newline = "") as my_file:

        writer = csv.writer(my_file)

        if check_existence(filename) : writer.writerows(user_data)

        else :

            writer.writerow(headers)
            writer.writerows(full_list)


def collect_latest(full_list) :

    return    


def main() :
    
    all_users = []

    while True:

        # getting user's name
        print("Please enter your name:")
        print("Example : John Smith")
        user_name = get_name()

        #getting user's age
        print("Please enter your age as numbers only:")
        print("Example : 26")
        user_age = get_age()

        # asking for user's gender
        print("Please choose your gender:")
        print("Press M for Male and F for Female")
        user_gender = get_gender()

        # asking for user's preferred measurement unit
        print("Which measurement unit do you prefer for your height and weight?")
        print("M for Metric system(g/m) & I for Imperial system(lb/ft)")
        print("Example : M")
        unit = get_unit()

        # asking for user's height & weight
        if unit == 'Metric' :

            # height
            print("Please enter your height in centimeters as numbers only:")
            print("Example : 158")
            user_height = get_height(unit)

            # weight
            print("Please enter your weight in kilograms as numbers only:")
            print("Example : 65")
            user_weight = get_weight(unit)

        elif unit == 'Imperial' :

            # height
            print("Please enter the feet portion of your height as numbers:")
            print("Example : 6")
            foot = get_height(unit, part = 'feet')

            print("Please enter the remaining inches as numbers:")
            print("Example : 11")
            user_height = get_height(unit, part = 'inch', foot = foot)

            # weight
            print("Please enter your weight in pounds as numbers only:")
            print("Example : 120")
            user_weight = get_weight(unit)

        # calculating BMI score
        bmi_score = calc_bmi(unit, user_height, user_weight)

        # saving info in a dictionary
        user_data = build_data_dictionary(user_name, user_age, user_gender, unit, user_height, user_weight, bmi_score, bmi_status)

        updated_user = check_to_save(user_data)
        if user_data == 'restart' : continue

        all_users.append(updated_user)

        # saving data
        save_to_csv(all_users)

        # asking for new users if desired
        another_user = new_user()

        if another_user : continue

        else : break

    input("Press enter to exit...")


if __name__ == "__main__" :
    
    main()

import csv
import os
from typing import Dict

###############################################################################

# global dictionary

MESSAGES: Dict[str, str] = {
    'ask_name' : 'Please enter your name :',
    'example_for_name' : 'Example: John Smith',
    'ask_age' : 'Please enter your age as a number only :',
    'example_for_age' : 'Example: 26',
    'ask_gender' : 'Please select your gender :',
    'example_for_gender' : 'Choose "M" for "Male" and "F" for "Female"',
    'description_for_gender' : 'Enter "M" for Male and "F" for Female',
    'ask_measurement_unit' : 'Which measurement system do you use?', 
    'measurement_system' : '"M" for Metric system (kg/cm) and "I" for Imperial system (lb/ft) :' ,
    'ask_height_metric' : 'Please enter your height in centimeters as only a number: ',
    'example_for_height_in_metric' : 'Example: 162' , 
    'ask_weight_metric' : 'Please enter your weight in kilograms as only a number: ',
    'example_for_weight_in_metric' : 'Example: 62',
    'ask_height_imperial_feet' : 'Please enter the feet portion of your height as a number :',
    'example_for_height_in_imperial_feet' : 'Example: 6',
    'ask_height_imperial_inches' : 'Please enter the remaining inches of your height as a number :',
    'example_for_height_in_imperial_inches' : 'Example: 11',
    'ask_weight_imperial' : 'Please enter your weight in pounds as a number :',
    'example_for_weight_in_imperial' : 'Example: 92',
    'invalid_input' : 'Invalid input! Please enter a valid number',
    'summary' : 'Here is your information so far: ',
    'confirmation' : 'Does everything look good, or do you want to make some changes?',
    'confirmation_answer' : "Press 'Y' for saving and 'N' to make changes: ",
    'ask_options' : 'Please Choose one of the options below: \n',
    'option_0' : 'Press 0 to re-enter your information from scratch',
    'option_1' : 'Press 1 to change your name',
    'option_2' : 'Press 2 to change your age',
    'option_3' : 'Press 3 to change your gender',
    'option_4' : 'Press 4 to change your preferred measurement unit',
    'option_5' : 'Press 5 to change your height',
    'option_6' : 'Press 6 to change your weight',
    'option_7' : 'Press 7 to Show the summary again',
    'option_8' : 'Press 8 to exit',
    'new_user_inquiry' : 'Do you want to add another user?',
    'new_user_inquiry_input' : "Choose 'Y' to add a new user and 'N' to exit: "
}


###############################################################################

def msg(*keys: str) -> None :

    for key in keys :

        message = MESSAGES.get(key)

        if message is not None :
            print(message)
        
        else :
            
            print(f"[Warning: Message key '{key}' not found]")

def integer_validator(min_value = None, max_value = None) :
    
    '''
    This function gets a minimum and a maximum value and checks the integer values that users put in.
    The default minimum and maximum value are None.
    '''

    while True :
        
        try :
            
            n = int(input())

            if min_value is not None and n < min_value :
                
                print(f"Value must at least be {min_value}")
                continue

            if max_value is not None and n > max_value :

                print(f"Value can't be higher than {max_value}")
                continue
            
            return n
        
        except ValueError:

            msg('invalid_input')

def float_validator(min_value = None, max_value = None) :

    '''
    This function gets a minimum and a maximum value and checks the floating values that users put in.
    The default minimum and maximum value are None.
    '''

    while True :

        try :

            n = float(input())
            if min_value is not None and n < min_value :

                print(f"Value must at least be {min_value}")
                continue

            if max_value is not None and n > max_value :
                
                print(f"Value can't be higher than {max_value}")
                continue

            return n

        except ValueError :
            
            msg('invalid_input')

def string_validator(min_length = None, max_length = None, valid_values=None, case_sensitive=False) :

    '''
    This function is used to validate strings. If asked about name, minimum and maximum length of input should be entered, an the other variables would have their default value.
    variable named case_sensitive would be false by default, but for name inputs, it will have a value of True.
    valid_values variable will have values only when there are options to choose from.
    '''

    while True :

        s = input().strip()

        if not case_sensitive:

            s = s.lower()

        if min_length is not None and len(s) < min_length :

            print(f"Input must be at least {min_length} characters.")
            continue

        if max_length is not None and len(s) > max_length :
            print(f"Input must be at most {max_length} characters.")
            continue

        if valid_values is not None and s not in valid_values :

            if len(valid_values) == 1 :

                valid_options = valid_values[0]
            
            elif len(valid_values) == 2 :

                valid_options = " or ".join(valid_values)
            
            else :

                valid_options = ", ".join(valid_values[:-1]) + f" or {valid_values[-1]}"

            print(f"Invalid input! Your input should be from {valid_options}")
            continue

        return s

def get_name(user) :

    '''
    This function receives an empty dictionary, then using sting_validation function checks the input, then if it's the correct input, will assign the first part of the name to the variable called first_name and other parts to variable called last_name, and save them in the dictionary.
    '''

    full_name = string_validator(min_length = 3, case_sensitive = True)
    parts = full_name.split()

    first_name = parts[0]
    last_name = " ".join(parts[1:]) if len(parts) > 1 else None

    first_name = first_name.lower().title()
    last_name = last_name.lower().title()

    user['first_name'] = first_name
    user['last_name'] = last_name

def get_age(user) :

    '''
    Simple function. receives a dictionary, gets use's age by calling integer_validator function, and saves it in the dictionary called user
    '''

    user['age'] = integer_validator(min_value = 1, max_value = 120)

def get_gender(user) -> None :

    '''
    This function receives a dictionary, calls the functon string_validator with a minimum and maximum length of 1, and valid_values = ['M' , 'F'] and then saves it in the dictionary.
    '''


    g = string_validator(min_length = 1, max_length = 1, valid_values = ['m', 'f'])

    if g == 'm' :
        
        gender = 'Male'
    
    elif g == 'f' :
        
        gender = 'Female'


    user['gender'] = gender

def get_unit(user) -> None :

    '''
    This function receives a dictionary, calls the functon string_validator with a minimum and maximum length of 1, and valid_values = ['M' , 'I'] and then saves it in the dictionary.
    '''

    u = string_validator(min_length = 1, max_length = 1, valid_values =['m', 'i'])
    
    if u == 'm' :

        system = 'Metric'
    
    elif u == 'i' :

        system = 'Imperial'

    user['system'] = system

def height_converter(user, **height) -> None:

    if user['system'] == 'Metric' :

        new_height = height['cm'] / 100
        

    elif user['system'] == 'Imperial' :

        nheight = (height['feet'] * 12) + height['inches']
        height_in_cm = nheight * 2.54
        
        new_height = height_in_cm / 100
    # height is in meters
    user['height'] = {
        'value' : round(new_height, 2),
        'unit' : 'meters'
    }

def get_height(user) -> None:

    if user['system'] == 'Metric' :

        msg('ask_height_metric', 'example_for_height_in_metric')
        height = float_validator(min_value = 1.00, max_value = 275.00)
        height_converter(user, cm = height)
        user['initial_height'] = {
            'cm' : height
        }
    
    elif user['system'] == 'Imperial' :

            
            msg('ask_height_imperial_feet', 'example_for_height_in_imperial_feet')
            height_feet = integer_validator(min_value = 1, max_value = 9)

            msg('ask_height_imperial_inches', 'example_for_height_in_imperial_inches')
            height_inches = integer_validator(min_value = 0, max_value = 11)
            user['initial_height'] = {
            'feet' : height_feet,
            'inches' : height_inches
        }

            height_converter(user, feet = height_feet, inches = height_inches)

def get_weight(user) -> None:

    '''
    This funtion asks for weight according to measurement system. if the measurement system is metric, asks for weight in kilograms and saves it, if it is imperial, sends the weight to another function to convert it to kilograms and saves it.
    '''

    if user['system'] == 'Metric' :
        
        msg('ask_weight_metric', 'example_for_weight_in_metric')
        final_weight = float_validator(min_value = 1.00, max_value = 400.00)
        user['initial_weight'] = {
            'kg' : final_weight
        }
    
    elif user['system'] == 'Imperial' :

        msg('ask_weight_imperial', 'example_for_weight_in_imperial')
        weight = float_validator(min_value = 1.00, max_value = 600.00)
        final_weight = weight_converter(weight)
        user['initial_weight'] = {
            'lb' : weight
        }
    
    # weight is in kilograms
    user['weight'] = {
        'value' : final_weight,
        'unit' : 'kilograms'
        }

def weight_converter(weight) -> float:

    '''
    This functions receives a variable called weight which is in pounds, converts it to kilograns and returns it.
    '''
    # weight is in kilograms
    weight_in_metric = weight * 0.45359237

    return round(weight_in_metric, 2)

def bmi_calculator(user) -> None:

    '''
    This function calculates BMI and saves it in the dict called user.
    '''

    bmi_score = user['weight']['value'] / (user['height']['value'] ** 2)

    user['bmi_score'] = round(bmi_score, 2)

def bmi_status(user) -> None:

    '''
    simple function to save the bmi status of the user based on their bmi
    '''

    if user['bmi_score'] < 18.5 :
        
        user['bmi_status'] = "Underweight"

    elif 18.5 <= user['bmi_score'] < 25 :

        user['bmi_status'] = "Normal"
    
    elif 25 <= user['bmi_score'] < 30 :

        user['bmi_status'] = "Overweight"
    
    elif 30 <= user['bmi_score'] < 35 :

        user['bmi_status'] = "Obese"
    
    elif  user['bmi_score'] >= 35 :

        user['bmi_status'] = "Extremely Obese"

def user_builder(users) -> None:

       # getting user's name
        msg('ask_name', 'example_for_name')
        get_name(users)

        # getting user's age
        msg('ask_age', 'example_for_age')
        get_age(users)

        # asking for user's gender
        msg('ask_gender', 'example_for_gender')
        get_gender(users)

        # asking for user's preferred measurement system
        msg('ask_measurement_unit', 'measurement_system')
        get_unit(users)

        # asking for height and weight based on preferred measuremnet system

        # height
        get_height(users)

        # weight
        get_weight(users)

        # bmi calculation
        bmi_calculator(users)

        # determining bmi status
        bmi_status(users)

def show_summary(user, units) -> None:

    '''
    a simple function, called before saving a user in all_users list.
    '''

    if user['system'] == 'Metric' :

        height_text = f"{user['initial_height']['cm']} {units['unit_for_height']['unit']}"
        weight_text = f"{user['initial_weight']['kg']} {units['unit_for_weight']}"
    
    elif user['system'] == 'Imperial' :

        height_text = f"{user['initial_height']['feet']} {units['unit_for_height']['feet']} {user['initial_height']['inches']} {units['unit_for_height']['inches']}"
        weight_text = f"{user['initial_weight']['lb']} {units['unit_for_weight']}"


    print(f"""           Your name is {user['first_name']} and you are {user['age']} years old;
           Your preferred measurement system is {user['system']}, your height is {height_text} and your weight is {weight_text}.
           Your BMI score is {user['bmi_score']: .2f} and based on that you are {user['bmi_status']}.
""")

def check_system(users) -> dict:

    if users['system'] == 'Metric' :

        units = {
            'unit_for_height' : {'unit' : 'centimeters'},
            'unit_for_weight' : 'kilograms'
        }
    
    elif users['system'] == 'Imperial' :

        units = {
            'unit_for_height' : {
                'feet' : 'ft',
                'inches' : 'inches'
            },
            'unit_for_weight' : 'pounds'
        }
    return units

def check_to_save(users) -> str:

    units = check_system(users)

    # showing the summary of collected data so far
    msg('summary')
    show_summary(users, units)

    # asking for confirmation
    msg('confirmation', 'confirmation_answer')

    answer = string_validator(min_length = 1, max_length = 1, valid_values = ['y', 'n'])
    answer = answer.capitalize()

    if answer == 'Y' :

        return 'Yes'
    
    elif answer == 'N' :
        return 'No'

def process_user_decision(answer) -> bool:


    if answer == 'Yes' :

        return True
        
    elif answer == 'No' :
            
        return False

def change_information(users) -> None:

    while True :

        choice = choices()

        if choice == 0 :

            user_builder(users)
            
        elif choice == 1 :

            msg('ask_name', 'example_for_name')
            get_name(users)
            
        elif choice == 2 :

            msg('ask_age', 'example_for_age')
            get_age(users)
            
        elif choice == 3 :

            msg('ask_gender', 'example_for_gender')
            get_gender(users)
            
        elif choice == 4 :

            msg('ask_measurement_unit', 'measurement_system')
            get_unit(users)
            get_height(users)
            get_weight(users)
            
        elif choice == 5 :

            get_height(users)
            
        elif choice == 6 :

            get_weight(users)

        elif choice == 7 :

            return
        

        if choice == 4 or choice == 5 or choice == 6 :

            bmi_calculator(users)
            bmi_status(users)

        elif choice == 8 :

            break

def id_assigner(users, current_id = None) -> None:

    # temporary value for current_id will be 0
    if current_id is None :

        current_id = 0

    users['id'] = current_id + 1

def save_users(all_users, users) -> None :

    all_users.append(users)

def choices() -> int:

    msg('ask_options')
    msg('option_0', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'option_6', 'option_7', 'option_8')

    option = integer_validator(min_value = 0, max_value = 8)

    return option

def data_manager(all_users, users, current_id) -> bool :

    while True :

        # validating the collected data
        answer = check_to_save(users)

        # checking for the outcome and saving
        decision = process_user_decision(answer)

        if decision :
            
            #assigning id
            id_assigner(users, current_id)
            current_id += 1

            # saving the user in the list
            save_users(all_users, users)

            return True

        elif not decision :

            change_information(users)

            continue

def id_collecter(filename) -> list:

    id_list = []

    with open(filename, 'r', newline="", encoding="utf-8") as my_file:

        reader = csv.DictReader(my_file)

        for row in reader :

            if "id" in row : id_list.append(int(row['id']))
        
    return id_list


def collecter(users) -> list:

    csv_ready_data = []
    processed_data = []

    processed_data = [
        users['id'],
        users['first_name'],
        users['last_name'],
        users['age'],
        users['gender'],
        users['system'],
        users['height']['value'],
        users['weight']['value'],
        users['bmi_score'],
        users['bmi_status']
    ]

    csv_ready_data.append(processed_data)
    
    return csv_ready_data

def csv_users(csv_ready_data) -> list:

    user_list = []


    for key in csv_ready_data :
        user_data = {}

        user_data['id'] = key[0]
        user_data['first_name'] = key[1]
        user_data['last_name'] = key[2]
        user_data['age'] = key[3]
        user_data['gender'] = key[4]
        user_data['measurement_system'] = key[5]
        user_data['height_m'] = key[6]
        user_data['weight_kg'] = key[7]
        user_data['bmi_score'] = key[8]
        user_data['bmi_status'] = key[9]

        user_list.append(user_data)

    return user_list

def data_file_path(filename) -> str:

    '''
    This function receives the name of the file that the data will be saved on, then checks where the python script os being saved and save the file in the same directory.
    '''

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename)

    return file_path

def check_existence(filename) -> bool:

    '''
    This function receives the name of the file that the data is going to be saved on, and checks whether it already exists or not, and if it exists, whether it is empty or already has data stored in it.
    '''

    file_path = data_file_path(filename)
    file_existence = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    return file_existence

def save_to_csv_manager(users, filename) :


    keys = ['id', 'first_name', 'last_name', 'age', 'gender', 'measurement_system', 'height_m', 'weight_kg', 'bmi_score', 'bmi_status']
    headers = ['ID', 'First Name', 'Last Name', 'Age', 'Gender', 'Measurement System', 'Height in Meters', 'Weight in Kilograms', 'BMI Score', 'BMI Status']

    # collecting needed data from the users dictionary
    csv_ready_data = collecter(users)

    # making a list of dictionaries with the processed data
    csv_data = csv_users(csv_ready_data)

    # checking the existence of the file and whether it is empty or not
    existence = check_existence(filename)
    
    with open(data_file_path(filename), "a+", newline = "") as my_file :
        
        writer = csv.DictWriter(my_file, fieldnames = keys)

        if existence : writer.writerows(csv_data)

        else :

            writer.writerow(dict(zip(keys, headers)))
            writer.writerows(csv_data)

def new_user() -> bool :

    msg('new_user_inquiry', 'new_user_inquiry_input')

    inquiry = string_validator(min_length = 1, max_length = 1, valid_values = ['y', 'n'])

    if inquiry == 'y' :

        return True
    
    elif inquiry == 'n' :

        return False

def main() :

    all_users = []
    
    filename = 'udata.csv'
    

    if check_existence(filename) : 

        ids = id_collecter(filename)

        current_id = max(ids) if ids else 0
    
    else : 

        current_id = 0
    
    if not current_id :

        current_id = 0

    


    while True :

        users = {}
        
        # collecting data from user
        user_builder(users)

        # checking, changing and saving the collected data
        if data_manager(all_users, users, current_id) :

            # saving the completed user in the csv file
            save_to_csv_manager(users, filename)
        
        # user is asked about creation of a new entry
        if new_user() :

            continue
        
        else :
        
            break

    
    input("Press Enter to exit...")
 
        




if __name__ == "__main__" :
    
    main()

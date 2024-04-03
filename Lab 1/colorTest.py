import random 
import time

# ansi escape codes for text color
COLOR_RED = '\033[91m'  
COLOR_GREEN = '\033[92m'  
COLOR_BLUE = '\033[94m'  
COLOR_YELLOW = '\033[93m'  
COLOR_END = '\033[0m'  

def test():
    colors = ['RED', "GREEN", "BLUE", 'YELLOW']
    color_codes = [COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_YELLOW]
    num_trial = 5
    num_answer = 0
    print('~~~~~Welcome! ~~~~~ :')
    print('Write the color of the text')

    for trial in range(num_trial):
        word = random.choice(colors)
        ink_color = random.choice(colors)
        inc_color_code = color_codes[colors.index(ink_color)]

        print(inc_color_code + word)
        print(COLOR_END)

        start_time = time.time()  # Start time
        user_resp = input('What is the text color? ').strip().upper()
        end_time = time.time()  # End time

        interval = end_time - start_time  # Calculate the interval

        if user_resp == ink_color:
            print('Correct!')
            print('Response Time:', interval, 'seconds')

        else:
            print('Incorrect')
            print('Response Time:', interval, 'seconds')

test()

import random 
import time
import threading

def user_input(prompt, user_resp):
    user_resp.append(input(prompt).strip().upper())

def test():
    directions = {'LEFT': '<----', 'RIGHT': '---->'}
    num_trials = 5
    correct_answers = 0
    print('Welcome:')
    print('Determine the direction of the middle arrow (LEFT or RIGHT)')

    for trial in range(num_trials):
        arrows = []
        for _ in range(5):
            arrow_direction = random.choice(['LEFT', 'RIGHT'])
            arrows.append(directions[arrow_direction])

        print('Arrows:', ' '.join(arrows))
        
        start_time = time.time()  # Start time
        user_resp = []
        thread = threading.Thread(target=user_input, args=("What is the direction of the middle arrow? ", user_resp))
        thread.start()

        user_input_received = False
        while time.time() - start_time < 3:  # Check if 3 seconds have not elapsed
            if thread.is_alive():
                time.sleep(0.1)  # Sleep briefly to avoid busy-waiting
            else:
                user_input_received = True
                break
        
        if not user_input_received:
            print('Time out! Moving to the next question.')
            continue
        
        if user_resp and user_resp[0] in directions and directions[user_resp[0]] == arrows[2]:
            print('Correct!')
            correct_answers += 1
        elif user_resp:
            print('Incorrect')
        else:
            print('No response')
    
    print('Test completed.')
    print('Total score:', correct_answers, 'out of', num_trials)

test()

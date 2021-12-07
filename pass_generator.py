import random
import time
import enlighten

banner = """

╭━━━┳━━━┳━━━┳━━━┳╮╭╮╭┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃
┃╰━╯┃┃╱┃┃╰━━┫╰━━┫┃┃┃┃┃┃╱┃┃╰━╯┃┃┃┃┃
┃╭━━┫╰━╯┣━━╮┣━━╮┃╰╯╰╯┃┃╱┃┃╭╮╭╯┃┃┃┃
┃┃╱╱┃╭━╮┃╰━╯┃╰━╯┣╮╭╮╭┫╰━╯┃┃┃╰┳╯╰╯┃
╰╯╱╱╰╯╱╰┻━━━┻━━━╯╰╯╰╯╰━━━┻╯╰━┻━━━╯
Generator By: Nemo
Discord: Nemo#1819
Github: xNEMOx
"""

print(banner)
pas_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@']

tlmn = input('Type F to generate password: ')
tlmns = input('How many digits: ')

# fake loading thing
if tlmn == 'f' or 'F':
    pbar = enlighten.Counter(total=100, desc='Generating', unit='ticks')
    for num in range(100):
        time.sleep(0.03)  # Simulate work
        pbar.update()
    print("\033[1m" + 'Choosing numbers [             0%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing numbers [=           10%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing numbers [==          20%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing letters [===         30%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing letters [====        40%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing numbers [=====       50%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing numbers [======      60%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Choosing numbers [=======     70%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Completing w8w8w [========    80%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Nearly done wait [=========   90%]' + "\033[0m")
    time.sleep(0.1)
    print("\033[1m" + 'Success DONE!    [========== 100%]' + "\033[0m")
    time.sleep(0.1)
    print(''.join(random.sample(pas_letters, int(tlmns))))


    # python3 pass_generator.py

    

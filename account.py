import os
import csv
import pwinput
import time
from login import *


is_exit = False
main_input = ''

def main():
    clear()
    print('[1] Register')
    print('[2] Login')
    print('[3] Logout')
    print('[4] Reset Password')
    global main_input
    main_input = input('Pick: ')
    is_exit=False

    while is_exit == False:
        if main_input == '1':
            clear()
            register()
            main()
        if main_input == '2':
            clear()
            login()
        if main_input == '3':
            clear()
            logout()
            main()
        if main_input == '4':
            clear()
            reset_password()
            main()

        return True

def register():
    print('Register')
    username = input('Enter username: ')
    password = pwinput.pwinput(prompt='Enter password: ', mask = '*')
    with open('database.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([username, password])
    return True

def logout():
    return True

def reset_password():
    print('Reset Password')
    print('Login First')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        counter = 0
        index = None
        new_list = []
        for row in reader:
            new_list.append(row)
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
                    index = counter
            counter += 1

        if is_success:
            new_password = input('New Password: ')
            for i in range(len(new_list)):
                if i == index:
                    new_list[i][1] = new_password
            with  open('database.csv', 'w+') as csv_file:
                writer = csv.writer(csv_file)
                for i in range(len(new_list)):
                    writer.writer(new_list)
            time,sleep(20)
        else:
            print('Login Failed')
        global is_exit
        global main_input
        is_exit = True

def clear():
    os.system('clear||cls')

main()
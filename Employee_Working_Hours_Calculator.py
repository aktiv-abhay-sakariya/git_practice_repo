from datetime import datetime


def calculate_employee_working_hours(login_time, logout_time):
    """
    This function calculate total working hours and minutes of employee

    Args:
        login_time (datetime) : The employee's logging time
        logout_time (datetime) : The employee's logout time

    Returns:
        total_hours (int) : total working hours
        total_minutes (int) : total working minutes
    """
    total_hours = logout_time.time().hour - login_time.time().hour
    if logout_time.time().minute >= login_time.time().minute:
        total_minutes = logout_time.time().minute - login_time.time().minute
    else:
        total_minutes = logout_time.time().minute - login_time.time().minute + 60
        total_hours -= 1
    return total_hours, total_minutes


while True:
    try:
        opening_time = input('Enter Opening time of Office (HH:MM) use 24-hour system :')
        opening_time = datetime.strptime(opening_time, "%H:%M").time()
        break
    except Exception:
        print('Enter time only (HH:MM) format')
while True:
    try:
        closing_time = input('Enter Closing time of Office (HH:MM) use 24-hour system :')
        closing_time = datetime.strptime(closing_time, "%H:%M").time()
        if opening_time >= closing_time:
            print('Opening time of Office is Bigger then Closing Time')
        else:
            break
    except Exception:
        print('Enter time only (HH:MM) format')
while True:
    try:
        login_time = input('Enter Logging time of Office (DD/MM/YYYY HH:MM) :')
        login_time = datetime.strptime(login_time, "%d/%m/%Y %H:%M")
        if login_time.time() >= opening_time:
            break
        print('Enter login time after the office opening time')
    except Exception:
        print('Enter time only (HH:MM) format')
while True:
    try:
        logout_time = input('Enter Logout time of Office (DD/MM/YYYY HH:MM) :')
        logout_time = datetime.strptime(logout_time, "%d/%m/%Y %H:%M")
        if login_time >= logout_time or login_time.date() != logout_time.date():
            print('Opening time of Office is Bigger then Closing Time or Enter same Date')
        else:
            if logout_time.time() <= closing_time:
                break
            else:
                print('Enter logout time before the office closing time')
    except Exception:
        print('Enter time only (HH:MM) format')
total_hours, total_minutes = calculate_employee_working_hours(login_time, logout_time)
print(f'Total Working Hours: {total_hours} hours {total_minutes} minutes')

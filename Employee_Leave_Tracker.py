from datetime import date, datetime

def analyzes_employee_leave_generates_categorized(leaves, current_date):
    """
    This function analyzes employee leave data and identifies Currently On Leave, Upcoming Leaves,
    and Categorize employees based on leave type.

    Args:
        leaves (list) :  A list of dictionaries, where each dictionary contain employee id, name,
                        leave type, starting date, ending date.

    Returns:
        final_output (dict) : dict it contain Currently On Leave, Upcoming Leaves,
                                and Categorize employees based on leave type.
    """
    final_output = {"Currently On Leave": [], "Upcoming Leaves": [],
        "Leave Type Breakdown": {"Sick": [], "Casual": [], "Paid": []}}
    for employee_data in leaves:
        final_output["Leave Type Breakdown"][employee_data['leave_type']].append(employee_data["employee_name"])
        start_date = datetime.strptime(employee_data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(employee_data["end_date"], "%Y-%m-%d").date()
        if start_date > current_date:
            final_output["Upcoming Leaves"].append(employee_data["employee_name"])
        elif end_date >= current_date:
            final_output["Currently On Leave"].append(employee_data["employee_name"])
    return final_output


def get_leave_type(limit):
    """
    Repeatedly ask number from user until enter between 1 to limit

    argument:
        limit (int): in the sequence last number user can enter

    return:
        string : string base on user select number
    """
    while True:
        try:
            select = int(input('\nSelect Leave Type :'))
            if 1 <= select <= limit:
                break
            print('\nEnter 1 to', limit)
        except Exception:
            print('\nEnter Only Number')
    return 'Sick' if select == 1 else 'Casual' if select == 2 else 'Paid'


current_date = date.today()
leaves = []
while True:
    try:
        e_id = int(input('Enter Employee ID :'))
        if leaves and list(filter(lambda data: data["employee_id"] == e_id, leaves)):
            print('Employee ID already added')
            continue
        while True:
            e_name = input('Enter Employee Name :').strip()
            if e_name:
                break
            else:
                print('Do not enter blank')
        print('1. Sick\n2. Casual\n3. Paid')
        leave_type = get_leave_type(3)
        while True:
            try:
                start_date_str = input("Enter Start Date (YYYY-MM-DD) :")
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                break
            except Exception:
                print('Enter date only (YYYY-MM-DD) format')
        while True:
            try:
                end_date_str = input("Enter End Date (YYYY-MM-DD) :")
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
                if end_date >= start_date:
                    break
                else:
                    print('Ending date must be bigger then staring date')
            except Exception:
                print('Enter date only (YYYY-MM-DD) format')
        leaves.append({"employee_id": e_id, "employee_name": e_name, "leave_type": leave_type, "start_date": start_date_str, "end_date": end_date_str})
        print("\nEmployee's Leave Added")
        while True:
            next_iter = input('Do you want add another book (enter Y/N) ?').strip()
            if next_iter.lower() in ('y', 'n'):
                break
            print("Enter only 'y' or 'n'")
        if next_iter.lower() == 'n':
            break
    except Exception:
        print('Enter only number')
print(analyzes_employee_leave_generates_categorized(leaves, current_date))

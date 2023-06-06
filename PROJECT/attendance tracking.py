import csv
import datetime

def mark_attendance(student_id):
    timestamp = datetime.datetime.now()
    date = timestamp.date()
    time = timestamp.time()

    attendance_file = f"attendance_{date}.csv"
    file_exists = check_file_exists(attendance_file)

    with open(attendance_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Time', 'Student ID'])
        writer.writerow([date, time, student_id])

    print("Attendance marked successfully.")

def check_file_exists(filename):
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False

def view_attendance(date):
    attendance_file = f"attendance_{date}.csv"
    if not check_file_exists(attendance_file):
        print("Attendance file not found.")
        return
    with open(attendance_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
mark_attendance("S12345")
mark_attendance("S67890")
view_attendance(datetime.date.today())

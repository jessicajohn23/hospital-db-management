import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Mark_0904",database="hospital")
if con.is_connected():
    print("Successful connection")
    print("Welcome to Hospital Database")
else:
    print("Not connected")
cur=con.cursor()

cur.execute("create table if not exists patients(PID int primary key,name varchar(20),DOB date,insurance varchar(3),payment_method varchar(4),age int,sex varchar(1),blood_group varchar(3),mobile_no int)")
cur.execute("create table if not exists appointment(PID int primary key,name varchar(20),height float,weight float,bmi float,doctor_name varchar(20),doctor_type varchar(20),date_of_visit date,follow_up_date date)")
cur.execute("create table if not exists doctors(DID int primary key,doctor_name varchar(20),doctor_type varchar(20),age int,room_no int,DOJ date,years_of_experience int,salary float,sex varchar(1))")
n=int(input("Choose a table to enter records: 1.Patients 2.Appointment 3.Doctors"))
if n==1:
    r=int(input("Enter number of records to be entered"))
    for i in range(r):
        PID=int(input("Enter Patient ID"))
        name=input("Enter Patient Name")
        DOB=input("Enter Date of Birth in YYYY-MM-DD format")
        insurance=input("Does the patient have insurance? (yes/no)")
        payment_method=input("Enter Payment Method (cash/card)")
        age=int(input("Enter Age"))
        cur.execute("insert into patients values(%s,%s,%s,%s,%s,%s)",(PID,name,DOB,insurance,payment_method,age))
        con.commit()
elif n==2:
    r=int(input("Enter number of records to be entered"))
    for i in range(r):
        PID=int(input("Enter Patient ID"))
        name=input("Enter Patient Name")
        height=float(input("Enter height in meters"))
        weight=float(input("Enter weight in kg"))
        bmi=weight/(height**2)
        doctor_name=input("Enter Doctor Name")
        doctor_type=input("Enter Doctor Type")
        date_of_visit=input("Enter Date of Visit in YYYY-MM-DD format")
        fud=input("Does the patient have a follow up appointment? (yes/no)")
        if fud=='no':
            follow_up_date=None
        else:
            follow_up_date=input("Enter Follow Up Date in YYYY-MM-DD format")
        cur.execute("insert into appointment values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PID,name,height,weight,bmi,doctor_name,doctor_type,date_of_visit,follow_up_date))
        con.commit()
elif n==3:
    r=int(input("Enter number of records to be entered"))
    for i in range(r):
        DID=int(input("Enter Doctor ID"))
        doctor_name=input("Enter Doctor Name")
        doctor_type=input("Enter Doctor Type")
        age=int(input("Enter age"))
        room_no=int(input("Enter Room Number"))
        DOJ=input("Enter Date of Joining in YYYY-MM-DD format")
        years_of_experience=int(input("Enter Years of Experience"))
        salary=float(input("Enter Salary"))
        sex=input("Enter Sex (M/F)")
        cur.execute("insert into doctors values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(DID,doctor_name,doctor_type,age,room_no,DOJ,years_of_experience,salary,sex))
        con.commit()
else:
    print("Invalid choice")


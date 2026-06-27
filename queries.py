import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Mark_0904",database="hospital")
if con.is_connected():
    print("Successful connection")
    print("Welcome to Hospital Database")
else:
    print("Not connected")
cur=con.cursor()

def p1():
    x="select * from patients"
    execution(x)
def p2():
    x="select name,age from patients order by age desc"
    execution(x)
def p3():
    x="select PID,name,insurance from patients where insurance='yes'"
    execution(x)
def p4():
    x="select name,payment_method from patients"
    execution(x)
def p5():
    x="select * from patients where age between 15 and 20"
    execution(x)
def p6():
    x="select name,payment_method from patients where payment_method='card'"
    execution(x)
def p7():
    x="select PID,name,age,sex from patients where sex='F'"
    execution(x)
def p8():
    x="select PID,name,age,sex from patients where sex='M'"
    execution(x)
def p9():
    x="select PID,name,blood_group from patients where blood_group='O+'"
    execution(x)
def p10():
    x="select * from patients where blood_group like 'B%'"
    execution(x)
def p11():
    x="select count(name),sex from patients group by sex"
    execution(x)

def a1():
    x="select * from appointment"
    execution(x)
def a2():
    x="select name,height from appointment order by height"
    execution(x)
def a3():
    x="select * from appointment where follow_up_date is not null"
    execution(x)
def a4():
    x="select count(name),doctor_type from appointment group by doctor_type"
    execution(x)
def a5():
    x="select * from appointment where doctor_type='Cardiologist'"
    execution(x)
def a6():
    x="select name,bmi from appointment where bmi>25"
    execution(x)
def a7():
    x="select name,bmi from appointment where bmi<18.5"
    execution(x)
def a8():
    x="select name,weight from appointment order by weight"
    execution(x)
def a9():
    x="select name,date_of_visit from appointment where date_of_visit like '2024-08-__'"
    execution(x)
def a10():
    x="select p.name,p.age,p.sex,a.height,a.weight from patients p,appointment a where p.name=a.name"
    execution(x)
def a11():
    x="select * from appointment where doctor_type='dermatologist'"
    execution(x)
def d1():
    x="select * from doctors"
    execution(x)
def d2():
    x="select avg(salary) from doctors"
    execution(x)
def d3():
    x="select min(salary) from doctors"
    execution(x)
def d4():
    x="select max(salary) from doctors"
    execution(x)
def d5():
    x="select DID,doctor_name,age from doctors order by age"
    execution(x)
def d6():
    x="select DID,doctor_name,DOJ from doctors where DOJ like '2015%'"
    execution(x)
def d7():
    x="select DID,doctor_name,years_of_experience from doctors where years_of_experience>5"
    execution(x)
def d8():
    x="select * from doctors where sex='F'"
    execution(x)
def d9():
    x="select * from doctors where sex='M'"
    execution(x)
def d10():
    x="select name,doctor_type from patients p,doctors d where p.pid=d.did"
    execution(x)
def d11():
    x="select a.name,d.room_no from appointment a, doctors d where a.doctor_name=d.doctor_name"
    execution(x)
    
def execution(q):
    cur.execute(q)
    result=cur.fetchall()
    for i in result:
        print(i)

def call(t,c):
    p={1:p1,2:p2,3:p3,4:p4,5:p5,6:p6,7:p7,8:p8,9:p9,10:p10,11:p11}
    a={1:a1,2:a2,3:a3,4:a4,5:a5,6:a6,7:a7,8:a8,9:a9,10:a10,11:a11}
    d={1:d1,2:d2,3:d3,4:d4,5:d5,6:d6,7:d7,8:d8,9:d9,10:d10,11:d11}
    if t==1:
        if c in p.keys():
            p[c]()
        else:
            print("Enter valid choice")
    elif t==2:
        if c in a.keys():
            a[c]()
        else:
            print("Enter valid choice")
    elif t==3:
        if c in d.keys():
            d[c]()
        else:
            print("Enter valid choice")
    else:
        print("Enter valid choice of table")

while True:
    print("1.Patients Table")
    print("2.Appointments Table")
    print("3.Doctors Table")
    t=int(input("Please enter choice of table number"))
    if t==1:
        print("PATIENTS TABLE ")
        print("1.to Display all records")
        print("2.to Display patients' name and age from oldest to youngest")
        print("3.to Display patients who have insurance")
        print("4.to Display patients according to payment method")
        print("5.to Display patient details of those aged between 15 and 20")
        print("6.to Display patients whose payment method is through card")
        print("7.to Display the female patients")
        print("8.to Display the male patients")
        print("9.to Display the patients with O+ blood group")
        print("10.to Display the patients with either B+ or B- blood group")
        print("11.to Display the patients according to sex")
    elif t==2:
        print("APPOINTMENTS TABLE")
        print("1.to Display all records")
        print("2.to Display patients in increasing order of height")
        print("3.to Display patients who have a follow up appointment")
        print("4.to Display patients according to doctor type")
        print("5.to Display patients who have an appointment with a cardiologist")
        print("6.to Display patients who are overweight")
        print("7.to Display patients who are underweight")
        print("8.to Display patients by increasing weight")
        print("9.to Display patients who visited in August")
        print("10.to Display health details of all patients")
        print("11.to Display patients who have an appointment with dermatologists")
    elif t==3:
        print("DOCTORS TABLE")
        print("1.to Display all records")
        print("2.to Display average salary")
        print("3.to Display minimum salary")
        print("4.to Display maximum salary")
        print("5.to Display doctors in increasing order of age")
        print("6.to Display doctors who joined in 2015")
        print("7.to Display doctors who have years of experience above 5")
        print("8.to Display female doctors ")
        print("9.to Display male doctors")
        print("10.to Display patient and their doctor types")
        print("11.to Display patient names along with room numbers")
    c=int(input("Please enter choice of query"))
    call(t,c)
    ans=input("Would you like to continue")
    if ans=='n' or ans=='N':
        print("Thank you")
        break
    else:
        pass
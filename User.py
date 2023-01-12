import hashlib
from brta import BRTA
from vehicles import Car,Bike,Cng
from ride_manager import uber
from random import random,randint


license_authority=BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encrypted=hashlib.md5(password.encode()).hexdigest()
        already_existed=False
        with open('user.txt','r') as f:
            if email in f.read():
                already_existed=True
                # print('already exist')
        if already_existed==False:   
            with open("user.txt",'a') as file:
                file.writelines(f'{email} {pwd_encrypted}\n')
            file.close()
            # print(self.name,'user created')

    @staticmethod
    def log_in(email,password):
        stored_password=''
        with open('user.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(' ')[1]
        file.close()
        hashed_password=hashlib.md5(password.encode()).hexdigest()
        if hashed_password==stored_password:
            print('valid user')
            return True
        else: 
            print('invalid user')
            return False
        # print('password found',stored_password)

class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location=location
        self.balancec=balance
        super().__init__(name, email, password)
    
    def set_location(self,location):
        self.location=location
    
    def get_location(self):
        return self.location

    def request_trip(self,destination):
        pass

    def start_a_trip(self,fare):
        self.balancec-=fare


class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.license=license
        self.valid_driver=license_authority.validation_license(email,license)
        self.earning=0

    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result==False:
            # print('Sorry you failed, try again')
            self.license=None
        else:
            self.license=result
            self.valid_driver=True
    
    def register_a_vehicle(self,vehicle_type,license_plate,rate,):
        if self.valid_driver is True:
            new_vehicle=None
            if vehicle_type=='car':
                new_vehicle=Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicles(vehicle_type,new_vehicle)
            elif vehicle_type=='bile':
                new_vehicle=Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicles(vehicle_type,new_vehicle)
            else:
                new_vehicle=Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicles(vehicle_type,new_vehicle)
            pass
        else:
            print('you are not a valid driver')

    def start_a_trip(self,destination,fare):
        self.earning+=fare
        self.location=destination



rider1=Rider('rider1','rider1@gmail.com','raider1',randint(0,30),5000)
rider1=Rider('rider2','rider2@gmail.com','raider2',randint(0,30),5000)
rider3=Rider('rider3','rider3@gmail.com','raider3',randint(0,30),5000)

for i in range(1,100):
    driver1=Driver(f'driver{i}',f'driver{i}@gamil.com',f'driver{i}',randint(0,30),randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle('car',1245,10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider1,'car',90)


# start from rider 2- 3



git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/AlSaimun/OOP-Rider.git
git push -u origin main
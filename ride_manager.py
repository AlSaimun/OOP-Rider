
class RideManager:
    def __init__(self) -> None:
        print('Ride manage activalted')
        self.__available_Cars=[]
        self.__available_Bikes=[]
        self.__available_Cngs=[]

    def add_a_vehicles(self,vehicle_type,vehicle):
        if vehicle_type=='car':
            self.__available_Cars.append(vehicle)
        elif vehicle_type=='bike':
            self.__available_Bikes.append(vehicle)
        else:
            self.__available_Cngs.append(vehicle)

    def get_available_cars(self):
        return self.__available_Cars

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type=='car':
            if len(self.__available_Cars)==0:
                print('Sorry no cars is available')
                return False
            for car in self.__available_Cars:
                print('poential',rider.location,car.driver.location)
                if abs(rider.location-car.driver.location)<30:
                    if car.status=='available':
                        car.status='unavailable'
                        print(len(self.__available_Cars))
                        self.__available_Cars.remove(car)
                        print(len(self.__available_Cars))

                        print('match')
                        return True


uber=RideManager()


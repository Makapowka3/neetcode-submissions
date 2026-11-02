class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]
        return

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.parking[0] != 0:
                self.parking[0] -= 1
                return True
            else:
                return False
        
        elif carType == 2:
            if self.parking[1] != 0:
                self.parking[1] -= 1
                return True
            else:
                return False
        
        else:
            if self.parking[2] != 0:
                self.parking[2] -= 1
                return True
            else:
                return False

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]
        return

    def addCar(self, carType: int) -> bool:
        if self.parking[carType-1] == 0: return False
        self.parking[carType-1] -= 1
        return True

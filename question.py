class Mobile:
    def __init__(self,mobile_name,battery_life,camera):
        self.mobile_name=mobile_name
        self.battery_life=battery_life
        self.camera=camera
    def details(self):
        return f"The mobile name is {self.mobile_name}\nthe battery life is {self.battery_life}\nthe camera is {self.camera}"
b = Mobile("iphone","6000 mAh","108 megapixel")
print(b.details()) 
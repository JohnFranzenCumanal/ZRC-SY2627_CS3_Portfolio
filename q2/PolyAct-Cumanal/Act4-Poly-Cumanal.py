class HealthPotion:
    def use(self):
        print("You regain 50 HP")
        
class ManaPotion:
    def use(self):
        print("You regain 30 MP")
        
class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds")
        
        
def apply_item(item):
    item.use()
    
healthpotion = HealthPotion()
manapotion = ManaPotion()
speedboost = SpeedBoost()

items = [healthpotion, manapotion, speedboost]

for item in items:
    apply_item(item)

        

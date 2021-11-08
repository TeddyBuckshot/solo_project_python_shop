# build objects for testing here

from models.brand import Brand
from models.keyboard import Keyboard
import repositories.brand_repository as brand_repository
import repositories.keyboard_repository as keyboard_repository

brand_repository.delete_all()
keyboard_repository.delete_all()

brand1 = Brand("Glorious PC gaming race", "USA")
brand1 = brand_repository.save(brand1)

brand2 = Brand("Corsair", "USA")
brand2 = brand_repository.save(brand2)

brand3 = Brand("Razer", "USA")
brand3 = brand_repository.save(brand3)

keyboard1 = Keyboard("GMMK Pro", brand1, "75% Mechanical Keyboard", 4, 100.00, 169.99)
keyboard1 = keyboard_repository.save(keyboard1)

keyboard2 = Keyboard("GMMK", brand1, "Full-size Mechanical Keyboard", 6, 80.00, 149.99)
keyboard2 = keyboard_repository.save(keyboard2)

keyboard3 = Keyboard("GMMK TKL", brand1, "10-key-less Compact Mechanical Keyboard", 10, 85.00, 154.99)
keyboard3 = keyboard_repository.save(keyboard3)

keyboard4 = Keyboard("K70", brand2, "Full-size Gaming Keyboard", 4, 120.00, 179.99)
keyboard4 = keyboard_repository.save(keyboard4)

keyboard5 = Keyboard("Huntsman Elite", brand3, "TKL Optical-switch Mechanical Keyboard", 4, 95.00, 129.99)
keyboard5 = keyboard_repository.save(keyboard5)



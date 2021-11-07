# build objects for testing here

from models.brand import Brand
from models.keyboard import Keyboard
import repositories.brand_repository as brand_repository
import repositories.keyboard_repository as keyboard_repository

brand_repository.delete_all()
keyboard_repository.delete_all()

brand1 = Brand("Glorious PC gaming race", "USA")
brand1 = brand_repository.save(brand1)

keyboard1 = Keyboard("GMMK Pro", brand1, "75% Mechanical Keyboard", 4, 100.00, 169.99)
keyboard1 = keyboard_repository.save(keyboard1)



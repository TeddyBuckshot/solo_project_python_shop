from models.brand import Brand
from models.category import Category
from models.keyboard import Keyboard
import repositories.brand_repository as brand_repository
import repositories.keyboard_repository as keyboard_repository
import repositories.category_repository as category_repository

brand_repository.delete_all()
keyboard_repository.delete_all()

brand1 = Brand("Glorious PC gaming race", "Texas, USA")
brand2 = Brand("Corsair", "California, USA")
brand3 = Brand("Razer", "California, USA")
brand4 = Brand("Logitech", "Lausanne, Switzerland")
gpgr = brand_repository.save(brand1)
corsair = brand_repository.save(brand2)
razer = brand_repository.save(brand3)
logitech = brand_repository.save(brand4)

category1 = Category("60%")
category2 = Category("75%")
category3 = Category("TKL")
category4 = Category("full-size")
sixty = category_repository.save(category1)
seventy = category_repository.save(category2)
tenkey = category_repository.save(category3)
full = category_repository.save(category4)

keyboard1 = Keyboard("GMMK Pro", gpgr, "75% Mechanical Keyboard", seventy, 10, 110.00, 169.99)
keyboard2 = Keyboard("GMMK - FULL SIZE", gpgr, "World's first RGB, modular mechanical keyboard.", full, 15, 80.00, 109.95)
keyboard3 = Keyboard("GMMK - TENKEYLESS", gpgr, "Ten-key-less model of GMMK.", tenkey, 20, 80.00, 109.95)
keyboard4 = Keyboard("GMMK - COMPACT", gpgr, "60% model of GMMK, perfect for gaming.", sixty, 25, 80.00, 109.95)
keyboard5 = Keyboard("k65 Mini", corsair, "Mini 60% mechanical gaming keyboard.", sixty, 20, 75.00, 109.99)
keyboard6 = Keyboard("k70 RBG MK.2", corsair, "Premium gaming keyboard, built to last.", full, 12, 120.00, 179.99)
keyboard7 = Keyboard("k95", corsair, "Fullsize keyboard with built-in Elgato Stream Deck integration.", full, 10, 140.00, 199.99)
keyboard8 = Keyboard("k65 Rapidfire", corsair, "Compact TKL format mechanical keyboard with RGB.", tenkey, 18, 95.00, 139.99)
keyboard9 = Keyboard("Huntsman V2", razer, "No frills. All performance.", full, 30, 150.00, 199.99)
keyboard10 = Keyboard("Blackwidow V3 Mini", razer, "Compact, wireless RBG mechanical keyboard.", sixty, 24, 145.00, 199.99)
keyboard11 = Keyboard("Pro Type", razer, "Wireless keyboard focused on productivity.", full, 40, 95.00, 139.99)
keyboard12 = Keyboard("Huntsman V2 TKL", razer, "Same deal. No frills. All performance. More compact.", tenkey, 20, 115.00, 159.99)
keyboard1 = keyboard_repository.save(keyboard1)
keyboard2 = keyboard_repository.save(keyboard2)
keyboard3 = keyboard_repository.save(keyboard3)
keyboard4 = keyboard_repository.save(keyboard4)
keyboard5 = keyboard_repository.save(keyboard5)
keyboard6 = keyboard_repository.save(keyboard6)
keyboard7 = keyboard_repository.save(keyboard7)
keyboard8 = keyboard_repository.save(keyboard8)
keyboard9 = keyboard_repository.save(keyboard9)
keyboard10= keyboard_repository.save(keyboard10)
keyboard11 = keyboard_repository.save(keyboard11)
keyboard12 = keyboard_repository.save(keyboard12)
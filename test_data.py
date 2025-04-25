import os
import sys
import django

# Loyiha papkasini Python yo‘liga qo‘shish
sys.path.append("D:\\FoodExpres")

# Django sozlamalarini aniqlash va ishga tushirish
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Foodexpres.settings")
django.setup()

# Kerakli modellar import qilinadi
from user_app.models import Kitchen, Category, SubCategory, Product
from django.core.files import File

# Test ma'lumotlarni yaratish
def create_test_data():
    # 1. Avval SubCategory va Product modellarini tozalash
    print("SubCategory modeli tozalanmoqda...")
    SubCategory.objects.all().delete()
    print("Product modeli tozalanmoqda...")
    Product.objects.all().delete()

    # 2. Mavjud Kitchen va Category ma'lumotlarini olish
    kitchens = Kitchen.objects.all()
    categories = Category.objects.all()

    # 3. SubCategory modellarini yaratish (10 ta)
    subcategories_data = [
        {"name": "Sho‘rvalar", "category": categories[0]},  # Birinchi taomlar
        {"name": "Lag‘monlar", "category": categories[0]},  # Birinchi taomlar
        {"name": "Kaboblar", "category": categories[1]},    # Ikkinchi taomlar
        {"name": "Palovlar", "category": categories[1]},    # Ikkinchi taomlar
        {"name": "Yevropa salatlari", "category": categories[2]},  # Salatlar
        {"name": "O‘zbek salatlari", "category": categories[2]},  # Salatlar
        {"name": "Gazli ichimliklar", "category": categories[3]},  # Ichimliklar
        {"name": "Choy va qahva", "category": categories[3]},     # Ichimliklar
        {"name": "Klassik shirinliklar", "category": categories[4]},  # Shirinliklar
        {"name": "Burgerlar", "category": categories[5]},  # Fastfood taomlari
    ]
    subcategories = []
    for data in subcategories_data:
        subcategory, created = SubCategory.objects.get_or_create(**data)
        if created:
            print(f"SubCategory yaratildi: {data['name']}")
        subcategories.append(subcategory)

    # 4. Product modellarini yaratish (50 ta)
    products_data = [
        # O‘zbek taomlari
        {"title": "Mastava", "description": "An’anaviy o‘zbek sho‘rvasi", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[0], "price": 15000, "discount": 5},
        {"title": "Chuchvara", "description": "Go‘shtli chuchvara", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[0], "price": 20000, "discount": 0},
        {"title": "Lag‘mon", "description": "Qo‘lda tayyorlangan lag‘mon", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[1], "price": 18000, "discount": 10},
        {"title": "Tovuq lag‘mon", "description": "Tovuq go‘shtli lag‘mon", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[1], "price": 20000, "discount": 0},
        {"title": "Tandir kabob", "description": "Tandirda pishirilgan kabob", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[2], "price": 35000, "discount": 5},
        {"title": "Lula kabob", "description": "Go‘shtli lula kabob", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[2], "price": 30000, "discount": 0},
        {"title": "Toshkent palovi", "description": "An’anaviy Toshkent palovi", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[3], "price": 40000, "discount": 10},
        {"title": "Samarqand palovi", "description": "Samarqand uslubidagi palov", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[3], "price": 45000, "discount": 0},
        {"title": "Achchiq-chuchuk", "description": "Pomidor va piyozli salat", "kitchen": kitchens[0], "category": categories[2], "subcategory": subcategories[5], "price": 10000, "discount": 0},
        {"title": "Olivye", "description": "Klassik Olivye salati", "kitchen": kitchens[0], "category": categories[2], "subcategory": subcategories[4], "price": 15000, "discount": 5},

        # Italya taomlari
        {"title": "Pizza Margherita", "description": "Klassik italyan pizzasi", "kitchen": kitchens[1], "category": categories[6], "subcategory": subcategories[2], "price": 50000, "discount": 10},
        {"title": "Pasta Carbonara", "description": "Italya uslubidagi pasta", "kitchen": kitchens[1], "category": categories[6], "subcategory": subcategories[2], "price": 45000, "discount": 0},
        {"title": "Tiramisu", "description": "Italya shirinligi", "kitchen": kitchens[1], "category": categories[4], "subcategory": subcategories[8], "price": 30000, "discount": 5},
        {"title": "Sezar salati", "description": "Tovuq go‘shtli Sezar salati", "kitchen": kitchens[1], "category": categories[2], "subcategory": subcategories[4], "price": 25000, "discount": 0},
        {"title": "Pasta Alfredo", "description": "Kremli pasta", "kitchen": kitchens[1], "category": categories[6], "subcategory": subcategories[2], "price": 48000, "discount": 0},
        {"title": "Krem sup", "description": "Italya uslubidagi krem sup", "kitchen": kitchens[1], "category": categories[0], "subcategory": subcategories[0], "price": 30000, "discount": 5},
        {"title": "Grecheskiy salat", "description": "Yunon salati", "kitchen": kitchens[1], "category": categories[2], "subcategory": subcategories[4], "price": 20000, "discount": 0},
        {"title": "Espresso", "description": "Italya qahvasi", "kitchen": kitchens[1], "category": categories[3], "subcategory": subcategories[7], "price": 15000, "discount": 5},
        {"title": "Cappuccino", "description": "Kremli qahva", "kitchen": kitchens[1], "category": categories[3], "subcategory": subcategories[7], "price": 18000, "discount": 0},
        {"title": "Moxito", "description": "Yozgi ichimlik", "kitchen": kitchens[1], "category": categories[3], "subcategory": subcategories[6], "price": 15000, "discount": 5},

        # Xitoy taomlari
        {"title": "Nudle", "description": "Xitoy uslubidagi nudle", "kitchen": kitchens[2], "category": categories[1], "subcategory": subcategories[2], "price": 25000, "discount": 0},
        {"title": "Wok tovuq", "description": "Tovuq va sabzavotli wok", "kitchen": kitchens[2], "category": categories[1], "subcategory": subcategories[2], "price": 30000, "discount": 5},
        {"title": "Dumpling", "description": "Xitoy chuchvarasi", "kitchen": kitchens[2], "category": categories[0], "subcategory": subcategories[0], "price": 20000, "discount": 0},

        # Fastfood
        {"title": "Burger", "description": "Klassik burger", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 25000, "discount": 5},
        {"title": "Cheeseburger", "description": "Pishloqli burger", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 28000, "discount": 0},
        {"title": "Hot-dog", "description": "Klassik hot-dog", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 15000, "discount": 0},
        {"title": "Fri kartoshka", "description": "Qovurilgan kartoshka", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 10000, "discount": 0},
        {"title": "Cola", "description": "Gazlangan ichimlik", "kitchen": kitchens[3], "category": categories[3], "subcategory": subcategories[6], "price": 8000, "discount": 0},
        {"title": "Fanta", "description": "Gazlangan ichimlik", "kitchen": kitchens[3], "category": categories[3], "subcategory": subcategories[6], "price": 8000, "discount": 0},
        {"title": "Lavash", "description": "Tovuq lavash", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 20000, "discount": 0},
        {"title": "Donar", "description": "Turkiya donari", "kitchen": kitchens[3], "category": categories[5], "subcategory": subcategories[9], "price": 25000, "discount": 0},

        # Yapon taomlari
        {"title": "Sushi", "description": "Yapon sushi", "kitchen": kitchens[4], "category": categories[8], "subcategory": subcategories[2], "price": 60000, "discount": 10},
        {"title": "Miso sho‘rva", "description": "Yapon sho‘rvasi", "kitchen": kitchens[4], "category": categories[0], "subcategory": subcategories[0], "price": 25000, "discount": 0},

        # Fransuz taomlari
        {"title": "Kruassan", "description": "Fransuz kruassani", "kitchen": kitchens[5], "category": categories[4], "subcategory": subcategories[8], "price": 15000, "discount": 0},
        {"title": "Ratatuy", "description": "Sabzavotli fransuz taomi", "kitchen": kitchens[5], "category": categories[1], "subcategory": subcategories[2], "price": 35000, "discount": 5},

        # Turk taomlari
        {"title": "Baklava", "description": "Turk shirinligi", "kitchen": kitchens[6], "category": categories[4], "subcategory": subcategories[8], "price": 20000, "discount": 0},
        {"title": "Kebab", "description": "Turk kebabi", "kitchen": kitchens[6], "category": categories[7], "subcategory": subcategories[2], "price": 30000, "discount": 5},

        # Hind taomlari
        {"title": "Butter Chicken", "description": "Hind tovuqli taomi", "kitchen": kitchens[7], "category": categories[1], "subcategory": subcategories[2], "price": 40000, "discount": 0},
        {"title": "Naan", "description": "Hind noni", "kitchen": kitchens[7], "category": categories[1], "subcategory": subcategories[2], "price": 10000, "discount": 0},

        # Meksika taomlari
        {"title": "Tako", "description": "Meksika takosi", "kitchen": kitchens[8], "category": categories[1], "subcategory": subcategories[2], "price": 25000, "discount": 5},
        {"title": "Burrito", "description": "Meksika burritosi", "kitchen": kitchens[8], "category": categories[1], "subcategory": subcategories[2], "price": 30000, "discount": 0},

        # Arab taomlari
        {"title": "Hummus", "description": "Arab humusi", "kitchen": kitchens[9], "category": categories[2], "subcategory": subcategories[5], "price": 15000, "discount": 0},
        {"title": "Falafel", "description": "Arab falafeli", "kitchen": kitchens[9], "category": categories[1], "subcategory": subcategories[2], "price": 20000, "discount": 5},

        # Qo‘shimcha O‘zbek taomlari
        {"title": "Dimlama", "description": "Sabzavotli dimlama", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[2], "price": 28000, "discount": 0},
        {"title": "Sho‘rva", "description": "Go‘shtli sho‘rva", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[0], "price": 16000, "discount": 5},
        {"title": "Manti", "description": "Go‘shtli manti", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[2], "price": 20000, "discount": 0},
        {"title": "Qovurma lag‘mon", "description": "Qovurilgan lag‘mon", "kitchen": kitchens[0], "category": categories[0], "subcategory": subcategories[1], "price": 22000, "discount": 10},
        {"title": "Jizzax palovi", "description": "Jizzax uslubidagi palov", "kitchen": kitchens[0], "category": categories[1], "subcategory": subcategories[3], "price": 42000, "discount": 0},
        {"title": "Olma salati", "description": "Olma va sabzavotli salat", "kitchen": kitchens[0], "category": categories[2], "subcategory": subcategories[5], "price": 12000, "discount": 0},
        {"title": "Kungaboqar salati", "description": "Tovuq va sabzavotli salat", "kitchen": kitchens[0], "category": categories[2], "subcategory": subcategories[4], "price": 18000, "discount": 5},
        {"title": "Choy", "description": "Issiq choy", "kitchen": kitchens[0], "category": categories[3], "subcategory": subcategories[7], "price": 5000, "discount": 0},
        {"title": "Suv", "description": "Sof suv", "kitchen": kitchens[0], "category": categories[3], "subcategory": subcategories[6], "price": 3000, "discount": 0},
    ]

    for data in products_data:
        product, created = Product.objects.get_or_create(
            title=data["title"],
            description=data["description"],
            kitchen=data["kitchen"],
            category=data["category"],
            subcategory=data["subcategory"],
            price=data["price"],
            discount=data["discount"],
        )
        if created:
            print(f"Product yaratildi: {data['title']}")
            # Placeholder rasm qo‘shish
            placeholder_path = os.path.join("media", "product", "image", "placeholder.jpg")
            if os.path.exists(placeholder_path):
                with open(placeholder_path, "rb") as f:
                    product.photo.save("placeholder.jpg", File(f), save=True)

if __name__ == "__main__":
    # Test ma'lumotlarni yaratish
    create_test_data()
    print("SubCategory va Product modellariga test ma'lumotlari muvaffaqiyatli qo‘shildi!")
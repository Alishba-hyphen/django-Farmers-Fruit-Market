from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Seeds the database with default products"

    def handle(self, *args, **kwargs):

        if Product.objects.exists():
            self.stdout.write(self.style.SUCCESS("Products already exist."))
            return

        products = [
            {
                "name": "Orange",
                "price": 1.99,
                "stock": 50,
                "image_url": "https://orchardfruit.com/cdn/shop/files/Navel-Oranges-1-Pcs-The-Orchard-Fruit-72137770.jpg?v=1751051709&width=1000"
            },
            {
                "name": "Strawberry",
                "price": 2.99,
                "stock": 30,
                "image_url": "https://hips.hearstapps.com/clv.h-cdn.co/assets/15/22/1432664914-strawberry-facts1.jpg?resize=980:*"
            },
            {
                "name": "Kiwi",
                "price": 3.99,
                "stock": 40,
                "image_url": "https://www.gardenia.net/wp-content/uploads/2019/02/ChatGPT-Image-Aug-26-2025-02_17_58-PM.jpg"
            },
            {
                "name": "Mango",
                "price": 2.99,
                "stock": 100,
                "image_url": "https://www.pittmandavis.com/images/xl/pd24-floridamangoes.webp?v=1"
            },
            {
                "name": "Watermelon",
                "price": 4.99,
                "stock": 10,
                "image_url": "https://www.tasteofhome.com/wp-content/uploads/2026/07/How-to-Pick-a-Perfect-Watermelon_GettyImages-2119010569_FT.jpg?fit=750%2C750"
            },
            {
                "name": "Banana",
                "price": 1.99,
                "stock": 20,
                "image_url": "https://pamsdailydish.com/wp-content/uploads/2015/04/Bunch-Bananas-1.jpg"
            },
            {
                "name": "Apple",
                "price": 2.99,
                "stock": 100,
                "image_url": "https://www.bhg.com/thmb/ax1BqSJiW-uU-PLZ8tsFE4Tx-Rg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/BG_Apples_TOC_5326-1-1a51b65e00944463aa28148b39008efd.jpg"
            },
            {
                "name": "Peaches",
                "price": 1.99,
                "stock": 20,
                "image_url": "https://draxe.com/wp-content/uploads/2016/08/DrAxePeachHeader.jpg"
            },
            {
                "name": "Blueberries",
                "price": 3.99,
                "stock": 100,
                "image_url": "https://longevity-protocols.com/en/knowledge-base/whole-foods/blueberries/assets/featured.jpg"
            },
            {
                "name": "Grapes",
                "price": 3.99,
                "stock": 40,
                "image_url": "https://plantsexpress.com/cdn/shop/products/Green-Seedless-Table-Grape-2.jpg?v=1684510111&width=1800"
            },
            {
                "name": "Honeydew",
                "price": 4.99,
                "stock": 30,
                "image_url": "https://www.threshseed.com/cdn/shop/files/honeydew-orange-flesh-seeds-39701233172729.jpg?v=1700359281&width=580"
            },
            {
                "name": "Cherries",
                "price": 2.99,
                "stock": 30,
                "image_url": "https://images.immediate.co.uk/production/volatile/sites/30/2023/07/Cherries-02-d6ba13e.jpg?quality=90&webp=true&resize=440,400"
            },
        ]

        for product in products:
            Product.objects.create(**product)

        self.stdout.write(self.style.SUCCESS("Products added successfully!"))
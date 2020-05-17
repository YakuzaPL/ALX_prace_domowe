class Advertisement:

    def __init__(self, title, description, price, vendor_name, vendor_tel, vendor_mail):
        self.title = title
        self.description = description
        self.price = price
        self.vendor_name = vendor_name
        self.vendor_tel = vendor_tel
        self.vendro_mail = vendor_mail

    def make_adv(self):
        advert = {"title": self.title,
                  "Content": self.description,
                  "Price": self.price,
                  "vendro name": self.vendor_name,
                  "Vendor tel": self.vendor_tel,
                  "Vendor_mail": self.vendro_mail
                  }
        return advert


class AdvertCollector():
    def __init__(self):
        self.ad_colection = {}

    def add_advertisment(self, advertisement: Advertisement, advert_num=1):

        for i in range(1, 4):
            self.ad_colection[advert_num] = advertisement.make_adv()
            advert_num += 1

    def adv_printer(self):
        for ad in self.ad_colection.values():

            print("-" * 35)
            for cat, cont in ad.items():
                print(f"{cat}: {cont}")

    def __str__(self):
        return self.adv_printer()


# advert = AdvertCollector()
advert1 = Advertisement("Sprzedam1", "sdafcniksdacniuansc", 659895, "Jakub", "560-987-744", "jz@mail.com")
advert2 = Advertisement("Sprzedam2", "sdafcniksdacniuansc", 659895, "Zenek", "693-258-987", "zz@mail.com")
advert3 = Advertisement("Sprzedam3", "sdafcniksdacniuansc", 659895, "Aga", "844-647-872", "az@mail.com")

print(advert1)

colection = AdvertCollector()
colection.add_advertisment(advert1)
# colection.adv_printer()
colection.add_advertisment(advert2)
# colection.adv_printer()
colection.add_advertisment(advert3)
colection.adv_printer()

print(30 * "*")
a = colection.ad_colection.keys()
b = colection.ad_colection
print(a)
for x, y in b.items():
    print(x, y)

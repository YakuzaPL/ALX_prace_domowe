class Advertisement:

    def __init__(self, title, description, price, vendor_name, vendor_tel, vendor_mail):
        self.title = title
        self.description = description
        self.price = price
        self.vendor_name = vendor_name
        self.vendor_tel = vendor_tel
        self.vendro_mail = vendor_mail

    def make_adv(self) -> str:
        return f"Tytuł: {self.title}\n {self.description}\n Cena {self.price}\n {self.vendor_name}:\n " \
               f"tel: {self.vendor_tel}\n mail: {self.vendro_mail}"

    def __str__(self):
        return self.make_adv()


class AdvertCollector():
    def __init__(self):
        self.ad_collection = dict()

    def add_advertisment(self, advertisement: Advertisement, advert_num=1):

        self.ad_collection = {advert_num: {"title": advertisement.title,
                                           "Content": advertisement.description,
                                           "Price": advertisement.price,
                                           "vendro name": advertisement.vendor_name,
                                           "Vendor tel": advertisement.vendor_tel,
                                           "Vendor_mail": advertisement.vendro_mail
                                           }}
        advert_num += 1

    def adv_printer(self):
        for ad in self.ad_collection.values():
            print(self.ad_collection.keys())
            print("-" * 35)
            for cat, cont in ad.items():
                print(f"{cat}: {cont}")

    def __str__(self):
        return self.adv_printer()


# advert = AdvertCollector()
advert1 = Advertisement("Sprzedam1", "sdafcniksdacniuansc", 659895, "Jakub", "560-987-744", "jz@mail.com")
advert2 = Advertisement("Sprzedam2", "sdafcniksdacniuansc", 659895, "Zenek", "693-258-987", "zz@mail.com")
advert3 = Advertisement("Sprzedam3", "sdafcniksdacniuansc", 659895, "Aga", "844-647-872", "az@mail.com")

colection = AdvertCollector()
colection.add_advertisment(advert1)
colection.add_advertisment(advert2)
colection.add_advertisment(advert3)
colection.adv_printer()

print(30 * "*")
a = colection.ad_collection.keys()
print(a)

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
        # super().__init__(title, description, price, vendor_name, vendor_tel, vendor_mail)
        self.ad_collection = dict()

    def add_advertisment(self, title, description, price, vendor_name, vendor_tel, vendro_mail):
        advert_num = 1

        self.ad_collection[advert_num] = {"title": title,
                                          "Content": description,
                                          "Price": price,
                                          "vendro name": vendor_name,
                                          "Vendor tel": vendor_tel,
                                          "Vendor_mail": vendro_mail
                                          }
        if advert_num in self.ad_collection.keys():
            advert_num += 1

    def adv_printer(self) -> str:
        for ad in self.ad_collection.values():
            print(self.ad_collection.keys())
            print("-" * 35)
            for cat, cont in ad.items():
                print(f"{cat}: {cont}")

    def __str__(self) -> str:
        return self.adv_printer()


advert = AdvertCollector()
advert.add_advertisment("Sprzedam", "sdafcniksdacniuansc", 659895, "Jakub", "560-987-744", "jz@mail.com")
advert.adv_printer()
advert.add_advertisment("Sprzedam2", "sdafcniksdacniuansc", 659895, "Zenek", "693-258-987", "zz@mail.com")
advert.adv_printer()
print(35*"*")
print(advert.ad_collection)
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


class AdvertCollector(Advertisement):
    def __init__(self, title, description, price, vendor_name, vendor_tel, vendor_mail):
        super().__init__(title, description, price, vendor_name, vendor_tel, vendor_mail)
        self.ad_collection = dict()

    def add_advertisment(self):
        advert_num = 1
        self.ad_collection[advert_num] = {"title": self.title,
                                          "Content": self.description,
                                          "Price": self.price,
                                          "vendro name": self.vendor_name,
                                          "Vendor tel": self.vendor_tel,
                                          "Vendor_mail": self.vendro_mail
                                          }
        advert_num += 1

    def adv_printer(self) -> str:
        for ad in self.ad_collection.values():
            print(self.ad_collection.keys())
            print("-" * 35)
            for cat, cont in ad.items():
                print(f"{cat}: {cont}")

    def __str__(self) -> str:
        return self.adv_printer()


ad1 = AdvertCollector("auto na sprzedaż1", "bsndcijsancxjiansicdxna", 32580, "Jakub", "509-998-666", "jz@mail.com")
ad1.add_advertisment()
ad1.adv_printer()

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


advert = Advertisement("Sprzedam Auto", "Mam do sprzedania samochód", 32000, "Kuba", 506585098, "jz@mail.com")

print(advert.make_adv())
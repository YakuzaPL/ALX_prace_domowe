
class Advertisement:

    def __init__(self, title, description, price, vendor_name, vendor_tel, vendor_mail):
        self.title = title
        self.description = description
        self.price = price
        self.vendor_name = vendor_name
        self.vendor_tel = vendor_tel
        self.vendro_mail = vendor_mail

    def make_adv(self):
        advert = [self.title, self.description, self.price, self.vendor_name, self.vendor_tel, self.vendro_mail]
        return advert


class AdvertCollector():
    def __init__(self):
        self.advert_colection = list()

    def add_advertisment(self, advertisement: Advertisement):
        """
        Colecting advertisments from class Advertismen
        :param advertisement: object
        :return:
        """
        self.advert_colection.append(advertisement.make_adv())

    def print_advert(self):
        for advert in self.advert_colection:
            print(30 * "-")
            for i in advert:
                print(i)

    def price_filterer(self, advert_colection):
        filter_of_lists = filter(lambda advert: advert[2] < 3500, advert_colection)
        filtered_advertisment = list(filter_of_lists)
        for advertisment in filtered_advertisment:
            print(30*"-")
            for information in advertisment:
                print(information)

    def __str__(self):
        return self.print_advert()


advert1 = Advertisement("Sprzedam1", "sdafcniksdacniuansc", 450, "Jakub", "560-987-744", "jz@mail.com")
advert2 = Advertisement("Sprzedam2", "sdafcniksdacniuansc", 4000, "Zenek", "693-258-987", "zz@mail.com")
advert3 = Advertisement("Sprzedam3", "sdafcniksdacniuansc", 2800, "Aga", "844-647-872", "az@mail.com")

colector = AdvertCollector()
colector.add_advertisment(advert1)
colector.add_advertisment(advert2)
colector.add_advertisment(advert3)

# print(colector.print_advert())

# colector.price_filterer(500, 3000)
colector.price_filterer(colector.advert_colection)
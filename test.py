

advertisment = [["Ogłoszenie 1", "Treść ogłoszenia 1", 3520, "Imię sprzedającego 1", "Mail 1", "telefon 1"],
                ["Ogłoszenie 2", "Treść ogłoszenia 2", 480, "Imię sprzedającego 2", "Mail 2", "telefon 2"],
                ["Ogłoszenie 3", "Treść ogłoszenia 3", 56896, "Imię sprzedającego 3", "Mail 3", "telefon 3"],
                ["Ogłoszenie 4", "Treść ogłoszenia 4", 1200, "Imię sprzedającego 4", "Mail 4", "telefon 4"],
                ["Ogłoszenie 5", "Treść ogłoszenia 5", 98, "Imię sprzedającego 5", "Mail 5", "telefon 5"],
                ["Ogłoszenie 6", "Treść ogłoszenia 6", 1587415, "Imię sprzedającego 6", "Mail 6", "telefon 6"]]


def advertismen_searcher(list_of_adverts):
    for advert in list_of_adverts:
        print(30 * "-")
        for content in advert:
            print(content)


def price_filterer(list_of_adverts, more_than: int = 0, less_than: int = 0):
    for advert in list_of_adverts:
        for content in advert:
            if type(content) == int:
                if more_than < content < less_than:
                    for advert_list in list_of_adverts:
                        if content in advert_list:
                            print(30 * "-")
                            for data in advert_list:
                                print(data)


print(price_filterer(advertisment, 150, 2500))

# numbers = [1, 2, 3, 4, 5, 6]
#
# list_filter = filter(lambda number: number < 4, numbers)
# filtered_list = list(list_filter)

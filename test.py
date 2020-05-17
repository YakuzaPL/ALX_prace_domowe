advert = {1: {"title": "Tytuł1",
              "Content": "bla, bla bla bla bala bla",
              "vendro name": "Jakub",
              "Vendor tel": "506-585-098",
              "Vendor_mail": "jz@mail.com"},
          2: {"title": "Tytuł2",
              "Content": "ra, la, la, la, la",
              "vendro name": "Michał",
              "Vendor tel": "506-555-258",
              "Vendor_mail": "mj@mail.com"},
          3: {"title": "Tytuł3",
              "Content": "Oh my, oh my",
              "vendro name": "Aga",
              "Vendor tel": "513-888-258",
              "Vendor_mail": "az@mail.com"
              }}

for ad in advert.values():
    print("-" * 35)
    for cat, cont in ad.items():
        print(f"{cat}: {cont}")

print(advert.keys())

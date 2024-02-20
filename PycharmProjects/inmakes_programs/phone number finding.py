import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
phone_numbers=input("Enter your phone number with country code:")
pn=phonenumbers.parse(phone_numbers)

tz=timezone.time_zones_for_number(pn)
print("Timezon:",str(tz))
location=geocoder.description_for_number(pn,'en')
print("Location:",str(location))
sp=carrier.name_for_number(pn,'en')
print("Service provider:",str(sp))

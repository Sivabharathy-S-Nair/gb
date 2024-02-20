import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier

phone_no=input("enter your phone with country code:")
a=phonenumbers.parse(phone_no)
location=geocoder.description_for_number(a,'en')
print("Location:",str(location))
tz=timezone.time_zones_for_number(a)
print("Timezone:",str(tz))
Service=carrier.name_for_number(a,"en")
print("service provider:",str(Service))

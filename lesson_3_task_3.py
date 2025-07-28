# ВЛОЖЕННЫЕ КЛАССЫ

from address import Address
from mailing import Mailing


track = "RUS12345678"
from_address = Address("196006", "Санкт-Петербург",
                       "пр-кт Московский", "196 литера А", "5")
to_address = Address("101000", "Москва", "Мясницкая", "15", "12")
cost = "2000"


mailing = Mailing(track, from_address, to_address, cost)

print(mailing)

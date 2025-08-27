from Address import Address
from Mailing import Mailing

to_address = Address("443101", "г.Самара", "ул.Ивана Булкина", 45, 17)
from_address = Address("443101", "г.Москва", "ул.Булки Ивановой", 45, 14)


cost = 200
track = 45454545454545

my_mailing = Mailing(to_address, from_address, cost, track)
to = my_mailing.to_address
fr = my_mailing.from_address

str = "Отправление " + str(my_mailing.track) + " из " + fr.index + "," + fr.city + "," + fr.street + "," + str(fr.hous) + "-" + str(fr.flat) + " в " + to.index + "," + to.city + "," + to.street + "," + str(to.hous) + "-" + str(to.flat) + ". Стоимость: "+ str(my_mailing.cost)+" рублей."
print(str)

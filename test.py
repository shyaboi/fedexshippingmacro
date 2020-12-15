from address_parser import Parser
import re
addresss = '10431 SE 49th Court Apt 2 Belleview, FL 34420'

info = 'marthaballesteros@gmail.com 407-970-1439'

email = re.findall('\S+@\S+', info) 

ok = re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', info)

parser = Parser()
adr = parser.parse(addresss)

print(f'{adr.number.number} {adr.road.direction} {adr.road.name} {adr.road.suffix}')
print(f'{adr.locality.zip}')
print(f'{email}')
print(f'{ok}')
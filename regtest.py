from address_parser import Parser
import re


addresss = '387 View Ave apt4 Twin Falls, ID 83301'

info = 'Email:  dmmmartinez@gmail.com Phone:  +1 (956) 8574114'





email = re.findall('\S+@\S+', info) 

ok = re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', info)

parser = Parser()
adr = parser.parse(addresss)

print(f'{adr.number.number} {adr.road.direction} {adr.road.name} {adr.road.suffix}')
print(f'{adr.text}')
print(f'{email[0]}')
print(f'{ok[0]}')
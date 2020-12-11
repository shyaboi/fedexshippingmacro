import re

phoneMessy = '(920)-7167-896'

phone = re.sub('[^A-Za-z0-9]+', '', phoneMessy)

print(phone)
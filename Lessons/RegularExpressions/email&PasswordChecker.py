import re

emailPattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
passwordPattern = re.compile(r"[A-Za-z0-9_$%@]{8,}\d")
email = "test@gmail.com"
password = 'hksdjfkdfkdlfs%$9'

checkEmail = emailPattern.search(email)
print(checkEmail)

checkPassword = passwordPattern.fullmatch(password)
print(checkPassword)

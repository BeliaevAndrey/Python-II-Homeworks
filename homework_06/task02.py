from sem06_modules import s06_date_check
import re


pattern = re.compile("\\d{1,2}\\.\\d{1,2}\\.\\d{1,4}")
if not s06_date_check.argv:
    print("No arguments found")
else:
    for item in s06_date_check.argv[1:]:
        if pattern.match(item):
            print("The date is right indeed"
                  if s06_date_check.checker(item)
                  else "The date is NOT right indeed")
            break
    else:
        print("Date not found")

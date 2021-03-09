# Regex for phone numbers

import re, pyperclip

phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # seperator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x) # extension word-part (optional)
    (\d{2,5}))?)        #extension number=part(optional)
''', re.VERBOSE)

# TO DO: Create a regex for email adresses

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+

''', re.VERBOSE)

# TO DO: Get Text off the clipboard

text = pyperclip.paste()

# TO DO: Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


# TO DO: Copy the extracted email/phone to the clipboard

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

print(results)

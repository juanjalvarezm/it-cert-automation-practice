import re
    
def validate_user(username, minlen):
  # Usernames can't be shorter than minlen
  # Usernames can only use letters, numbers, dots and underscores
  # Usernames can't begin with a number
  if len(username) < minlen:
      return False
  if not re.match('^[a-zA-Z0-9_.]+$', username):
      return False
  if username[0].isnumeric():
      return False
  return True
print(validate_user("blue.kale", 3)) #True
print(validate_user(" .blue.kale", 3)) #False
print(validate_user("red_quinoa", 4)) #True
print(validate_user("_re", 4)) #False


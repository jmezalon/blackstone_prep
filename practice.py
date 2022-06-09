# import re                    # using regex

def isPalindrome(s: str) -> bool:

  s = ''.join(filter(str.isalnum, s)) # using join and filter to remove non alphn char

  # s = re.sub(r'[^a-zA-Z0-9]', '', s) # using regex to remove non aphanumeric chr

  return s[::-1].lower() == s.lower() # s[::-1] reverses a string

# print(isPalindrome('racecar'))
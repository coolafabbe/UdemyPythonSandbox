#Password Generator Project
from random import randint, choice, shuffle

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordGeneration():
  def __init__(self) -> None:
    self.nr_letters = randint(8, 10)
    self.nr_symbols = randint(2, 4)
    self.nr_numbers = randint(2, 4)

  def create_password(self):
    password_letters = [choice(LETTERS) for _ in range(self.nr_letters)]
    password_symbols = [choice(SYMBOLS) for _ in range(self.nr_symbols)]
    password_numbers = [choice(NUMBERS) for _ in range(self.nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    return password

  def set_length(self, **kwargs):
    self.nr_letters = kwargs["letters"]
    self.nr_symbols = kwargs["symbols"]
    self.nr_numbers = kwargs["numbers"]
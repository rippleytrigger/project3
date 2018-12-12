import re
from django.contrib.auth.models import User

def validate_password(password):
  if not password:
      raise ValueError('Password not provided')

  if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
      raise ValueError('Password must contain 1 capital letter and 1 number')

  if len(password) < 8 or len(password) > 50:
      raise ValueError('Password must be between 8 and 50 characters')

 
def validate_username(username):
  if not username:
      raise ValueError('No username provided')

  if User.objects.filter(username=username).exists():
    raise ValueError(f'The username you provided is already in use')

  if len(username) < 5 or len(username) > 20:
    raise ValueError('Username must be between 5 and 20 characters')


def validate_email(email):
  if not email:
    raise ValueError('No email provided')

  if not re.match("[^@]+@[^@]+\.[^@]+", email):
    raise ValueError('Provided email is not an email address')


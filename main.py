print('wassup')
print('hi')
print('dean')

print('xirui')

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(os.getenv("alpha_vantage_key"))
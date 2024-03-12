import pyupbit
import os
from dotenv import load_dotenv
load_dotenv()

upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))

print(upbit.get_balance("KRW"))
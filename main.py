import random

a = ["Stunning", "Good", "Crazy"]
n = ["Compoass", "Banana", "Geek"]

def generate_band_name():
  print(f"Generated band name: {random.choice(a)} {random.choice(n)}")

generate_band_name()
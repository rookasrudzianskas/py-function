a = ["Stunning", "Good", "Crazy"]
n = ["Compoass", "Banana", "Geek"]

def generate_band_name():
    current_time = int((id(a) + id(n)) / 1000000)
    adjective_index = current_time % len(a)
    noun_index = (current_time // len(a)) % len(n)
    
    adjective = a[adjective_index]
    noun = n[noun_index]
    print(f"Generated: {adjective} {noun}")

generate_band_name()
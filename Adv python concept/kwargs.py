# KWARGS SARE VAULE KO DICTION MAI STORE KARTA HAI AGAR WOO KEY VALUE PARE MAI  HO TOH


def my_function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
my_function(name="Abhi", age=20, city="Dhanbad")
countries = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "China": "Beijing",
    "France": "Paris"
}

country = input("Enter a country: ").strip().title()

if country in countries:
    print("Capital:", countries[country])
else:
    print("Country not found in the dictionary.")
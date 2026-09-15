# Program 2: StringPlayground
# Description: A playground where I play with Strings.

name = "Prasoon Bajpai"
print("\n\nString which is going to be used: " + name + "\n")

print("\nAll uppercase, using name.upper()")
print(name.upper())
print("All lowercase, using name.lower()")
print(name.lower())

print("\nCase 1: Successfully finding the index of a character in the string, using name.find('B')")
print(name.find('B'))
print("Case 2: Successfully finding the index from which the substring starts, using name.find('Bajpai')")
print(name.find("Bajpai"))
print("Case 3: Unsuccessful in finding the index of a character in the string (works for both cases), using name.find('z')")
print(name.find('z'))

print("\nReplacing 'Prasoon' with 'GOAT' using the name.replace('Prasoon', 'GOAT;)")
print(name.replace("Prasoon", "GOAT"))

print("\nCase 1: Checking to see whether 'B' is in the string \"Prasoon Bajpai\", using - 'B' in name")
print('B' in name)
print("Case 2: Checking to see if 'n' is in the string \"Prasoon Bajpai\", using - 'n' in name")
print('n' in name)
print("Case 3: Checking to see if \"Bajpai\" is in the string \"Prasoon Bajpai\", using - \"Bajpai\" in name")
print("Bajpai" in name)
print("Case 4: Checking to see if \"Ok\" is in the string \"Prasoon Bajpai\", using - \"Ok\" in name")
print("Ok" in name)

print("\n")
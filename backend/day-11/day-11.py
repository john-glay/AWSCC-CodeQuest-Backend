names = r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-11\names.txt'
sortedNames = r'C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-11\sortedNames.txt'

with open(names, 'r') as file:
    names = file.readlines()

names.sort()

with open(sortedNames, 'w') as file: #Change "sortedNames" to "names" to write the sorted names to that file
    file.writelines(names)

print("\nNames have been sorted and written back to the file!\n")

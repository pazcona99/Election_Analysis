x = 0
while x <= 5:
    print(x)
    x = x + 1


counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

counties_tuples = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuples)):
      print(counties_tuples[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):

      print(voting_data[i]['county'])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])
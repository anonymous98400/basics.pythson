""" Consider the following list which contains the month with year
years = ["January 2023", “February 2024”, March 2023”, "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
If you have noticed, for some months, the year was wrongly mentioned instead of 2023. Write a Python program to change the month to 2023. """

years = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
for i in range(len(years)):
    if "2023" not in years[i]:
        month = years[i].split()[0]
        years[i] = month + " 2023"

print(years)

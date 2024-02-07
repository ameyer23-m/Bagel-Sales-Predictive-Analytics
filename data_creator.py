import csv
import random
from datetime import datetime, timedelta
import holidays

# Function to generate a random date within a given range
def random_date(start_date, end_date):
    return start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )

# Function to generate temperature based on month
def generate_temperature(month):
    base_temperatures = {
        1: (10, 35),   # January
        2: (13, 38),   # February
        3: (16, 42),   # March
        4: (22, 49),   # April
        5: (29, 58),   # May
        6: (37, 69),   # June
        7: (43, 75),   # July
        8: (41, 73),   # August
        9: (34, 65),   # September
        10: (25, 55),  # October
        11: (18, 43),  # November
        12: (12, 37)   # December
    }
    base_min, base_max = base_temperatures[month]
    if random.random() < 0.05:
        base_max += 10
    return random.randint(base_min, base_max)

# Set the start and end date for the data
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)

# Generate data
data = []

# Determine US holidays
us_holidays = holidays.UnitedStates()

current_date = start_date
while current_date < end_date:
    # Determine if the day is a weekend (1) or not (0)
    is_weekend = 1 if current_date.weekday() in [5, 6] else 0

    # Determine if the day is a US holiday
    is_holiday = 1 if current_date in us_holidays else 0

    # Determine the number of bagels sold based on the day of the week and month
    month = current_date.month
    if month == 7:
        bagels_sold = random.randint(120, 180)
    elif month == 6 or month == 8:
        bagels_sold = random.randint(110, 175)   
    elif month == 5 or month == 9:
        bagels_sold = random.randint(100, 165)
    elif month == 4 or month == 10:
        bagels_sold = random.randint(90, 140)
    elif month == 3 or month == 11:
        bagels_sold = random.randint(75, 120) 
    elif month == 2 or month == 12:
        bagels_sold = random.randint(60, 90)       
    else:  # Winter months
        bagels_sold = random.randint(50, 70)  # Regular sales in winter

    # Adjust sales if it's a weekend (increase by 50%)
    if is_weekend == 1:
        bagels_sold = int(bagels_sold * 1.5)  # Increase by 50% on weekends

    # Adjust sales if it's a holiday (except Christmas and Thanksgiving)
    if is_holiday == 1 and month != 12 and current_date.day not in [25, 26]:  # Exclude Christmas and Thanksgiving
        sales_increase_percentage = random.uniform(1.15, 1.25)
        bagels_sold = int(bagels_sold * sales_increase_percentage)

    # Determine sales for each type of bagel based on actual sales percentages
    everything_bagels_sold = random.randint(int(0.3 * bagels_sold), int(0.45 * bagels_sold))
    salt_bagels_sold = random.randint(int(0.2 * bagels_sold), int(0.3 * bagels_sold))
    cinnamon_bagels_sold = random.randint(int(0.03 * bagels_sold), int(0.08 * bagels_sold))

    # Calculate remaining bagels
    remaining_bagels = bagels_sold - everything_bagels_sold - salt_bagels_sold - cinnamon_bagels_sold

    # Distribute remaining bagels among plain and sesame bagels
    plain_bagels_sold = random.randint(0, remaining_bagels)
    sesame_bagels_sold = remaining_bagels - plain_bagels_sold

    # Generate temperature for the day
    temperature_F = generate_temperature(month)

    # Append data for the day to the dataset
    data.append([
        current_date.strftime("%Y-%m-%d"),
        bagels_sold,
        is_weekend,
        everything_bagels_sold,
        cinnamon_bagels_sold,
        sesame_bagels_sold,
        salt_bagels_sold,
        plain_bagels_sold,
        temperature_F,
        is_holiday
    ])

    # Move to the next day
    current_date += timedelta(days=1)

# Write data to CSV file
csv_file_path = 'bagel_shop_data.csv'
columns = ['date', 'bagels_sold', 'is_weekend', 'everything_bagels_sold', 'cinnamon_bagels_sold', 'sesame_bagels_sold', 'salt_bagels_sold', 'plain_bagels_sold', 'temperature_F', 'is_holiday']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been created.")

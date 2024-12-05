import csv
from nutrition.models import Food  


file_path = "foods.csv"

def populate_foods():
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
    
            Food.objects.create(
                name=row['name'],
                calories=row['calories'],
                protein=row['protein'],
                carbs=row['carbs'],
                fats=row['fats'],
                serving_size=row['serving_size']
            )
    print("Database populated with food data!")

# Run the function
populate_foods()
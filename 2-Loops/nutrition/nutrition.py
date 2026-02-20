chosen_fruit = input("Fruit: ").lower()

fruit_dict = [
    {"fruit": "apple", "Calories": "130"},
    {"fruit": "avocado", "Calories": "50"},
    {"fruit": "banana", "Calories": "110"},
    {"fruit": "cantaloupe", "Calories": "50"},
    {"fruit": "grapefruit", "Calories": "60"},
    {"fruit": "grapes", "Calories": "90"},
    {"fruit": "honeydew melon", "Calories": "50"},
    {"fruit": "kiwifruit", "Calories": "90"},
    {"fruit": "lemon", "Calories": "15"},
    {"fruit": "lime", "Calories": "20"},
    {"fruit": "nectarine", "Calories": "50"},
    {"fruit": "orange", "Calories": "80"},
    {"fruit": "peach", "Calories": "60"},
    {"fruit": "pear", "Calories": "100"},
    {"fruit": "pineapple", "Calories": "50"},
    {"fruit": "plumes", "Calories": "70"},
    {"fruit": "strawberries", "Calories": "50"},
    {"fruit": "sweet cherries", "Calories": "100"},
    {"fruit": "tangerine", "Calories": "50"},
    {"fruit": "watermelon", "Calories": "80"},
]

for current_fruit in fruit_dict:
    if current_fruit["fruit"] == chosen_fruit:
        print(f'{current_fruit["Calories"]}')
        break

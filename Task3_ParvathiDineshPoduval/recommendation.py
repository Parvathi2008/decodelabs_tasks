print("=" * 60)
print("WELCOME TO THE FOOD RECOMMENDATION SYSTEM ")
print("=" * 60)

veg_food = {
    "spicy": [
        "Paneer Tikka",
        "Veg Manchurian",
        "Chilli Paneer",
        "Spicy Noodles"
    ],
    "sweet": [
        "Gulab Jamun",
        "Rasgulla",
        "Chocolate Cake",
        "Ice Cream"
    ],
    "healthy": [
        "Fruit Salad",
        "Vegetable Soup",
        "Sprouts Salad",
        "Mixed Vegetable Curry"
    ],
    "fast food": [
        "Veg Burger",
        "Veg Pizza",
        "French Fries",
        "Veg Sandwich"
    ],
    "south indian": [
        "Masala Dosa",
        "Idli",
        "Uttapam",
        "Vegetable Upma"
    ],
    "north indian": [
        "Paneer Butter Masala",
        "Chole Bhature",
        "Dal Makhani",
        "Naan"
    ]
}

nonveg_food = {
    "spicy": [
        "Chicken Biryani",
        "Chicken 65",
        "Mutton Curry",
        "Spicy Chicken Wings"
    ],
    "sweet": [
        "Caramel Custard",
        "Chocolate Mousse",
        "Ice Cream",
        "Brownie"
    ],
    "healthy": [
        "Grilled Chicken",
        "Boiled Eggs",
        "Grilled Fish",
        "Chicken Salad"
    ],
    "fast food": [
        "Chicken Burger",
        "Chicken Pizza",
        "Fried Chicken",
        "Chicken Wrap"
    ],
    "south indian": [
        "Chicken Sukka",
        "Fish Curry",
        "Prawn Ghee Roast",
        "Chicken Biryani"
    ],
    "north indian": [
        "Butter Chicken",
        "Chicken Tikka",
        "Mutton Rogan Josh",
        "Chicken Kebab"
    ]
}

while True:

    print("\n========== MAIN MENU ==========")
    print("Veg")
    print("Non-Veg")
    print("\nType 'exit' to quit.")

    main_choice = input("\nEnter your choice: ").lower().strip()

    if main_choice == "exit":
        print("\n🍴 Thank you for using the Food Recommendation System!")
        print("Goodbye! ")
        break

    elif main_choice == "veg":
        food = veg_food

    elif main_choice == "non veg" or main_choice == "non-veg":
        food = nonveg_food

    else:
        print("\n Invalid choice!")
        print("Please enter Veg, Non-Veg or Exit.")
        continue

    while True:

        print("\n----------- FOOD CATEGORIES -----------")
        print("Spicy")
        print("Sweet")
        print("Healthy")
        print("Fast Food")
        print("South Indian")
        print("North Indian")
        print("\nType 'back' to return to the Main Menu.")
        print("Type 'exit' to quit.")

        category = input("\nEnter a category: ").lower().strip()

        if category == "exit":
            print("\n Thank you for using the Food Recommendation System!")
            print("Goodbye!")
            exit()

        elif category == "back":
            break

        elif category in food:

            print("\nRecommended Foods:\n")

            for item in food[category]:
                print("->", item)

        else:
            print("\n Invalid category!")
            print("Please choose from the available categories.")

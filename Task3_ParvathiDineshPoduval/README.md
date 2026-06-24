# Task 2: Food Recommendation System

## Project Description

This project is a simple rule-based Food Recommendation System developed using Python. It recommends food items based on the user's preferences using predefined rules and conditional logic.

The application first asks the user to choose between **Veg** and **Non-Veg**. Based on the user's selection, it displays different food categories such as **Spicy**, **Sweet**, **Healthy**, **Fast Food**, **South Indian**, and **North Indian**. The system then recommends suitable food items from the selected category.

The application continues running until the user chooses to exit, allowing multiple recommendations during a single session.

---

## Objective

Develop a recommendation system that:

- Accepts user preferences
- Matches preferences using rule-based logic
- Recommends suitable food items
- Allows continuous interaction until the user exits

---

## Features

- Separate menus for Veg and Non-Veg food
- Food recommendations based on user-selected categories
- Categories include:
  - Spicy
  - Sweet
  - Healthy
  - Fast Food
  - South Indian
  - North Indian
- Continuous menu-driven interaction
- Back option to return to the main menu
- Exit option available from any menu
- Input validation with appropriate error messages

---

## Technologies Used

- Python 3
- Visual Studio Code (VS Code)

---

## Project Structure

```
Task2/
│── recommendation_system.py
│── README.md
```

---

## Sample Output

```
============================================================
WELCOME TO THE FOOD RECOMMENDATION SYSTEM
============================================================

========== MAIN MENU ==========
Veg
Non-Veg

Type 'exit' to quit.

Enter your choice: veg

----------- FOOD CATEGORIES -----------
Spicy
Sweet
Healthy
Fast Food
South Indian
North Indian

Type 'back' to return to the Main Menu.
Type 'exit' to quit.

Enter a category: healthy

Recommended Foods:

- Fruit Salad
- Vegetable Soup
- Sprouts Salad
- Mixed Vegetable Curry

Enter a category: back
```

---

## Concepts Used

- Variables
- User Input
- Dictionaries
- Lists
- Nested Loops
- Conditional Statements (`if`, `elif`, `else`)
- Rule-Based Recommendation Logic
- Pattern Matching
- Input Validation

---

## Learning Outcomes

Through this project, I learned how to:

- Build a menu-driven recommendation system
- Store and retrieve data using dictionaries
- Implement nested loops for continuous interaction
- Validate user input and handle invalid entries
- Apply rule-based logic to generate recommendations
- Improve logical thinking and problem-solving skills

---

## Future Enhancements

- Add recommendations based on budget
- Include meal categories such as Breakfast, Lunch, and Dinner
- Display calorie and nutritional information
- Recommend foods based on dietary restrictions
- Integrate a database for dynamic recommendations
- Develop a graphical user interface (GUI)

---

## Author

**Parvathi Dinesh Poduval**

AI Internship Project – Task 3

DecodeLabs AI Internship

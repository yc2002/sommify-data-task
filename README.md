# SommifyAI data task

## Title: Identification and Extraction 

## Objective

Create a Python function that can efficiently identify and extract non-English and English recipe titles from a given input string. The function should be designed to handle multiple titles simultaneously using vectorization techniques. You should focus on accuracy over speed but the function should be able to process a large number of titles in a reasonable amount of time.

## Task Description

Your task is to implement a Python function that takes a string as input and separates the non-English and English parts of the title. The function should be able to handle cases where the non-English title is a substring of the entire title. Additionally, the function should be designed to process multiple titles efficiently using vectorization techniques.

## Example

```
"Yogurtlu Kebab - Kofta With Tomato Sauce and Yogurt" ----> non-english title (Yougurtlu Kebab) + english title (Kofta With Tomato Sauce and Yogurt)
"Vegetable Biryani" ----> english title
"Kalya E Khaas (Traditional South African Chicken Curry)" ----> non-english title (Kalya E Khaas) + english title (Traditional South African Chicken Curry)
"Chicken and Rice" ----> english title
"Kibbeh" ----> non-english title (Kibbeh)
"Cantaloupe Salad (Insalata Di Melone)" ----> non-english title (Insalata Di Melone) + english title (Cantaloupe Salad)
```

## Steps

1. Fork this repository.
2. Download data using script provided in `data` folder.
```bash
python data/download_data.py
```
3. Implement your solution in `solution.py` file. For developing you can use `solution.ipynb` file but make sure to copy your solution to `solution.py` file. Additional data preprocessing can be added it is welcome but not required.
```python
def extract_titles(titles: list[str]) -> list[tuple[str, str]]:
```
4. Push your solution to your forked repository.
5. Contact us with link to your forked repository.

## Data notes

1. title : title of the recipe. You should work with this column.
2. recipe_id : unique id for each recipe, not required for the task (only for reference)


| title                                                  | recipe_id |
|--------------------------------------------------------|-----------|
| Egyptian Lentil Soup                                   | 2610      |
| Egyptian Green Beans with Carrots                      | 2611      |
| Egyptian Bamia                                         | 2612      |
| Magpie's Easy Falafel Cakes                            | 2613      |
| Dukkah                                                 | 2614      |
| Om Ali                                                 | 2615      |
| Rice Pudding with Lemon Juice and Caramelized Onion    | 2616      |
| (Egyptian Kishk)                                       |           |
| Couscous with Olives and Sun-Dried Tomato              | 2617      |
| Fava Bean Breakfast Spread                             | 2618      |
| Koshary                                                | 2619      |
| Egyptian Wheat Porridge (Belila)                       | 2620      |
| Fava Beans in Tahini Sauce                             | 2621      |
| Egyptian Feta Cheese Omelet Roll                       | 2622      |
| Quick and Easy Egyptian Chicken Broth                  | 2623      |


## Notes

You are expected to write a clean and well-documented code, and provide a brief explanation of your implementation choices. There are no restrictions for using AI tools such a ChatGPT or Github Copilot. However, you are expected to explain your implementation choices in the README file.

### Contact

```
Jacob : jacob@sommify.ai (Non task related questions)
William : william@sommify.ai (Questions about the task)
```

## Submission

Write here your submission description/notes.

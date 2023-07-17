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
| Rice Pudding with Lemon Juice and Caramelized Onion (Egyptian Kishk)       | 2616      |
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


## Approach explanation (Split+Detect)

For each Title, there are 4 different structures:
1. English
2. Non-English
3. English (Splitter) Non-English
4. Non-English (Splitter) English

Here Types 1 and 2 are similar where they only contain alphabetic characters. Types 3 and 4 contain two parts which are split by '-' or '()'. We can identify different parts of the title by looking for splitters ('-' and '()').

Once we have found the different parts of the title, we can utilize language detectors to identify whether a part is in English or not.

## Language Detection

'fasttext' library provides pre-trained language detection models with high accuracy and low time cost and is the most efficient among popular language detection tools like langdetect, langid and spaCY. We will implement our approach based on 'fasttext'.

## Non-language-specific part
'Fried Rice With Shrimp (1953)', 'Thai Beef Curry  (2)', 'Thai Coconut Lime: Infused Skewers (#2)', 'Rogan Josh (2)'
Above are some examples of the cases when we will have non-language-specific parts like digits and special characters (e.g. 1953,#2,2), we will filter out these parts using list comprehension(Efficient).


## Vectorization
Using list comprehension and pandas/numpy can benefit from the efficiency of vectorization. In the main programme, we can use pandas. apply() to apply fasttext's predict() in vectorized way to improve efficiency.

## Potential approach (Heuristic)

To determine whether a part is in English or not, we can utilize an English-food-recipe vocabulary to help us. A part containing a word from the Vocabulary is more likely to be in English.

Trade-off:
1. Could achieve similar accuracy if the vocabulary size is large enough and relevant
2. Different languages may share the same word could reduce accuracy
3. Less expensive than language detection

Due to the limitation of time and resources, this approach is not taken.

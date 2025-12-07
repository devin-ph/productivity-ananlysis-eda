# Productivity EDA Project

This project explores the relationship between daily productivity and various factors such as weather, mood, music, and study hours. It is a small-scale exploratory data analysis (EDA) project using my synthetic data collected over 3 months.

---

## 🧰 Libraries Used

- Python 3.14
- pandas
- numpy
- matplotlib
- seaborn

---

## 📊 Dataset Description

| Column          | Type       | Description |
|-----------------|------------|-------------|
| Date            | datetime   | Day of the record |
| Day_of_Week     | categorical| Monday to Sunday |
| Weather         | categorical| Sunny, Cloudy, Rainy, etc. |
| Temperature     | float      | Temperature in °C |
| Mood_Score      | int        | Mood rating (1-10) |
| Music           | categorical| Genre of music listened to |
| Study_Hours     | float      | Time spent studying in hours |

---

## 🔍 Analyses Performed

1. **Data Overview** – size, columns, missing values, data types.  
2. **Univariate Analysis** – distribution plots for individual variables.  
3. **Bivariate Analysis** – relationships between two variables (e.g., Mood vs Study Hours).  
4. **Correlation Analysis** – numeric correlation heatmaps.  
5. **Insights Summary** – key takeaways and patterns related to productivity.

---

## ⚡ Usage

**Clone the repository:**

```bash
git clone https://github.com/devin-ph/productivity-eda.git
cd productivity-eda
```
## 📌 Notes
- Open notebooks in Jupyter or VSCode.
- Run ***0.project_setup.ipynb*** first to load libraries, dataset, and helper functions.
- All notebooks are modular; they can be run independently after running ***0.project_setup.ipynb***.
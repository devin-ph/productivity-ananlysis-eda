# Productivity EDA Project

This project explores the relationship between daily productivity and various factors such as weather, mood, music, and study hours. It is a small-scale exploratory data analysis (EDA) project using synthetic data collected over 3 months.

---

## 🧰 Libraries Used

- Python 3.14
- pandas
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
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devin-ph/productivity-eda/)
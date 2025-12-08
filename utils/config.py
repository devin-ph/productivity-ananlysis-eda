import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
sns.set_theme(style='whitegrid')

def load_data():
    return pd.read_csv("../data/productivity_raw.csv")
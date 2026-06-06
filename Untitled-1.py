# %%
import pandas as pd

url = "https://raw.githubusercontent.com/Wonhee4132/ALP-Statistics/refs/heads/main/M5_World_Championship.csv"

df = pd.read_csv(url)

print(df.head())
print(df.info())

# %%
desc = df.describe()

desc

# %%
import pandas as pd

stats = pd.DataFrame({
    "Mean": df.mean(numeric_only=True),
    "Median": df.median(numeric_only=True),
    "Std Dev": df.std(numeric_only=True),
    "Min": df.min(numeric_only=True),
    "Max": df.max(numeric_only=True)
})

stats

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))
ax.axis('off')

table = ax.table(
    cellText=stats.round(2).values,
    colLabels=stats.columns,
    rowLabels=stats.index,
    loc='center'
)

plt.savefig("descriptive_statistics.png",
            bbox_inches="tight",
            dpi=300)

plt.show()

# %%
df.head(20)



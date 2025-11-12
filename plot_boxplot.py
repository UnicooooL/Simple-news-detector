import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("latency_results.csv")

plt.figure(figsize=(8, 5))
df.boxplot(column="Latency(ms)", by="CaseID")

plt.title("API Latency per Test Case (100 requests each)")
plt.suptitle("")  
plt.xlabel("Test Case ID")
plt.ylabel("Latency (ms)")
plt.grid(True, linestyle="--", alpha=0.5)

means = df.groupby("CaseID")["Latency(ms)"].mean()

for i, mean_val in enumerate(means, start=1):
    plt.text(i, mean_val + 20, f"Avg: {mean_val:.2f} ms", 
             ha="center", color="red", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.savefig("latency_boxplot_with_avg.png")
plt.show()

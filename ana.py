import matplotlib.pyplot as plt
import pandas as pd

# Quarterly MRR growth data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR Growth": [2.43, 5.11, 10.77, 12.65]
}

df = pd.DataFrame(data)
industry_target = 15
average = df["MRR Growth"].mean()

print("Quarterly MRR Growth:")
print(df)
print(f"\nAverage MRR Growth: {average:.2f}")
print(f"Industry Target: {industry_target}")

# Visualization
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["MRR Growth"], marker="o", label="MRR Growth")
plt.axhline(industry_target, color="r", linestyle="--", label="Industry Target (15)")
plt.title("Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth")
plt.legend()
plt.grid(True)
plt.savefig("mrr_growth_trend.png", dpi=300, bbox_inches="tight")
plt.show()

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset
df = pd.read_csv("Global Student Placement & Salary Dataset.csv")

print(df.info())
print(df.isnull().sum())

df["placement"] = (df["placement_status"] == "Placed").astype(int)

# Effects of Internships on Placement Rates
placement_rates = df.groupby("internship_count")["placement"].mean().round(3)
print("Placement rates by internship count:")
print(placement_rates)

df["strong_profile"] = (df["internship_count"] >= 1).astype(int)
strong_profile_rates = df.groupby("strong_profile")["placement"].mean().round(3)
print("\nPlacement rates by strong profile:")
print(strong_profile_rates)

# Effects of Internships on Graduate Salaries
placed = df[df["placement"] == 1].copy()

salary_by_internship = placed.groupby("internship_count")["salary"].mean().round(0)
print("\nAverage salary by internship count:")
print(salary_by_internship)

# Effects of Internships on Placement Rates Graph
placement_rates.plot(kind="bar")
plt.ylabel("Placement Probability")
plt.xlabel("Number of Internships")
plt.title("Effect of Internship Experience on Placement Outcomes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

####### NERD OUT #######
x = placement_rates.index.values
y = placement_rates.values

# Quadratic
coeffs = np.polyfit(x, y, 2)
a, b, c = coeffs
curve = np.poly1d(coeffs)

# Second derivative
second_derivative = 2 * a

# Curve
x_smooth = np.linspace(x.min(), x.max(), 200)
y_smooth = curve(x_smooth)
plt.figure()

plt.bar(x, y, width=0.6)
plt.plot(x_smooth, y_smooth, linewidth=2)
plt.scatter(x, y, zorder=3)

plt.ylabel("Placement Probability")
plt.xlabel("Number of Internships")
plt.title("Effect of Internship Experience on Placement Outcomes")
plt.xticks(x)

#Annotation
if second_derivative < 0:
    concavity_text = f"Second derivative = {second_derivative:.4f}\n→ Concave"
else:
    concavity_text = f"Second derivative = {second_derivative:.4f}\n→ Not concave"

plt.text(0.05, 0.9, concavity_text, transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()
####### NERD OUT #######

# Effects of Internships on Graduate Salaries
placed["internship_binary"] = (placed["internship_count"] >= 1).astype(int)

salary_comparison = placed.groupby("internship_binary")["salary"].mean().round(0)
print("\nAverage salary by internship experience (0 vs ≥1):")
print(salary_comparison)

# Effects of Internships on Graduate Salaries Graph
salary_comparison.plot(kind="bar")
plt.title("Average Salary by Internship Experience")
plt.ylabel("Average Salary (USD)")
plt.xlabel("Internship Experience (0 vs ≥1)")
plt.xticks([0, 1], ["No Internship", "At Least 1 Internship"], rotation=0)
plt.tight_layout()
plt.show()

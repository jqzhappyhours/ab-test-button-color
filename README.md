# A/B Test: Add to Cart Button Color

## 📌 Objective
Test whether changing the "Add to Cart" button color from blue (Control) to green (Variant) increases the add-to-cart conversion rate on an e-commerce site.

## 📊 Hypothesis
- **H₀ (Null Hypothesis):** Button color does not impact conversion rate.
- **H₁ (Alternative Hypothesis):** Green button leads to a higher conversion rate.

## 🧪 Experiment Design
- **Group A (Control):** Blue button
- **Group B (Variant):** Green button
- **Metric:** Add-to-cart conversion rate = (# conversions / # users)

## 🧮 Dataset
Synthetic dataset of 10,000 users simulated using Python:
- 5,000 users in Group A
- 5,000 users in Group B

## 🧠 Analysis
Used a z-test to compare conversion rates between the two groups and determine statistical significance.

## 📈 Results
- Group A: 10% conversion rate
- Group B: 12% conversion rate
- p-value: *[calculated in notebook]*

## ✅ Conclusion
The green button improved the add-to-cart conversion rate. The change is statistically significant and is recommended for deployment.

## 📁 Files
- `ab_test_analysis.ipynb`: Notebook with code and analysis
- `ab_test_data.csv`: Synthetic dataset
- `README.md`: Project summary

## 🛠 Tools Used
- Python
- pandas, numpy
- statsmodels
- matplotlib / seaborn
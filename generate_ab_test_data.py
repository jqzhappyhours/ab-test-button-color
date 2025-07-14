import numpy as np
import pandas as pd

def generate_ab_test_data(n_users = 10000, seed = 42, save_path = "ab_test_data.csv"):
    np.random.seed(seed)

    users = range(1, n_users + 1)
    groups = np.random.choice(['A', 'B'], size = n_users)

    conversion_rate_A = 0.10 # 10% for blue button
    conversion_rate_B = 0.12 # 12% for green button

    converted = [
        1 if (group == 'A' and np.random.rand() < conversion_rate_A) or
             (group == 'B' and np.random.rand() < conversion_rate_B) else 0
             for group in groups
    ]

    df = pd.DataFrame({
        'user_id' : users,
        'group' : groups,
        'converted' : converted
    })

    df.to_csv(save_path, index= False)
    print(f"✅ Data saved to {save_path}")

if __name__=="__main__":
    generate_ab_test_data()
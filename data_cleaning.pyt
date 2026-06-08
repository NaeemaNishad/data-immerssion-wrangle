import pandas as pd
import numpy as np

file_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\Ecommerce_Internship_Project\ecommerce_user_behavior_8000.csv"
df = pd.read_csv(file_path)

print("Starting Data Wrangling Pipeline...\n")

initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
print(f"Dropped {initial_rows - df.shape[0]} exact duplicate rows.")

df.dropna(subset=['user_id'], inplace=True)

df['gender'] = df['gender'].fillna('Unknown')
df['device_type'] = df['device_type'].fillna('Unknown')

numerical_cols = ['age', 'time_on_site', 'pages_viewed', 'previous_purchases', 
                  'cart_items', 'avg_session_time', 'bounce_rate']
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

binary_cols = ['discount_seen', 'ad_clicked', 'returning_user', 'purchase']
for col in binary_cols:
    df[col] = df[col].fillna(0)

int_cols = ['user_id', 'age', 'pages_viewed', 'previous_purchases', 'cart_items', 
            'discount_seen', 'ad_clicked', 'returning_user', 'purchase']
for col in int_cols:
    df[col] = df[col].astype(int)

age_bins = [0, 25, 45, 65, np.inf]
age_labels = ['Gen Z / Youth', 'Millennials / Young Adults', 'Gen X / Middle Aged', 'Seniors']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

df['pages_per_minute'] = round(df['pages_viewed'] / (df['time_on_site'] + 1e-5), 2)

output_path = r"C:\Users\naeem\OneDrive\Desktop\Naeema\Ecommerce_Internship_Project\cleaned_ecommerce_user_behavior_2026.csv"
df.to_csv(output_path, index=False)

print("\n--- CLEANED DATA SUMMARY ---")
df.info()
print(f"\nPipeline Executed Successfully! Cleaned file saved to: {output_path}")

import pandas as pd

# Load JSON
df = pd.read_json(r"C:\Users\abdul\Desktop\my_spotify_data\Streaming_History_Audio_2025_6.json")

# Save as Excel file
df.to_excel(r"C:\Users\abdul\Desktop\my_spotify_data\StreamingHistory2025.xlsx", index=False)

print("✅ Saved as Excel (.xlsx)")

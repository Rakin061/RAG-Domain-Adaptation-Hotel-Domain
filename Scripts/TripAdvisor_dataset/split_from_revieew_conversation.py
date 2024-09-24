
import pandas as pd
import csv
from Split_to_chunks import split_text_into_chunks

# Initialize the output CSV with headers
# with open('csv/knowledgebase_review.csv', 'a', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['title', 'text'])

# Read the CSV file using pandas
df = pd.read_csv('csv/Trip advisor Conversations_review.csv', encoding='utf-8')

for index, row in df.iterrows():
    title = row['title']
    text = row['text']
    print(title)
    chunks = split_text_into_chunks(text)

    with open('csv/knowledgebase_review.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for chunk in chunks:
            writer.writerow([title, chunk])

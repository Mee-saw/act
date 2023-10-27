import os
import openai
import pandas as pd
import time

# Load the file and fill the NAN values
df = pd.read_json('datafinal.json')
df["CodeList"].fillna("", inplace=True)

openai.api_key = "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"

# Parameters for handling timeouts and rate limits
DELAY_BETWEEN_CALLS = 5  # Delay of 5 seconds between API calls
MAX_RETRIES = 5  # Maximum number of retries upon failure

# Define a function to process a batch of text
def process_batch(batch_texts):
    responses = []
    for x in batch_texts:
        for _ in range(MAX_RETRIES):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an assistant that extracts programming code snippets from text paragraphs."
                        },
                        {
                            "role": "user",
                            "content": "Extract and return any code present in the following paragraph. If there's no code, return 'NULL'. Here's the paragraph: '{}'".format(x)
                        }
                    ]
                    ,
                    temperature=0.5,
                    max_tokens=250,
                )
                res = response.choices[0].message["content"]
                responses.append(res)
                break  # Break out of the retry loop upon success
            except openai.error.OpenAIError as e:
                print(f"Error encountered: {e}. Retrying...")
                time.sleep(DELAY_BETWEEN_CALLS)
    return responses

# Process the dataframe in batches
BATCH_SIZE = 6
result = []
for start in range(0, len(df), BATCH_SIZE):
    end = start + BATCH_SIZE
    batch_texts = df['Text'][start:end].tolist()
    print(f"Processing rows {start + 1} to {min(end, len(df))}...")
    batch_results = process_batch(batch_texts)
    df.loc[start:end-1, 'CodeList'] = batch_results
    time.sleep(DELAY_BETWEEN_CALLS)  # Delay between batches

# Save results to CSV
df.to_csv("Codelist.csv")

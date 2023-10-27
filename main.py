import os
import openai
import pandas as pd

#load the file and fill the NAN values
df = pd.read_json('datafinal.json')
df["CodeList"].fillna("", inplace=True)

result = list()
for i in range(0,20):
  x = df['Text'][i]
  openai.api_key = "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"
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a NLP Engineer"
      },
      {
        "role": "user",
        "content": "Identify and return only the code in this paragraph, if there is no code return NULL - {}".format(x)
      },
    ],
    temperature=1,
    max_tokens=537,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  res = response.choices[0].message["content"]
  result.append(res)


result = pd.DataFrame(result)
result.to_csv("Final.csv")
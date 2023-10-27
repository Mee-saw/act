import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "system",
      "content": "You are a NLP Engineer"
    },
    {
      "role": "user",
      "content": "Identify and return only the code in this paragraph, if there is no code return NULL - In software development, problem-solving is a critical skill. Developers are often faced with complex issues that require creative solutions. This is where a good understanding of algorithms and data structures can come in handy.\n\nFor instance, consider a problem where you need to find the largest number in an array of integers. Here's a simple C++ function that does this: int findMax(int arr[], int n) { int max = arr[0]; for (int i = 1; i < n; i++) if (arr[i] > max) max = arr[i]; return max; } This function iterates over the array and keeps track of the largest number it finds. It's a simple solution, but it's effective."
    },
  ],
  temperature=1,
  max_tokens=537,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
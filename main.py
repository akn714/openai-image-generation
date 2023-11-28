from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('OPENAI_API_KEY'))

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# response = client.images.generate(
#   model="dall-e-3",
#   prompt="airplane",
#   size="1024x1024",
#   quality="standard",
#   n=1,
# )

response = client.images.create_variation(
  image=open("image.png", "rb"),
  n=2,
  size="1024x1024"
) 

image_url = response.data[0].url

print(image_url)

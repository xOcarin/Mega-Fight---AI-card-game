from openai import OpenAI

#get API key from file
path = "../apikey.txt"
with open(path, 'r') as file:
    apiKey = file.readline().strip()

client = OpenAI(api_key = apiKey)




import random
import json


def GenerateImage(subject1, subject2, ability1, ability2):
    img_prompt = ("describe me a battle between these two fighters and their unique abilities:"
                  "Figther 1:" + subject1 + " abillity 1:" + ability1 + ""
                  "Figther 2:" + subject2 + " abillity 2:" + ability2 + ""
                  "Depict an epic battle. "
                  "Remember, only  " + subject1 + "has " + ability1 + " and only " + subject2 + " has " + ability2 + ""
                  "Make sure they are only using their own abilities. "
                  "Make sure they are not each others abilities")

    response = client.images.generate(
        model="dall-e-3",
        prompt=img_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url


def GeneratePrompt(subject1, subject2, ability1, ability2):

  img_prompt = ("describe me a battle between these two fighters and their unique abilities:"
                "Figther 1:" + subject1 + " abillity 1:" + ability1 + ""
                "Figther 2:" + subject2 + " abillity 2:" + ability2 + ""
                "Depict an epic battle. "
                "Remember, only  " + subject1 + "has " + ability1 + " and only " + subject2 + " has " + ability2 + ""
                "Make sure they are only using their own abilities. "
                "Make sure they are not each others abilities")

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "You are a helpful assistant designed to output a detailed description of a fight between two indiviuiduals with special powers."
                                    "to be given to an AI image generator"},
      {"role": "user", "content": img_prompt}
    ]
  )
  print(response.choices[0].message.content)
  prompt = "Depict a battle between " + "Figther 1:" + subject1 + " with special abillity: " + ability1 + (" Figther 1:"
           "") + subject2 + " with special abillity: " + ability2 + "No text. The battle will go like this: " + response.choices[0].message.content
  return prompt




#obtain Fighters(animal)
with open('static/fighters.json', 'r') as file:
    fighter_names = json.load(file)

#obtain Powers
with open('static/powers.json', 'r') as file:
    power_names = json.load(file)


current_fighter_index = 0;
current_power_index = 0;
random.shuffle(fighter_names)
random.shuffle(power_names)
def getFighter():
    global current_fighter_index
    fighter = fighter_names[current_fighter_index]
    current_fighter_index += 1
    return fighter


def getPower():
    global current_power_index
    power = power_names[current_power_index]
    current_power_index += 1
    return power








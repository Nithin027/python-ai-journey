import requests

def get_jokes(category):
    url = "https://official-joke-api.appspot.com/random_joke/{category}/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            data = data[0]
        print(f"\nCategory: {category.upper()}")
        print(f"Setup: {data['setup']}")
        print(f"Punchline: {data['punchline']}")

    else:
        print(f"Couldn't fetch joke: {response.status_code}")

def get_and_save_jokes():
    with open("jokes.txt", "w") as file:
        for i in range(3):
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                setup = data['setup']
                punchline = data['punchline']
                
                # print it
                print(f"Joke {i+1}:")
                print(f"Setup: {setup}")
                print(f"Punchline: {punchline}\n")
                
                # save to file
                file.write(f"Joke {i+1}: {setup} - {punchline}\n")
    
    print("All jokes saved to jokes.txt!")

get_and_save_jokes()




'''This extracts thousands of quotes from a json file. and saves them as a pickle(quotes.pkl)'''

import json
import random
import pickle

with open("quotes.json", 'r') as f:
    data = json.load(f)

gen = (random.sample(range(len(data)), k=random.randint(20,50)))
quotes = [data[i]['Quote'] for i in gen]
with open("quotes.pkl", 'wb') as f:
    pickle.dump(quotes, f)

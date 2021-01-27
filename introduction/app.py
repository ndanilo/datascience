import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def printModel(obj, title = None):
    if not title is None:
        print(title)
    print(f'{obj}\n')

movies = pd.read_csv("files/movies.csv")
notes = pd.read_csv("files/ratings.csv")

printModel(movies.head(), 'movies structure:')
printModel(notes.head(), 'notes structure:')

printModel(notes.rating.mean(), 'notes rating mean:')

notes.rating.plot(kind='hist')

plt.title('Model of ploting chart')
plt.show()

groupMovies = notes.groupby('movieId').mean()
printModel(groupMovies.head(), 'group movies by mean')

groupMovies.rating.plot(kind='hist')
plt.title('group movies by mean')
plt.show()
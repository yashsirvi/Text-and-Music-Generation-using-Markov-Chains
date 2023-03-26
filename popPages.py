from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

top100pages = """United States
Donald Trump
Elizabeth II
India
Barack Obama
Cristiano Ronaldo
World War II
United Kingdom
Michael Jackson
Elon Musk
Sex
Lady Gaga
Adolf Hitler
Eminem
Lionel Messi
Game of Thrones
World War I
The Beatles
Justin Bieber
Canada
Freddie Mercury
Kim Kardashian
Johnny Depp
Steve Jobs
Dwayne Johnson
Michael Jordan
Australia
List of presidents of the United States
The Big Bang Theory
Taylor Swift
Stephen Hawking
List of highest-grossing films
China
Russia
New York City
Japan
Kanye West
List of Marvel Cinematic Universe films
Abraham Lincoln
LeBron James
Charles III
Darth Vader
Star Wars
Miley Cyrus
Germany
September 11 attacks
Leonardo DiCaprio
Kobe Bryant
Selena Gomez
Joe Biden
Tom Cruise
Rihanna
Albert Einstein
Academy Awards
Prince Philip, Duke of Edinburgh
Harry Potter
Elvis Presley
The Walking Dead (TV series)
Scarlett Johansson
Lil Wayne
Tupac Shakur
Angelina Jolie
Queen Victoria
Jeffrey Dahmer
John F. Kennedy
COVID-19 pandemic
Diana, Princess of Wales
Marilyn Monroe
Keanu Reeves
Arnold Schwarzenegger
How I Met Your Mother
Chernobyl disaster
France
Ariana Grande
Jennifer Aniston
Breaking Bad
Meghan, Duchess of Sussex
Muhammad Ali
Will Smith
Ted Bundy
Pablo Escobar
Mila Kunis
Vietnam War
Mark Zuckerberg
Manchester United F
William Shakespeare
Titanic
Tom Brady
Jay-Z
Singapore
Earth
Bill Gates
Winston Churchill
Bruce Lee
Nicki Minaj
Israel
Princess Margaret, Countess of Snowdon
John Cena
Charles Manson
Ryan Reynolds
Brad Pitt
Vladimir Putin"""

# Split the string into a list of strings
top100pages = top100pages.split('\n')

for i in range(0,102):
    top100pages[i]=top100pages[i].replace(' ','_')

    # Specify url of the web page
    source = urlopen('https://en.wikipedia.org/wiki/'+top100pages[i]).read()
    print(source)
    # Make a soup 
    soup = BeautifulSoup(source,'lxml')

    # Extract the plain text content from paragraphs
    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))

    # Extract text from paragraph headers
    heads = []
    for head in soup.find_all('span', attrs={'mw-headline'}):
        heads.append(str(head.text))

    # Interleave paragraphs & headers
    text = [val for pair in zip(paras, heads) for val in pair]
    text = '\n'.join(text)

    # Drop footnote superscripts in brackets
    text = re.sub(r"\[.*?\]+", '', text)

    # Replace '\n' (a new line) with '' and end the string at $1000.
    # text = text.replace('\n', '')[:-11]
    file1 = open("wikiscrape.txt", "a")  # append mode
    file1.write(top100pages[i]+"\n")
    file1.write(text)
    file1.close()
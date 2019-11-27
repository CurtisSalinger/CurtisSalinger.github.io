#Homework 4 Curtis Salinger
from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt
import numpy
import itertools

#Create empty variables for all of the different data sets I want to pull
name = ''
names = []
elect = ''
percentage = ''
totals = {}
winners = {}
d_states = {}
r_states = {}
e_votes = {}
e_votesd = {}
e_votesr = {}
e_votesboth = {}
e_votessorted = {}
colors = []
xaxisd = []
xaxisr = []
yaxisd = []
yaxisr = []

#Load the HTML code from the webiste
url = 'https://www.politico.com/2016-election/results/map/president/'
html = requests.get(url).text
bs = BeautifulSoup(html)
states = bs.find_all('table', class_='results-table')
heads = bs.find_all('h3')

#Scrape the data I want and put it into the variables created above
for i in range(len(states)):
    name = heads[i+2].text[59:61]
    nominees = states[i].find_all('span',class_= 'name-combo')
    n1 = nominees[0].text[9:]
    n2 = nominees[1].text[2:]
    percentage = states[i].find_all('span', class_= 'number')
    p1 = float(percentage[0].text[:-1])
    p2 = float(percentage[1].text[:-1])
    evote = states[i].find('td',class_= 'delegates-cell').text

    e_votes[name] = (n1 + ' ' + evote)
    totals[name] = {n1:p1,n2:p2}
    winners[name] = {n1:p1}
    if 'H. Clinton' in n1:
        d_states[name] = p1
        xaxisd.append(name)
        yaxisd.append(p1)
        e_votesd[name] = int(evote)
    else:
        r_states[name] = p1
        xaxisr.append(name)
        yaxisr.append(p1)
        e_votesr[name] = int(evote)
            

  
x2= []
y2= []
for key in sorted(d_states.keys()):
    x2.append(key)
    y2.append(d_states[key])

# Democrat Percentage Victory
fig, ax = plt.subplots()
ax.bar(d_states.keys(),d_states.values(),color = 'b')
plt.title('Percentage that H. Clinton Won the State With')
plt.xlabel('States')
plt.xticks(rotation = 'vertical')
plt.ylabel('Percent')
plt.savefig('DPercentage.png')

# Republican Percentage Victory
fig, ay = plt.subplots()
ay.bar(r_states.keys(),r_states.values(),color = 'r')
plt.title('Percentage that D. Trump Won the State With')
plt.xlabel('States')
plt.ylabel('Percent')
plt.xticks(rotation = 'vertical')
plt.savefig('RPercentage.png')


for elem in e_votesd.keys():
    e_votesboth[elem] = (e_votesd[elem])
for elem in e_votesr.keys():
    e_votesboth[elem] = (e_votesr[elem])
    

#sort the keys and values
for elem in sorted(e_votesboth.keys()):
    e_votessorted[elem] = e_votesboth[elem]
    if elem in r_states.keys():
        colors.append('r')
    else:
        colors.append('b')

# Electoral Votes
fig, az = plt.subplots()
az.bar(e_votessorted.keys(),e_votessorted.values(), color = colors)
plt.title('Number of Electoral Votes per State')
plt.xlabel('States')
plt.ylabel('Votes')
plt.xticks(rotation = 'vertical')
plt.savefig('ElectionResultsVotes.png')
plt.show()

with open ('index.html','w') as f:
        
    text = ('<head>'+
            '<meta name="description" content="This will give you Curtis\'s breakdown of the 2016 Election.">'+
            '<title> Political Data </title>' +
            '<h1> Political Data</h1>' +
            
            '<p> This is my breakdown of how the voting went state by state for the 2016 election. I went through and plotted the data for each candidate\'s'
            ' performance in each state, in terms of number of the percentage with which they won, and then in addition plotted their number of electoral ' +
            ' votes from their winning states on the same graph.</p>'
            
            '<img src="DPercentage.png" alt="H. Clinton Percentage Wins">'+
            '<img src="RPercentage.png" alt="D. Trump Percentage Wins">'+
            '<img src="ElectionResultsVotes.png" alt="Electoral College Votes">' +
            '<p> I scraped all of my data off of a website that recorded voting information after the election. In this process, I went through '+
            'the HTML of the website and found what tags I needed to inspect. I started by making a list of all of the different states by using ' +
            'the beautiful soup find_all() method to find every table of class "Results-Table". I also found all of the "h3" tags which were used to ' +
            'display the state names. Then I wrote a loop that went through all of the states and found their "name-combo" span classes which had the ' +
            'name of the nominee that one. I found the corresponding percentage of vote by finding the span "number" class. Then I just had to sort which ' +
            'name went into the democrat list, and which went into the republican list. Then I went through and found how many electoral votes the '
            'candidate got from each state they won (for the states in which the electoral college can split votes, I just did the majority).' +
            '<p><a href = "https://www.politico.com/2016-election/results/map/president/">Link</a> to where I scraped the data from</p>')
            
                
    f.write(text)


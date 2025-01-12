import matplotlib.pylab as plt
from operator import itemgetter

# read csv, save lines, split lines at ; and save result array into array and return array
def readcsv():
    csv = []
    #open persons.csv
    with open('persons.csv') as file:
        #for each line in csv
        for pos, line in enumerate(file):
            #don't take first line
            if(pos > 1):
                # split line at ; and append result array in array
                csv.append(line.split(';'))
    return csv

# extract forenames ignore empty forenames, sort names and return array
def extractnames(data):
    names = []
    for line in data:
        # ignore lines with empty forename
        if(line[2] != ''):
            names.append(line[2])
    #sort is unnessecery after sorting of dict to get 10 highest
    names.sort()
    return names

def countnames(data):
    # create dict with names as key and occurance as value
    result = dict((i,data.count(i)) for i in data)
    return result

def sortdict(data):
    return dict(sorted(data.items(), key=itemgetter(1), reverse=True)[:10])

def plotdata(data):
    n, c = zip(*data.items())
    plt.bar(n, c)
    plt.show()

data = readcsv()
names = extractnames(data)
countednames = countnames(names)

sorteddict = sortdict(countednames)
plotdata(sorteddict)






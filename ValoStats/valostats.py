counter = 0

f = open('data.txt','a')
f.close()

f = open('data.txt','r')
for lines in f:
    counter = counter + 1
f.close()

if counter < 2:
    print('-- Welcome to ValoStats --')
    print('To setup, please type SETUP')
    dosetup = input('Type: ')
    if dosetup == 'SETUP':
        f = open('data.txt','w')
        f.write('- - STATS - - \n \n')
        f.close()
        
if counter < 2:
    username = input('Enter your username: ')
    f = open('data.txt','a')
    f.write('Username: '+username+'\n \n')
    f.close()
    
fornewline = 0

f = open('data.txt','r')
for lines in f:
    line = lines
    if 'Game' in line:
        fornewline += 1

games = []

for x in range(fornewline):
    games.append('to fill')

amount = int(input('How many games would you like to write stats for: '))

counter2 = 0

c = open('Count.txt','a')
c.close()

c = open('Count.txt','r')
readline1 = c.readline(1)
c.close()
c = open('data.txt', 'a')
if len(readline1) < 1:
    for x in range(amount):
        games.append('Game '+ str(len(games)))
        print('Game'+str(x + 1)+': ')
        kills = int(input('Enter kills: '))
        deaths = int(input('Enter deaths: '))
        assists = int(input('Enter assists: '))
        f = open('data.txt','a')
        f.write(games[len(games) - 1]+'\n'+'Kills: '+str(kills)+'\n'+'Deaths: '+str(deaths)+'\n'+'Assists: '+str(assists)+'\n \n')

ksecondpart = 0
dsecondpart = 0
asecondpart = 0

f = open('data.txt','r')
for lines in f:
    if 'Kills' in lines:
        kfirstpart = lines.replace('Kills:', '')
        ksecondpart = ksecondpart + int(kfirstpart)
        totalkills = ksecondpart
    if 'Deaths' in lines:
        dfirstpart = lines.replace('Deaths:','')
        dsecondpart = dsecondpart + int(dfirstpart)
        totaldeaths = dsecondpart
    if 'Assists' in lines:
        afirstpart = lines.replace('Assists:','')
        asecondpart = asecondpart + int(afirstpart)
        totalassists = asecondpart

print('Type STATS to see specific stats')

choice = input('Answer: ')

if choice == 'STATS':
    print('Choices: ')
    print('1 - K/D')
    print('2 - Total Kills')
    print('3 - Total Deaths')
    print('4 - Total Assists')
    print('5 - Total Games')
    Continue = False
    while Continue == False:
        choice2 = int(input('\n Number of Choice (Type 0 to stop): '))

        if choice2 == 1:
            print('KDR:', totalkills / totaldeaths)
        if choice2 == 2:
            print('Total Kills:', totalkills)
        if choice2 == 3:
            print('Total Deaths:', totaldeaths)
        if choice2 == 4:
            print('Total Assists:', totalassists)
        if choice2 == 5:
            print('Total Games:', fornewline + amount)
        if choice2 == 0:
            Continue = True

amountofgames = fornewline + amount
Continue = False

print('Type MORE to see specific games')

seemore = input('Answer: ')

f = open('data.txt','r')
content = f.read()
f.close()

if seemore == 'MORE':
    print('How to see a specific game: ')
    print('1 - Type in the number of the game below')
    print('2 - This program will output that game number')
    print('Game numbers start from 0 and go up to the newest game.')
    while Continue == False:
        seemore2 = int(input('Answer (Type 9999 to Stop): '))
        if seemore2 == 9999:
            Continue = True
            print('- Thank you for using ValoStats -')
        else:
            print('Note: You have', amountofgames, 'games stored. ( 0 - ',amountofgames - 1,')')
            if seemore2 > amountofgames or seemore2 < 0:
                print('You must pick a number between 0 and', amountofgames)
            else:
                f = open('data.txt','r')
                for lines in f:
                    if ('Game '+str(seemore2)) in lines:
                        print(lines, end='')
                        x = 1
                    if x == 1:
                        if ('Game '+str(seemore2 + 1)) not in lines:
                            if 'Kills' in lines or 'Assists' in lines or 'Deaths' in lines:
                                if content.index(lines) > content.index('Game '+str(seemore2)):
                                    print(lines, end='')
                        if ('Game '+str(seemore2 + 1)) in lines:
                            break
                            x = 0



                f.close()

Continue = False

while Continue == False:
    toexit = input('Enter EXIT to exit the program.')
    if toexit == 'EXIT':
        exit()
    else:
        continue

input()



                    

                    

    






        



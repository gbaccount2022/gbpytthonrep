import Lesson_4_3_module as stats

gamesCount = int(input())

teams = {}

for i in range(1,gamesCount+1):
    [team1, count1, team2, count2] = input().split(';')

    count1 = int(count1)
    count2 = int(count2)

    stats.initDefaultStats(teams, team1)
    stats.initDefaultStats(teams, team2)

    if (count1 == count2):
        stats.setPoints(teams, team1, 0, 1, 0)
        stats.setPoints(teams, team2, 0, 1, 0)
    elif (count1 > count2):
        stats.setPoints(teams, team1, 1, 0, 0)
        stats.setPoints(teams, team2, 0, 0, 1)
    else:
        stats.setPoints(teams, team1, 0, 0, 1)
        stats.setPoints(teams, team2, 1, 0, 0)

print('---- output ----')
for i in teams:
    print(i, end=': ')
    for j in teams[i]:
        print(f'{teams[i][j]}', end=' ')
    print('')
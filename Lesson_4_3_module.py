


def initDefaultStats(obj,name):
    obj.setdefault(name, {
        'totalGames': 0,
        'wins': 0,
        'draws': 0,
        'looses': 0,
        'totalPoints': 0,
    })

def setPoints(obj, name, wins, draws, looses):
    obj[name]['totalGames'] += 1
    obj[name]['wins'] += wins
    obj[name]['draws'] += draws
    obj[name]['looses'] += looses
    if wins > 0:
        obj[name]['totalPoints'] += 3
    elif draws > 0:
        obj[name]['totalPoints'] += 1


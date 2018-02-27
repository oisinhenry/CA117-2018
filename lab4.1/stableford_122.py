import sys

def points(strokes, index, par, handicap):
    strokes -= handicap // 18
    if handicap % 18 >= index:
        strokes -= 1

    return max(0, par - strokes + 2)


def main():
    pars = list(map(int, input().split()))
    indices = list(map(int, input().split()))

    names = []
    player_handicap = []
    scores = []
    for line in sys.stdin:
        split_input = line.split()

        name = split_input[:len(split_input)-19]
        names.append(' '.join(name))

        player_handicap.append(int(split_input[len(name)]))

        scores.append(split_input[len(name)+1:])

    scored_players = {}
    for player_i in range(len(names)):
        total_pts = 0
        for hole_i, strokes in enumerate(scores[player_i]):
            if strokes == 'X':
                continue

            total_pts += points(int(strokes), indices[hole_i], pars[hole_i], player_handicap[player_i])

        scored_players[names[player_i]] = total_pts

    name_field = len(max(names, key=len))
    for name, score in sorted(scored_players.items(), key=lambda x: x[1], reverse=True):
        print('{:>{}s} : {:>2}'.format(name, name_field, score))

if __name__ == '__main__':
    main()
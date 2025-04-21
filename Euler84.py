import random
from collections import defaultdict
from operator import itemgetter


def roll() -> tuple[int, bool]:
    die_1 = random.randrange(1, DICE_SIZE + 1)
    die_2 = random.randrange(1, DICE_SIZE + 1)
    count = die_1 + die_2
    is_double = die_1 == die_2
    return (count, is_double)


def positions():
    pos = 0
    doubles = 0
    while True:
        diff, is_double = roll()
        if is_double:
            doubles += 1
        else:
            doubles = 0
        if doubles == 3:
            pos = 10  # go to jail
        else:
            pos = (pos + diff) % 40
            if pos in [2, 17, 33]:
                ## community chest
                if (r := random.randrange(16)) == 0:
                    pos = 0  # advance to GO
                elif r == 1:
                    pos = 10  # go to jail
            elif pos in [7, 22, 36]:
                ## chance
                if (r := random.randrange(16)) == 0:
                    pos = 0  # advance to GO
                elif r == 1:
                    pos = 10  # go to jail
                elif r == 2:
                    pos = 11  # go to C1
                elif r == 3:
                    pos = 24  # go to E3
                elif r == 4:
                    pos = 39  # go to H2
                elif r == 5:
                    pos = 5  # go to R1
                elif r in [6, 7]:
                    ## go to next railway
                    if pos < 5 or pos >= 35:
                        pos = 5  # go to R1
                    elif 5 <= pos < 15:
                        pos = 15  # go to R2
                    elif 15 <= pos < 25:
                        pos = 25  # go to R3
                    elif 25 <= pos < 35:
                        pos = 35  # go to R4
                    else:
                        raise ValueError(f"invalid position: {pos}")
                elif r == 8:
                    ## go to next utility
                    if pos < 12 or pos >= 28:
                        pos = 12  # go to U1
                    elif 12 <= pos < 28:
                        pos = 28  # go to U2
                    else:
                        raise ValueError(f"invalid position: {pos}")
                elif r == 9:
                    pos -= 3
            elif pos in [10, 30]:
                pos = 10  # go to jail
        yield pos


if __name__ == "__main__":
    DICE_SIZE = 4
    position_counts = defaultdict(int)
    for i, p in enumerate(positions()):
        # print(p)
        position_counts[p] += 1

        if i == 0:
            continue
        if i % 1_000_000 == 0:
            print(
                "".join(
                    str(pos)
                    for pos, _ in sorted(
                        dict(position_counts).items(),
                        key=itemgetter(1),
                        reverse=True,
                    )[:3]
                )
            )
            # print(
            #     list(
            #         (pos, format(count / i, ".2%"))
            #         for pos, count in sorted(
            #             dict(position_counts).items(),
            #             key=itemgetter(1),
            #             reverse=True,
            #         )[:3]
            #     )
            # )

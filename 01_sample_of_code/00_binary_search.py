import time
from typing import List, Optional


def bs_position(src: List[int], target: int) -> Optional[int]:
    bot, top, prev_check, check = 0, len(src), 0, len(src)
    while check != prev_check:
        prev_check, check = check, bot + (top - bot) // 2
        tmp = src[check]
        print(check, '<-', bot, top)
        if tmp == target:
            return check
        bot, top = (bot, check) if target < tmp else (check, top)
    return None


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 20), 2),
        ('test_01', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 30), 3),
        ('test_02', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 40), 4),
        ('test_03', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 50), 5),
        ('test_04', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 0), 0),
        ('test_05', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 90), 9),

        ('test_06', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], -1), None),   # double_check_last_value
        ('test_07', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 111), None),  # double_check_last_value
        ('test_07', ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 64), None),   # double_check_last_value
    ]

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        print(f'\n{name}')
        rlt = bs_position(*inpt)
        print(rlt)
        assert rlt == outpt, print(f'Problem ⚠️ {name} - {rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

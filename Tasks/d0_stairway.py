from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return 0

    steps_min = [0] * len(stairway)
    steps_min[0] = stairway[0]
    steps_min[1] = stairway[1]

    for step in range(2, len(stairway)):
        steps_min[step] = min(steps_min[step - 1], steps_min[step - 2]) + stairway[step]
    return steps_min[-1]

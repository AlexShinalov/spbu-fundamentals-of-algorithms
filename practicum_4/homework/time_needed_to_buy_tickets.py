from typing import Any
from collections import deque
import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0
    n = len(tickets)
    remaining_tickets = tickets.copy()
    q = deque(range(n))


    while q:
        current_person = q.popleft()

        if current_person == k and remaining_tickets[k] == 0:
            return seconds_elapsed

        remaining_tickets[current_person] -= 1
        seconds_elapsed += 1

        if remaining_tickets[current_person] == 0:
            continue


        q.append(current_person)
    if n % 2!=0:
        seconds_elapsed-=1

    return seconds_elapsed


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("./time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")

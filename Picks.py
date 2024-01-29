import csv, sys
from typing import *
import matplotlib.pyplot as plt

# ----------------------------------------------     CLASSES     ----------------------------------------------


class Date:  # DATE FROM THE MATCH
    def __init__(self, day, month, year):
        self.day: int = day
        self.month: int = month
        self.year: int = year


class Pick:
    def __init__(self, date, time, match, stars, odds, hthg, htag, fthg, ftag, tie):
        self.date: Date = date
        self.time: str = time
        self.match = match  # List[str]
        self.stars: int = stars
        self.odds: float = odds
        self.hthg: int = hthg
        self.htag: int = htag
        self.fthg: int = fthg
        self.ftag: int = ftag
        self.tie: bool = tie


class Match:  # TEAMS THAT PLAY EACH MATCH
    def __init__(self, home, away):
        self.home = home
        self.away = away

    def __str__(self):
        return self.home + '-' + self.away


class Picks:
    def __init__(self, picks, i=0, stars=None):
        self.picks = picks  # List[Pick]
        self.stars = stars if stars is not None else i
        self.filtered_picks = self.picks_filter(self.picks, self.stars)

    def picks_filter(self, picks, stars: Optional[int]):
        if stars is None:
            return picks
        filtered_picks = []
        for p in picks:
            if p.stars >= stars:
                filtered_picks.append(p)
        return filtered_picks

# ----------------------------------------------     STAKING PLANS     ----------------------------------------------

# From the list of picks returns the final balance and
# every gain/loss from each match
# FORMAT: variable bank is initialized with 1 betting unit
#         variable profits is a dictionary with objects Match as key and profits from that match (can be negative)

    def flat(self):
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = m.odds - 1
            else:
                profits[partido] = -1
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def martingale(self):
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        unit = 1
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                unit *= 1.5
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]

        return bank, profits, profits_mensual

    # ----------------- Generic fibo with retro 2
    def fibonacci(self):  # If winning then bet times the element in two positions behind on the
                                                 # Fibonacci sequence (unless you are at 1 or 2 betting units, if lose bet
                                                 # timee the element in the next position of the Fibonacci sequence
        def fib_mem(n: int):
            def _f(n: int):
                if n == 0: return 1.0001
                if n == 1: return 1
                if n not in mem:
                    mem[n] = _f(n-2) + _f(n-1)
                return mem[n]
            mem = {}
            return _f(n)

        term = 1

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        sequence_index = [1]
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                if unit == 1 or unit == 2:
                    unit = 1
                else:
                    unit = sequence_index[sequence_index.index(unit) - 2]
            else:
                profits[partido] = -unit
                if sequence_index.index(unit) == len(sequence_index) - 1:
                    term += 1
                    sequence_index.append(fib_mem(term))
                unit = sequence_index[sequence_index.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    # -------------------------------- FIBOS RETRO 2 --------------------------------
    # --------- NO STOP -------------------
    def fibo5retro2nostop(self):
        sequence = [1, 1.0001, 2, 3, 5]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                if unit == 1 or unit == 2:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) - 2]
            else:
                profits[partido] = -unit
                if sequence.index(unit) == 4:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo6retro2nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                if unit == 1 or unit == 2:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) - 2]
            else:
                profits[partido] = -unit
                if sequence.index(unit) == 5:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo7retro2nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                if unit == 1 or unit == 2:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) - 2]
            else:
                profits[partido] = -unit
                if sequence.index(unit) == 6:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo8retro2nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13, 21]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                if unit == 1 or unit == 2:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) - 2]
            else:
                profits[partido] = -unit
                if sequence.index(unit) == 7:
                    unit = 1
                else:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual
    # ------------ STOP ---------------

    def fibo5retro2stop(self):
        sequence = [1, 1.0001, 2, 3, 5]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    if unit == 1 or unit == 2:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) - 2]
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) == 4:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6retro2stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    if unit == 1 or unit == 2:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) - 2]
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) == 5:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo7retro2stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    if unit == 1 or unit == 2:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) - 2]
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) == 6:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo8retro2stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13, 21]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    if unit == 1 or unit == 2:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) - 2]
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) == 7:
                        unit = 1
                    else:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    # -------------------------------- FIBOS --------------------------------
    # --------- NO STOP -------------------
    def fibo5nostop(self):
        sequence = [1, 1.0001, 2, 3, 5]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != 3:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo6nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if sequence.index(unit) != 5:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo7nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if sequence.index(unit) != 6:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def fibo8nostop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13, 21]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if sequence.index(unit) != 7:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    # ------------ STOP ---------------

    def fibo5stop(self):
        sequence = [1, 1.0001, 2, 3, 5]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 4:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 5:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus6(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001, 5.000001, 3.0000001, 2.0000001, 1.000001, 1.0000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 11:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus5(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001, 5.000001, 3.0000001, 2.0000001, 1.000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 10:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus4(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001, 5.000001, 3.0000001, 2.0000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 9:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus3(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001, 5.000001, 3.0000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 8:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus2(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001, 5.000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 7:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6plus1(self):
        sequence = [1, 1.00001, 2, 3, 5, 8, 8.000001]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 6:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo6stopPlus1(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 10, 15]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        fase_2 = False
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop or fase_2:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) < 5:
                        unit = sequence[sequence.index(unit) + 1]
                    if unit == 15:
                        fase_2 = False
                    if unit == 10:
                        unit = 15
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[5]:
                stop = True
                unit = 10
                fase_2 = True
            first_match = False
            if stop and m.tie:
                stop = False
                fase_2 = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo7stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 6:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo8stop(self):
        sequence = [1, 1.0001, 2, 3, 5, 8, 13, 21]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 7:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def fibo3day(self):
        sequence = [1, 1.0001, 2]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 7:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual


    # ------------------- Pronotest6 ---------------------

    def pronotest6nostop(self):
        sequence = [1, 3, 5, 6, 7, 8]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != sequence[len(sequence) - 1]:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    def pronotest6stop(self):
        sequence = [1, 3, 5, 6, 7, 8]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if unit != sequence[len(sequence) - 1]:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def pronotest6Plus1stop(self):
        sequence = [1, 3, 4, 5, 6, 7, 8, 10]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        fase_2 = False
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop or fase_2:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) < 6:
                        unit = sequence[sequence.index(unit) + 1]
                    if unit == 10:
                        fase_2 = False
                    if unit == 8:
                        unit = 10
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[6]:
                stop = True
                unit = 10
                fase_2 = True
            first_match = False
            if stop and m.tie:
                stop = False
                fase_2 = False
                unit = 1
        return bank, profits, profits_mensual

    # ----------------- Increment -----------------
    # -------- No stop --------
    def inc5nostop(self):
        sequence = [1, 2, 3, 4, 5]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != sequence[len(sequence) - 1]:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]

        return bank, profits, profits_mensual

    def inc6nostop(self):
        sequence = [1, 2, 3, 4, 5, 6]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != sequence[len(sequence) - 1]:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]

        return bank, profits, profits_mensual

    def inc7nostop(self):
        sequence = [1, 2, 3, 4, 5, 6, 7]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != sequence[len(sequence) - 1]:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]

        return bank, profits, profits_mensual

    def inc8nostop(self):
        sequence = [1, 2, 3, 4, 5]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        profits_mensual = [0] * 12
        for m in matches:
            partido = Match(m.match[0], m.match[1])
            if m.tie:
                profits[partido] = unit * m.odds - unit
                unit = 1
            else:
                profits[partido] = -unit
                if unit != sequence[len(sequence) - 1]:
                    unit = sequence[sequence.index(unit) + 1]
            bank += profits[partido]
            profits_mensual[m.date.month - 1] += profits[partido]
        return bank, profits, profits_mensual

    # -------- Stop --------
    def inc5stop(self):
        sequence = [1, 2, 3, 4, 5]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if unit != sequence[len(sequence) - 1]:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def inc6stop(self):
        sequence = [1, 2, 3, 4, 5, 6]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if unit != sequence[len(sequence) - 1]:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def inc7stop(self):
        sequence = [1, 2, 3, 4, 5, 6, 7]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if unit != sequence[len(sequence) - 1]:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

    def inc8stop(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8]

        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if unit != sequence[len(sequence) - 1]:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits, profits_mensual

#-------------------------------     NEW STAKING PLAN       ----------------------------

    def newsp(self):
        sequence = [1, 1.0001, 2, 3, 5, 8]
        unit = 1
        bank = 1000
        matches = picks.filtered_picks
        profits = {}
        stop = False
        first_match = True
        profits_mensual = [0] * 12
        for m in matches:
            if first_match or not stop:
                partido = Match(m.match[0], m.match[1])
                if m.tie:
                    stop = False
                    profits[partido] = unit * m.odds - unit
                    unit = 1
                else:
                    profits[partido] = -unit
                    if sequence.index(unit) != 5:
                        unit = sequence[sequence.index(unit) + 1]
                bank += profits[partido]
                profits_mensual[m.date.month - 1] += profits[partido]
            if not m.tie and unit == sequence[len(sequence) - 1]:
                stop = True
            first_match = False
            if stop and m.tie:
                stop = False
                unit = 1
        return bank, profits
# ----------------------------------     EXECUTE STAKING PLAN     ----------------------------------

    def apply_sp(self, sp):
        if sp == "flat":
            return self.flat()
        if sp == "fibonacci":
            return self.fibonacci()
        if sp == "martingale":
            return self.martingale()
        if sp == "fibo5stop":
            return self.fibo5stop()
        if sp == "fibo6stop":
            return self.fibo6stop()
        if sp == "fibo6stopPlus1":
            return self.fibo6stopPlus1()
        if sp == "fibo7stop":
            return self.fibo7stop()
        if sp == "fibo8stop":
            return self.fibo8stop()
        if sp == "fibo5nostop":
            return self.fibo5nostop()
        if sp == "fibo6nostop":
            return self.fibo6nostop()
        if sp == "fibo7nostop":
            return self.fibo7nostop()
        if sp == "fibo8nostop":
            return self.fibo8nostop()
        if sp == "fibo5retro2stop":
            return self.fibo5retro2stop()
        if sp == "fibo6retro2stop":
            return self.fibo6retro2stop()
        if sp == "fibo7retro2stop":
            return self.fibo7retro2stop()
        if sp == "fibo8retro2stop":
            return self.fibo8retro2stop()
        if sp == "fibo5retro2nostop":
            return self.fibo5retro2nostop()
        if sp == "fibo6retro2nostop":
            return self.fibo6retro2nostop()
        if sp == "fibo7retro2nostop":
            return self.fibo7retro2nostop()
        if sp == "fibo8retro2nostop":
            return self.fibo8retro2nostop()
        if sp == "pronotest6stop":
            return self.pronotest6stop()
        if sp == "pronotest6nostop":
            return self.pronotest6nostop()
        if sp == "inc5stop":
            return self.inc5stop()
        if sp == "inc6stop":
            return self.inc6stop()
        if sp == "inc7stop":
            return self.inc7stop()
        if sp == "inc8stop":
            return self.inc8stop()
        if sp == "inc5nostop":
            return self.inc5nostop()
        if sp == "inc6nostop":
            return self.inc6nostop()
        if sp == "inc7nostop":
            return self.inc7nostop()
        if sp == "inc8nostop":
            return self.inc8nostop()
        if sp == "fibo6plus6":
            return self.fibo6plus6()
        if sp == "fibo6plus5":
            return self.fibo6plus5()
        if sp == "fibo6plus4":
            return self.fibo6plus4()
        if sp == "fibo6plus3":
            return self.fibo6plus3()
        if sp == "fibo6plus2":
            return self.fibo6plus2()
        if sp == "fibo6plus1":
            return self.fibo6plus1()
        if sp == "pronotest6Plus1stop":
            return self.pronotest6Plus1stop()
        if sp == "fibo3day":
            return self.fibo3day()
        if sp == "newsp":
            return self.newsp()

# ----------------------------------     METHODS TO REPRESENTENT THE RESULTS     ----------------------------------

    def show_results(self, method, profits, profits_mensuales):
        def gains(profits):
            balance = [1000]
            gains = 1000
            for value in profits.values():
                gains += value
                balance.append(gains)
            max_profit = max(balance) - 1000
            min_profit = min(balance) - 1000
            bank = balance[-1]
            profit = bank - 1000
            return balance, bank, profit, max_profit, min_profit

        def plot(method, balance):  # Plots the results, x axis = matches; y axis = balance
            plt.plot(balance)
            plt.title(method.upper())
            plt.ylabel("BALANCE")
            plt.xlabel("MATCHES")
            plt.scatter(len(balance), balance[-1], color='y')
            plt.annotate(round(balance[-1] - 1000, 2), (len(balance), balance[-1]))
            plt.show()
        balance, bank, profit, max_profit, min_profit = gains(profits)
        plot(method, balance)
        print("Final balance: {0:.2f}" .format(bank))
        print("Profit: {0:.2f} " .format(profit))
        print("Max profit: {0:.2f}" .format(max_profit))
        print("Min profit: {0:.2f}" .format(min_profit))
        mensuales_rounded = []
        for p in profits_mensuales:
            pr = round(p, 2)
            mensuales_rounded.append(pr)
        print("Monthly profits: {0}" .format(mensuales_rounded))
# -------------------------------------------     READ DATA        -------------------------------------------


def loadCSV(f) -> List[Pick]:
    csvreader = csv.reader(f)
    header = [next(csvreader)]
    rows = []
    for row in csvreader:
        rows.append(row)
    partidos = []
    for f in rows:  # From the read file all the Pick objects are created
        fecha = f[0].strip().split('/')
        #fecha = f[0].strip().split('-')
        year = int(fecha[2])
        month = int(fecha[1])
        day = int(fecha[0])
        date = Date(day, month, year)
        time = f[1]
        match = f[2].strip('\n ').split('-')
        if f[3] == '':
            stars = 0
        else:
            stars = int(f[3])
        odds = float(f[4])
        if odds < 2.80:
            odds = 2.80
        hth = int(f[5])
        hta = int(f[6])
        fth = int(f[7])
        fta = int(f[8])
        tie = False
        if fth == fta:
            tie = True
        pick = Pick(date, time, match, stars, odds, hth, hta, fth, fta, tie)
        if (pick.stars != 1 and pick.date.month < 11) or pick.date.month > 10:
            partidos.append(pick)
    return partidos

# -------------------------------------------     MAIN PROGRAM     -------------------------------------------


if __name__ == '__main__':
    nombreFichero = input()
    f = open(nombreFichero, 'r', encoding='utf-8')
    # rows = loadCSV(sys.stdin)
    rows = loadCSV(f)
    picks = Picks(rows, int(input()))
    method = input()
    bank, profits, mensuales = picks.apply_sp(method)
    picks.show_results(method, profits, mensuales)
import time
from algorithms.two_approx import TwoApprox
from algorithms.dynamic_programming_by_weights import DynamicProgrammingByWeights
from algorithms.dynamic_programming_by_profits import DynamicProgrammingByProfits
from algorithms.branches_and_boundaries import BranchesAndBoundaries
from algorithms.fptas import FPTAS


def benchmark():
    time_table = []
    counter_table = []
    solution_table = []
    weight_table = []
    profit_table = []

    for i in range(1, 9):
        capacity = 0
        with open(f'benchmarks/p0{i}_c.txt') as f:
            for j in f:
                capacity = int(j)
        profits = []
        with open(f'benchmarks/p0{i}_p.txt') as f:
            for j in f:
                profits.append(int(j))
        solve = []
        with open(f'benchmarks/p0{i}_s.txt') as f:
            for j in f:
                solve.append(int(j))
        weights = []
        with open(f'benchmarks/p0{i}_w.txt') as f:
            for j in f:
                weights.append(int(j))
        classes = [TwoApprox, DynamicProgrammingByWeights,
                   DynamicProgrammingByProfits, BranchesAndBoundaries, FPTAS]
        time_current = []
        counter_current = []
        solution_current = []
        weight_current = []
        profit_current = []
        for algo in classes:
            if i!=8 or (i==8 and algo==TwoApprox or algo==BranchesAndBoundaries):
                instance = algo(weights, profits, capacity)
                opt_x, opt_profit, opt_weight = None, None, None
                start_time = time.time()
                opt_x, opt_profit, opt_weight = instance.calculate()
                time_current.append(time.time() - start_time)
                counter_current.append(instance.solution_counter)
                solution_current.append(opt_x)
                weight_current.append(opt_weight)
                profit_current.append(opt_profit)
            else:
                time_current.append('-')
                counter_current.append('-')
                solution_current.append('-')
                weight_current.append('-')
                profit_current.append('-')
        time_table.append(time_current)
        counter_table.append(counter_current)
        solution_table.append(solution_current)
        weight_table.append(weight_current)
        profit_table.append(profit_current)
    return time_table, counter_table, solution_table, weight_table, profit_table


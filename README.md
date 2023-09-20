# water_jug_problem
Problem Statement:
You are given two water jugs with different capacities, Jug A and Jug B. Jug A can hold "X" liters of water, and Jug B can hold "Y" liters of water, where X and Y are positive integers. Your goal is to measure a specific quantity of water, "Z" liters, using these two jugs. You can perform the following operations:

Fill a Jug: You can fill either Jug A or Jug B with water from an infinite water source until the jug is full. For example, you can fill Jug A with X liters or Jug B with Y liters.

Empty a Jug: You can completely empty either Jug A or Jug B to get rid of its contents. For example, you can empty Jug A if it contains water.

Pour Water: You can pour water from one jug into the other until the receiving jug is full, or the pouring jug is empty. This operation allows you to transfer water between the two jugs. For example, you can pour water from Jug A into Jug B, or vice versa, until one of them is full or empty.

Objective:
Your objective is to determine if it's possible to measure exactly "Z" liters of water using these jugs. If it's possible, you should also figure out the steps to achieve this measurement.

Approach:
To solve this problem, you can start with both jugs empty and iteratively perform the operations mentioned above. Keep track of the state of the jugs (the amount of water in each jug) at each step. Continue these operations until you either measure "Z" liters of water or determine that it's not possible to reach that amount.

Example:
Let's consider a simple example to illustrate the problem. Suppose Jug A has a capacity of 3 liters, Jug B has a capacity of 5 liters, and you want to measure 4 liters of water. You can follow a sequence of operations like filling Jug B, pouring Jug B into Jug A, emptying Jug A, pouring Jug B into Jug A again, and finally, filling Jug B again. This sequence of operations will allow you to measure exactly 4 liters of water.

Note: While this description doesn't explicitly mention algorithms like BFS or DFS, the approach used for solving the problem is similar to a systematic exploration of all possible states of the jugs until a solution is found or determined to be impossible.






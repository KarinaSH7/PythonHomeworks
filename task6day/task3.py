"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""

object = max(set(newspaper).union(set(magazine))) - min(set(newspaper).union(set(magazine)))+1
print(object - (max(both) - min(both) + 1))

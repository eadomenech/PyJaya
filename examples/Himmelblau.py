# -*- coding: utf-8 -*-
"""Himmelblau funtion with constraints
http://benchmarkfcns.xyz/benchmarkfcns/himmelblaufcn.html
"""

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdadtive import JayaSelfAdadtive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampemultiprocess import JayaSAMPE
from pyJaya.variables import VariableFloat


def himmelblau(solution):
    return (
        solution[0] ** 2 + solution[1] - 11) ** 2 +\
            (solution[0] + solution[1] ** 2 - 7) ** 2


def himmelblauConstraintOne(solution):
    return (26 - (solution[0] - 5) ** 2 - solution[1] ** 2) >= 0


def himmelblauConstraintTwo(solution):
    return (20 - 4 * solution[0] - solution[1]) >= 0


def main():
    print("RUN: JayaClasic")
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    ja = JayaClasic(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    ja = JayaSelfAdadtive(
        listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    ja = JayaQuasiOppositional(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    ja = JayaSAMP(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    ja = JayaSAMPE(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()

def calculateSalary(baseSalary, bonusRate=.1):
    return baseSalary * (1+bonusRate)

def calculateBonus(totalSalary, baseSalary):
    return (totalSalary - baseSalary)/baseSalary
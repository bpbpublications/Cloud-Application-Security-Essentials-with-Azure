#
# economic models
#
class AttackCost:
    # assume the attack costs this amount
    cost = 5
    def GetAttackCost():
        return AttackCost.cost
    

#
# value protected
value = 10
# protection cost
protcost= 2
# attack cost
attackcost = AttackCost.GetAttackCost()
# print the value and attack cost
print(f"protecting an asset with a value of {value} using protection costing {protcost} against an attack valued at {attackcost}")
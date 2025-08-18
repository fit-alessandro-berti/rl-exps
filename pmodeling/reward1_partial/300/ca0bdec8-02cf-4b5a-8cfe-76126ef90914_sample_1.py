import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Blocks = Transition(label='Pressing Blocks')
Salting_Process = Transition(label='Salting Process')
Aging_Monitoring = Transition(label='Aging Monitoring')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Compliance_Check = Transition(label='Compliance Check')
Market_Research = Transition(label='Market Research')
Direct_Shipping = Transition(label='Direct Shipping')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Adjust = Transition(label='Recipe Adjust')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Testing, Culture_Prep, Milk_Pasteurize])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Cutting, Whey_Draining, Molding_Cheese])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Pressing_Blocks, Salting_Process])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Monitoring, Flavor_Profiling])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Design, Compliance_Check])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Market_Research, Direct_Shipping])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Recipe_Adjust])

root = StrictPartialOrder(nodes=[Milk_Sourcing, loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(Milk_Sourcing, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)

print(root)
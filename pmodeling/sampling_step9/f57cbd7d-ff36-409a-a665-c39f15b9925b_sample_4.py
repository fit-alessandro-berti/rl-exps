import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
Trend_Scan = Transition(label='Trend Scan')
Idea_Sprint = Transition(label='Idea Sprint')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Review = Transition(label='Risk Review')
Tech_Prototype = Transition(label='Tech Prototype')
Market_Simulate = Transition(label='Market Simulate')
Stakeholder_Align = Transition(label='Stakeholder Align')
Budget_Adjust = Transition(label='Budget Adjust')
Talent_Source = Transition(label='Talent Source')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Refine = Transition(label='Data Refine')
Scale_Analysis = Transition(label='Scale Analysis')
Integration_Plan = Transition(label='Integration Plan')
Change_Manage = Transition(label='Change Manage')
Knowledge_Transfer = Transition(label='Knowledge Transfer')

# Define silent transitions (e.g., for parallel execution)
skip = SilentTransition()

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Tech_Prototype, Market_Simulate, Stakeholder_Align])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Data_Refine])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Scale_Analysis, Integration_Plan])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Budget_Adjust, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Talent_Source, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Change_Manage, Knowledge_Transfer])

# Construct the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)

# Print the root of the POWL model
print(root)
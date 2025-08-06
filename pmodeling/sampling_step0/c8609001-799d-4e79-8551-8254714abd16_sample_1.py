import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Test = Transition(label='Material Test')
Expert_Consult = Transition(label='Expert Consult')
Database_Search = Transition(label='Database Search')
Condition_Report = Transition(label='Condition Report')
Risk_Assess = Transition(label='Risk Assess')
Market_Analysis = Transition(label='Market Analysis')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Legal_Review = Transition(label='Legal Review')
Insurance_Quote = Transition(label='Insurance Quote')
Price_Negotiation = Transition(label='Price Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Final_Approval = Transition(label='Final Approval')
Asset_Registration = Transition(label='Asset Registration')

# Define silent activities
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check, Material_Test, Expert_Consult, Risk_Assess, Market_Analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Meet, Legal_Review, Insurance_Quote, Price_Negotiation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Contract_Draft, Final_Approval])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Database_Search, Condition_Report])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor2, loop2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor3, loop3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Asset_Registration, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor5])
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the POWL model
print(root)
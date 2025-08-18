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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Material_Test, Condition_Report])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Assess, Market_Analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Meet, Legal_Review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Insurance_Quote, Price_Negotiation])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Contract_Draft, Final_Approval])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Database_Search, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Asset_Registration, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[Initial_Review, Provenance_Check, loop1, xor1, loop2, xor2, loop3, loop4, loop5])
root.order.add_edge(Initial_Review, Provenance_Check)
root.order.add_edge(Provenance_Check, loop1)
root.order.add_edge(Provenance_Check, xor1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(xor1, loop3)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, Asset_Registration)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
opportunity_scan = Transition(label='Opportunity Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_merge = Transition(label='Concept Merge')
resource_align = Transition(label='Resource Align')
prototype_build = Transition(label='Prototype Build')
feasibility_test = Transition(label='Feasibility Test')
pilot_launch = Transition(label='Pilot Launch')
feedback_gather = Transition(label='Feedback Gather')
design_adapt = Transition(label='Design Adapt')
compliance_check = Transition(label='Compliance Check')
scaling_plan = Transition(label='Scaling Plan')
ip_management = Transition(label='IP Management')
market_sync = Transition(label='Market Sync')
partner_review = Transition(label='Partner Review')
exit_strategy = Transition(label='Exit Strategy')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[resource_align, exit_strategy])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, exit_strategy])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[feasibility_test, exit_strategy])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, exit_strategy])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_gather, exit_strategy])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[design_adapt, exit_strategy])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, exit_strategy])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[scaling_plan, exit_strategy])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ip_management, exit_strategy])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[market_sync, exit_strategy])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[partner_review, exit_strategy])

# Create the StrictPartialOrder model
root = StrictPartialOrder(nodes=[opportunity_scan, idea_workshop, concept_merge, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11])
root.order.add_edge(opportunity_scan, idea_workshop)
root.order.add_edge(idea_workshop, concept_merge)
root.order.add_edge(concept_merge, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)

print(root)
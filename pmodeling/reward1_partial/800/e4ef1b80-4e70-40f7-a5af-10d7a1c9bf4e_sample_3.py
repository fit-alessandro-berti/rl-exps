import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, resource_align])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[concept_merge, prototype_build])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[feasibility_test, pilot_launch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[feedback_gather, design_adapt])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, scaling_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[ip_management, market_sync])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[partner_review, exit_strategy])

# Define the partial order
root = StrictPartialOrder(nodes=[opportunity_scan, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(opportunity_scan, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
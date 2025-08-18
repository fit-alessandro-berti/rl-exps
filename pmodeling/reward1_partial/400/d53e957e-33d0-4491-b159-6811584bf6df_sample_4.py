import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
data_capture = Transition(label='Data Capture')
trend_scan = Transition(label='Trend Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_draft = Transition(label='Concept Draft')
expert_review = Transition(label='Expert Review')
prototype_build = Transition(label='Prototype Build')
regulation_check = Transition(label='Regulation Check')
ip_alignment = Transition(label='IP Alignment')
supply_sync = Transition(label='Supply Sync')
market_mapping = Transition(label='Market Mapping')
pilot_launch = Transition(label='Pilot Launch')
feedback_loop = Transition(label='Feedback Loop')
design_iterate = Transition(label='Design Iterate')
impact_measure = Transition(label='Impact Measure')
strategy_adapt = Transition(label='Strategy Adapt')

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, ip_alignment])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, market_mapping])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, feedback_loop])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[impact_measure, strategy_adapt])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, trend_scan, idea_workshop, concept_draft, expert_review, prototype_build, xor1, xor2, xor3, xor4])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor5])
root.order.add_edge(xor5, xor1)
root.order.add_edge(xor5, xor2)
root.order.add_edge(xor5, xor3)
root.order.add_edge(xor5, xor4)
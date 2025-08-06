import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Client Consult', 'Spec Finalize', 'Design Draft', 'Aerodynamics Test', 'AI Integration', 'Material Sourcing', 'Component Order', 'Assembly Line', 'Firmware Install', 'Environmental Test', 'Quality Check', 'Brand Packaging', 'Shipping Prep', 'Delivery Schedule', 'Post-Sale Support']

# Define the transitions
transitions = [Transition(label=activity) for activity in activities]

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=transitions)

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=transitions[11:])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
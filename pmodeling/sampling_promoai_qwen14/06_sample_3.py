import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
online_order = Transition(label='Customer places order online')
phone_order = Transition(label='Customer places order over the phone')
confirmation = Transition(label='Generate and send order confirmation')
label_generation = Transition(label='Generate shipping label')
handover = Transition(label='Hand over order to logistics provider')
monitor = Transition(label='Monitor shipment')
pick_pack = Transition(label='Pick and pack items')
feedback_returns = Transition(label='Process customer feedback or returns')
tracking = Transition(label='Send tracking information to customer')
delivery = Transition(label='Successful delivery')

# Define silent transitions for optional activities
silent_feedback_returns = SilentTransition()

# Define XOR choice for online or phone order
order_type = OperatorPOWL(operator=Operator.XOR, children=[online_order, phone_order])

# Define the main sequence of activities
sequence = OperatorPOWL(operator=Operator.SEQUENCE, children=[order_type, confirmation, pick_pack, label_generation, handover, monitor, tracking, delivery])

# Define the optional feedback/returns path
feedback_returns_path = OperatorPOWL(operator=Operator.SEQUENCE, children=[silent_feedback_returns, feedback_returns])

# Create the final POWL model
root = StrictPartialOrder(nodes=[sequence, feedback_returns_path])
root.order.add_edge(sequence, feedback_returns_path)
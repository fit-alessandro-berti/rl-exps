import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
scan = Transition(label='Scan Markets')
host = Transition(label='Host Workshops')
form = Transition(label='Form Teams')
dev = Transition(label='Develop Prototypes')
test = Transition(label='Simulate Tests')
feedback = Transition(label='Collect Feedback')
review = Transition(label='Review Ethics')
analysis = Transition(label='Conduct Analysis')
identify = Transition(label='Identify Partners')
align = Transition(label='Align Strategy')
launch = Transition(label='Launch Pilots')
monitor = Transition(label='Monitor Trends')
ai = Transition(label='AI Analytics')
pivot = Transition(label='Pivot Plans')
cycle = Transition(label='Cycle Renewal')

# Loop for the iterative process: do -> optionally do
loop_body = StrictPartialOrder(nodes=[dev, test, feedback, review, analysis, identify, align, launch, monitor, ai, pivot])
loop_body.order.add_edge(dev, test)
loop_body.order.add_edge(test, feedback)
loop_body.order.add_edge(feedback, review)
loop_body.order.add_edge(review, analysis)
loop_body.order.add_edge(analysis, identify)
loop_body.order.add_edge(identify, align)
loop_body.order.add_edge(align, launch)
loop_body.order.add_edge(launch, monitor)
loop_body.order.add_edge(monitor, ai)
loop_body.order.add_edge(ai, pivot)

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[scan, host, form, loop_body, skip])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[loop, cycle])
root.order.add_edge(loop, cycle)

# Print the root model (optional)
print(root)
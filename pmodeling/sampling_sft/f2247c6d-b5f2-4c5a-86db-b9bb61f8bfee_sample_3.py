import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
receive = Transition(label='Receive Returns')
inspect = Transition(label='Inspect Items')
segregate = Transition(label='Segregate Stock')
wipe = Transition(label='Wipe Data')
harvest = Transition(label='Harvest Parts')
refurbish = Transition(label='Refurbish Units')
test = Transition(label='Test Quality')
recycle = Transition(label='Recycle Waste')
dispose = Transition(label='Dispose Defects')
update = Transition(label='Update Inventory')
coordinate = Transition(label='Coordinate Resale')
process_refunds = Transition(label='Process Refunds')
analyze = Transition(label='Analyze Patterns')
improve = Transition(label='Improve Design')
report = Transition(label='Report Metrics')

# Silent transition for loop continuation
skip = SilentTransition()

# Choice for either recycling or disposing
recycle_or_dispose = OperatorPOWL(operator=Operator.XOR, children=[recycle, dispose])

# Loop: after quality testing, either continue to analysis or perform the choice and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[test, recycle_or_dispose])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    receive, inspect, segregate, wipe, harvest, refurbish, loop,
    update, coordinate, process_refunds, analyze, improve, report
])

# Define the control-flow dependencies
root.order.add_edge(receive, inspect)
root.order.add_edge(inspect, segregate)
root.order.add_edge(segregate, wipe)
root.order.add_edge(wipe, harvest)
root.order.add_edge(harvest, refurbish)
root.order.add_edge(refurbish, loop)
root.order.add_edge(loop, update)
root.order.add_edge(update, coordinate)
root.order.add_edge(coordinate, process_refunds)
root.order.add_edge(process_refunds, analyze)
root.order.add_edge(analyze, improve)
root.order.add_edge(improve, report)
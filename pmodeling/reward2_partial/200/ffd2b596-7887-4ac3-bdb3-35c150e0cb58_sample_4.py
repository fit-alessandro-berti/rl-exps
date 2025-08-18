import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
sourcing = Transition(label='Component Sourcing')
calibration = Transition(label='Sensor Calibrate')
assembly = Transition(label='Motor Assembly')
frame = Transition(label='Frame Build')
software = Transition(label='Software Install')
tuning = Transition(label='Algorithm Tune')
battery = Transition(label='Battery Integrate')
signal = Transition(label='Signal Test')
durability = Transition(label='Durability Check')
simulate = Transition(label='Flight Simulate')
inspect = Transition(label='Quality Inspect')
review = Transition(label='Compliance Review')
package = Transition(label='Packaging Prep')
logistics = Transition(label='Logistics Plan')
feedback = Transition(label='Client Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[
    sourcing, calibration, assembly, frame, software, tuning, battery, signal, durability, simulate, inspect, review, package, logistics, feedback
])

# Define the dependencies
root.order.add_edge(sourcing, calibration)
root.order.add_edge(calibration, assembly)
root.order.add_edge(assembly, frame)
root.order.add_edge(frame, software)
root.order.add_edge(software, tuning)
root.order.add_edge(tuning, battery)
root.order.add_edge(battery, signal)
root.order.add_edge(signal, durability)
root.order.add_edge(durability, simulate)
root.order.add_edge(simulate, inspect)
root.order.add_edge(inspect, review)
root.order.add_edge(review, package)
root.order.add_edge(package, logistics)
root.order.add_edge(logistics, feedback)

# Print the result
print(root)
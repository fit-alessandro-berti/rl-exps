import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
component_sourcing = Transition(label='Component Sourcing')
sensor_calibrate = Transition(label='Sensor Calibrate')
motor_assembly = Transition(label='Motor Assembly')
frame_build = Transition(label='Frame Build')
software_install = Transition(label='Software Install')
algorithm_tune = Transition(label='Algorithm Tune')
battery_integrate = Transition(label='Battery Integrate')
signal_test = Transition(label='Signal Test')
durability_check = Transition(label='Durability Check')
flight_simulate = Transition(label='Flight Simulate')
quality_inspect = Transition(label='Quality Inspect')
compliance_review = Transition(label='Compliance Review')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

# Create a StrictPartialOrder model with defined activities
root = StrictPartialOrder(nodes=[
    component_sourcing,
    sensor_calibrate,
    motor_assembly,
    frame_build,
    software_install,
    algorithm_tune,
    battery_integrate,
    signal_test,
    durability_check,
    flight_simulate,
    quality_inspect,
    compliance_review,
    packaging_prep,
    logistics_plan,
    client_feedback
])

# Since there are no dependencies mentioned in the problem description, we don't need to add any edges.
# However, if there were dependencies, we could add them like this:
# root.order.add_edge(component_sourcing, sensor_calibrate)
# root.order.add_edge(component_sourcing, motor_assembly)
# root.order.add_edge(component_sourcing, frame_build)
# root.order.add_edge(component_sourcing, software_install)
# root.order.add_edge(component_sourcing, algorithm_tune)
# root.order.add_edge(component_sourcing, battery_integrate)
# root.order.add_edge(component_sourcing, signal_test)
# root.order.add_edge(component_sourcing, durability_check)
# root.order.add_edge(component_sourcing, flight_simulate)
# root.order.add_edge(component_sourcing, quality_inspect)
# root.order.add_edge(component_sourcing, compliance_review)
# root.order.add_edge(component_sourcing, packaging_prep)
# root.order.add_edge(component_sourcing, logistics_plan)
# root.order.add_edge(component_sourcing, client_feedback)

# The final result is stored in the variable 'root'
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

# Define the partial order structure
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

# Define dependencies between nodes
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, motor_assembly)
root.order.add_edge(motor_assembly, frame_build)
root.order.add_edge(frame_build, software_install)
root.order.add_edge(software_install, algorithm_tune)
root.order.add_edge(algorithm_tune, battery_integrate)
root.order.add_edge(battery_integrate, signal_test)
root.order.add_edge(signal_test, durability_check)
root.order.add_edge(durability_check, flight_simulate)
root.order.add_edge(flight_simulate, quality_inspect)
root.order.add_edge(quality_inspect, compliance_review)
root.order.add_edge(compliance_review, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_feedback)

# Now 'root' contains the POWL model for the described process.
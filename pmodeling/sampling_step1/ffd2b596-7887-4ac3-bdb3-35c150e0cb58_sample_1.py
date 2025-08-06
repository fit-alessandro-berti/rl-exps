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

# Define a loop for software installation and algorithm tuning
software_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[software_install, algorithm_tune])

# Define a choice for the battery integration and signal testing
battery_integrate_choice = OperatorPOWL(operator=Operator.XOR, children=[battery_integrate, signal_test])

# Define a choice for the flight simulation and quality inspection
flight_simulate_choice = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, quality_inspect])

# Define a loop for the compliance review and logistics plan
compliance_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_review, logistics_plan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[component_sourcing, sensor_calibrate, motor_assembly, frame_build, software_install_loop, battery_integrate_choice, flight_simulate_choice, quality_inspect, compliance_review_loop, packaging_prep, logistics_plan, client_feedback])

# Add edges to the root POWL model
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, motor_assembly)
root.order.add_edge(motor_assembly, frame_build)
root.order.add_edge(frame_build, software_install_loop)
root.order.add_edge(software_install_loop, battery_integrate_choice)
root.order.add_edge(battery_integrate_choice, flight_simulate_choice)
root.order.add_edge(flight_simulate_choice, quality_inspect)
root.order.add_edge(quality_inspect, compliance_review_loop)
root.order.add_edge(compliance_review_loop, logistics_plan)
root.order.add_edge(logistics_plan, packaging_prep)
root.order.add_edge(packaging_prep, client_feedback)

# Print the root POWL model
print(root)
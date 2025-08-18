import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the transitions as silent transitions (for simplicity, no actual operations are performed)
skip = SilentTransition()

# Define the POWL model
loop_sensor_calibration = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, battery_integrate])
loop_flight_simulation = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate, quality_inspect])
xor_sensor_and_battery = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibrate, battery_integrate])
xor_quality_and_flight = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, flight_simulate])

root = StrictPartialOrder(nodes=[component_sourcing, motor_assembly, frame_build, software_install, algorithm_tune, xor_sensor_and_battery, xor_quality_and_flight, loop_sensor_calibration, loop_flight_simulation, compliance_review, packaging_prep, logistics_plan, client_feedback])
root.order.add_edge(component_sourcing, motor_assembly)
root.order.add_edge(motor_assembly, frame_build)
root.order.add_edge(frame_build, software_install)
root.order.add_edge(software_install, algorithm_tune)
root.order.add_edge(algorithm_tune, xor_sensor_and_battery)
root.order.add_edge(xor_sensor_and_battery, loop_sensor_calibration)
root.order.add_edge(loop_sensor_calibration, xor_quality_and_flight)
root.order.add_edge(xor_quality_and_flight, loop_flight_simulation)
root.order.add_edge(loop_flight_simulation, compliance_review)
root.order.add_edge(compliance_review, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_feedback)

# Print the root POWL model
print(root)
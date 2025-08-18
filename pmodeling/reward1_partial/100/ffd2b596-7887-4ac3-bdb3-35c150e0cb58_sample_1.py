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

# Define the loop nodes
sensor_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, battery_integrate, algorithm_tune])
motor_assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[motor_assembly, signal_test])
flight_simulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate, compliance_review])

# Define the exclusive choices
quality_inspect_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, client_feedback])
logistics_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, compliance_review])

# Define the partial order
root = StrictPartialOrder(nodes=[component_sourcing, sensor_calibration_loop, motor_assembly_loop, frame_build, software_install, algorithm_tune, battery_integrate, signal_test, durability_check, flight_simulation_loop, quality_inspect_xor, logistics_plan_xor])
root.order.add_edge(component_sourcing, sensor_calibration_loop)
root.order.add_edge(component_sourcing, motor_assembly_loop)
root.order.add_edge(sensor_calibration_loop, motor_assembly_loop)
root.order.add_edge(motor_assembly_loop, frame_build)
root.order.add_edge(frame_build, software_install)
root.order.add_edge(software_install, algorithm_tune)
root.order.add_edge(algorithm_tune, battery_integrate)
root.order.add_edge(battery_integrate, signal_test)
root.order.add_edge(signal_test, durability_check)
root.order.add_edge(durability_check, flight_simulation_loop)
root.order.add_edge(flight_simulation_loop, quality_inspect_xor)
root.order.add_edge(quality_inspect_xor, logistics_plan_xor)
root.order.add_edge(logistics_plan_xor, client_feedback)
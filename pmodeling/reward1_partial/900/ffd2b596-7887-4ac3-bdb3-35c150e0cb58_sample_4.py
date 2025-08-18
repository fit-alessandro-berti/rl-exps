import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
source_component = Transition(label='Component Sourcing')
sensor_calibration = Transition(label='Sensor Calibrate')
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

# Define silent transitions
skip_quality_inspect = SilentTransition()
skip_compliance_review = SilentTransition()

# Define POWL models
quality_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, skip_quality_inspect])
compliance_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_review, skip_compliance_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    source_component, 
    sensor_calibration, 
    motor_assembly, 
    frame_build, 
    software_install, 
    algorithm_tune, 
    battery_integrate, 
    signal_test, 
    durability_check, 
    flight_simulate, 
    quality_inspect_loop, 
    compliance_review_loop, 
    packaging_prep, 
    logistics_plan, 
    client_feedback
])

# Define dependencies
root.order.add_edge(source_component, sensor_calibration)
root.order.add_edge(source_component, motor_assembly)
root.order.add_edge(sensor_calibration, frame_build)
root.order.add_edge(motor_assembly, frame_build)
root.order.add_edge(frame_build, software_install)
root.order.add_edge(software_install, algorithm_tune)
root.order.add_edge(algorithm_tune, battery_integrate)
root.order.add_edge(battery_integrate, signal_test)
root.order.add_edge(signal_test, durability_check)
root.order.add_edge(durability_check, flight_simulate)
root.order.add_edge(flight_simulate, quality_inspect_loop)
root.order.add_edge(quality_inspect_loop, compliance_review_loop)
root.order.add_edge(compliance_review_loop, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_feedback)

print(root)
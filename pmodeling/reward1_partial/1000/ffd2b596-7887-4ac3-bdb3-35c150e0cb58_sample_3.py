import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
source_component_sourcing = Transition(label='Component Sourcing')
calibrate_sensors = Transition(label='Sensor Calibrate')
assemble_motors = Transition(label='Motor Assembly')
build_frame = Transition(label='Frame Build')
install_software = Transition(label='Software Install')
tune_algorithms = Transition(label='Algorithm Tune')
integrate_battery = Transition(label='Battery Integrate')
signal_test = Transition(label='Signal Test')
durability_check = Transition(label='Durability Check')
flight_simulate = Transition(label='Flight Simulate')
quality_inspect = Transition(label='Quality Inspect')
compliance_review = Transition(label='Compliance Review')
package_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

# Define partial order
root = StrictPartialOrder(nodes=[
    source_component_sourcing,
    calibrate_sensors,
    assemble_motors,
    build_frame,
    install_software,
    tune_algorithms,
    integrate_battery,
    signal_test,
    durability_check,
    flight_simulate,
    quality_inspect,
    compliance_review,
    package_prep,
    logistics_plan,
    client_feedback
])

# Define order relationships
root.order.add_edge(source_component_sourcing, calibrate_sensors)
root.order.add_edge(calibrate_sensors, assemble_motors)
root.order.add_edge(assemble_motors, build_frame)
root.order.add_edge(build_frame, install_software)
root.order.add_edge(install_software, tune_algorithms)
root.order.add_edge(tune_algorithms, integrate_battery)
root.order.add_edge(integrate_battery, signal_test)
root.order.add_edge(signal_test, durability_check)
root.order.add_edge(durability_check, flight_simulate)
root.order.add_edge(flight_simulate, quality_inspect)
root.order.add_edge(quality_inspect, compliance_review)
root.order.add_edge(compliance_review, package_prep)
root.order.add_edge(package_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_feedback)

# Print the root model
print(root)
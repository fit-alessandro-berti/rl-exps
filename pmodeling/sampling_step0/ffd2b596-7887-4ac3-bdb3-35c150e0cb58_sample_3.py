import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sourcing = Transition(label='Component Sourcing')
calibrate = Transition(label='Sensor Calibrate')
assemble_motors = Transition(label='Motor Assembly')
build_frame = Transition(label='Frame Build')
install_software = Transition(label='Software Install')
tune_algorithm = Transition(label='Algorithm Tune')
integrate_battery = Transition(label='Battery Integrate')
signal_test = Transition(label='Signal Test')
durability_check = Transition(label='Durability Check')
flight_simulate = Transition(label='Flight Simulate')
quality_inspect = Transition(label='Quality Inspect')
compliance_review = Transition(label='Compliance Review')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

# Define the silent transitions
skip_sourcing = SilentTransition()
skip_calibrate = SilentTransition()
skip_assemble_motors = SilentTransition()
skip_build_frame = SilentTransition()
skip_install_software = SilentTransition()
skip_tune_algorithm = SilentTransition()
skip_integrate_battery = SilentTransition()
skip_signal_test = SilentTransition()
skip_durability_check = SilentTransition()
skip_flight_simulate = SilentTransition()
skip_quality_inspect = SilentTransition()
skip_compliance_review = SilentTransition()
skip_packaging_prep = SilentTransition()
skip_logistics_plan = SilentTransition()

# Define the partial order
root = StrictPartialOrder(nodes=[sourcing, calibrate, assemble_motors, build_frame, install_software, tune_algorithm, integrate_battery, signal_test, durability_check, flight_simulate, quality_inspect, compliance_review, packaging_prep, logistics_plan, client_feedback])
root.order.add_edge(sourcing, calibrate)
root.order.add_edge(calibrate, assemble_motors)
root.order.add_edge(assemble_motors, build_frame)
root.order.add_edge(build_frame, install_software)
root.order.add_edge(install_software, tune_algorithm)
root.order.add_edge(tune_algorithm, integrate_battery)
root.order.add_edge(integrate_battery, signal_test)
root.order.add_edge(signal_test, durability_check)
root.order.add_edge(durability_check, flight_simulate)
root.order.add_edge(flight_simulate, quality_inspect)
root.order.add_edge(quality_inspect, compliance_review)
root.order.add_edge(compliance_review, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_feedback)

# Print the root
print(root)
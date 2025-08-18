import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

gather_specs = Transition(label='Gather Specs')
adapt_design = Transition(label='Adapt Design')
source_parts = Transition(label='Source Parts')
component_test = Transition(label='Component Test')
assemble_frame = Transition(label='Assemble Frame')
install_firmware = Transition(label='Install Firmware')
calibrate_sensors = Transition(label='Calibrate Sensors')
stress_test = Transition(label='Stress Test')
flight_simulate = Transition(label='Flight Simulate')
validate_battery = Transition(label='Validate Battery')
check_accuracy = Transition(label='Check Accuracy')
package_units = Transition(label='Package Units')
create_manuals = Transition(label='Create Manuals')
ship_drones = Transition(label='Ship Drones')
collect_feedback = Transition(label='Collect Feedback')

xor = OperatorPOWL(operator=Operator.XOR, children=[
    assemble_frame,
    install_firmware,
    calibrate_sensors,
    stress_test,
    flight_simulate,
    validate_battery,
    check_accuracy
])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    package_units,
    create_manuals,
    ship_drones,
    collect_feedback
])

root = StrictPartialOrder(nodes=[
    gather_specs,
    adapt_design,
    source_parts,
    component_test,
    xor,
    xor2
])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, component_test)
root.order.add_edge(component_test, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, package_units)
root.order.add_edge(package_units, create_manuals)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(ship_drones, collect_feedback)
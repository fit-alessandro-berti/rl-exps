import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
client_meet      = Transition(label='Client Meet')
design_draft     = Transition(label='Design Draft')
vendor_select    = Transition(label='Vendor Select')
component_order  = Transition(label='Component Order')
parts_inspect    = Transition(label='Parts Inspect')
frame_build      = Transition(label='Frame Build')
wiring_setup     = Transition(label='Wiring Setup')
software_load    = Transition(label='Software Load')
flight_sim       = Transition(label='Flight Sim')
quality_test     = Transition(label='Quality Test')
feedback_review  = Transition(label='Feedback Review')
adjust_design    = Transition(label='Adjust Design')
compliance_check = Transition(label='Compliance Check')
packaging_prep   = Transition(label='Packaging Prep')
final_demo       = Transition(label='Final Demo')
ship_drone       = Transition(label='Ship Drone')

# Loop for iterative adjustments: do Feedback Review, then either exit or do Adjust Design and Feedback Review again
adjust_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_review, adjust_design]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    client_meet,
    design_draft,
    vendor_select,
    component_order,
    parts_inspect,
    frame_build,
    wiring_setup,
    software_load,
    flight_sim,
    quality_test,
    adjust_loop,
    compliance_check,
    packaging_prep,
    final_demo,
    ship_drone
])

# Sequence edges
root.order.add_edge(client_meet, design_draft)
root.order.add_edge(design_draft, vendor_select)
root.order.add_edge(vendor_select, component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect, frame_build)
root.order.add_edge(frame_build, wiring_setup)
root.order.add_edge(wiring_setup, software_load)
root.order.add_edge(software_load, flight_sim)
root.order.add_edge(flight_sim, quality_test)
root.order.add_edge(quality_test, adjust_loop)
root.order.add_edge(adjust_loop, quality_test)
root.order.add_edge(adjust_loop, compliance_check)
root.order.add_edge(compliance_check, packaging_prep)
root.order.add_edge(packaging_prep, final_demo)
root.order.add_edge(final_demo, ship_drone)

# All nodes are concurrent before the loop starts
for node in [client_meet, design_draft, vendor_select, component_order, parts_inspect, frame_build, wiring_setup, software_load, flight_sim]:
    root.order.add_edge(node, adjust_loop)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
client_meet    = Transition(label='Client Meet')
design_draft   = Transition(label='Design Draft')
vendor_select  = Transition(label='Vendor Select')
component_order= Transition(label='Component Order')
parts_inspect  = Transition(label='Parts Inspect')
frame_build    = Transition(label='Frame Build')
wiring_setup   = Transition(label='Wiring Setup')
software_load  = Transition(label='Software Load')
flight_sim     = Transition(label='Flight Sim')
quality_test   = Transition(label='Quality Test')
feedback_review= Transition(label='Feedback Review')
adjust_design  = Transition(label='Adjust Design')
compliance_check= Transition(label='Compliance Check')
packaging_prep = Transition(label='Packaging Prep')
final_demo     = Transition(label='Final Demo')
ship_drone     = Transition(label='Ship Drone')

# Loop for iterative design adjustments: do Design Draft, then optionally Adjust Design and repeat
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[design_draft, adjust_design]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    client_meet,
    design_loop,
    vendor_select,
    component_order,
    parts_inspect,
    frame_build,
    wiring_setup,
    software_load,
    flight_sim,
    quality_test,
    feedback_review,
    compliance_check,
    packaging_prep,
    final_demo,
    ship_drone
])

# Add ordering constraints
root.order.add_edge(client_meet, vendor_select)
root.order.add_edge(vendor_select, component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect, frame_build)
root.order.add_edge(frame_build, wiring_setup)
root.order.add_edge(wiring_setup, software_load)
root.order.add_edge(software_load, flight_sim)
root.order.add_edge(flight_sim, quality_test)
root.order.add_edge(quality_test, feedback_review)
root.order.add_edge(feedback_review, design_loop)
root.order.add_edge(design_loop, compliance_check)
root.order.add_edge(compliance_check, packaging_prep)
root.order.add_edge(packaging_prep, final_demo)
root.order.add_edge(final_demo, ship_drone)
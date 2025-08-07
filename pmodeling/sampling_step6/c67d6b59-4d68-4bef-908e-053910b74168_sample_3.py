import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
client_meet = Transition(label='Client Meet')
design_draft = Transition(label='Design Draft')
vendor_select = Transition(label='Vendor Select')
component_order = Transition(label='Component Order')
parts_inspect = Transition(label='Parts Inspect')
frame_build = Transition(label='Frame Build')
wiring_setup = Transition(label='Wiring Setup')
software_load = Transition(label='Software Load')
flight_sim = Transition(label='Flight Sim')
quality_test = Transition(label='Quality Test')
feedback_review = Transition(label='Feedback Review')
adjust_design = Transition(label='Adjust Design')
compliance_check = Transition(label='Compliance Check')
packaging_prep = Transition(label='Packaging Prep')
final_demo = Transition(label='Final Demo')
ship_drone = Transition(label='Ship Drone')

# Define the partial order
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
    feedback_review,
    adjust_design,
    compliance_check,
    packaging_prep,
    final_demo,
    ship_drone
])

# Add dependencies
root.order.add_edge(client_meet, design_draft)
root.order.add_edge(client_meet, vendor_select)
root.order.add_edge(client_meet, component_order)
root.order.add_edge(client_meet, parts_inspect)
root.order.add_edge(client_meet, frame_build)
root.order.add_edge(client_meet, wiring_setup)
root.order.add_edge(client_meet, software_load)
root.order.add_edge(client_meet, flight_sim)
root.order.add_edge(client_meet, quality_test)
root.order.add_edge(client_meet, feedback_review)
root.order.add_edge(client_meet, adjust_design)
root.order.add_edge(client_meet, compliance_check)
root.order.add_edge(client_meet, packaging_prep)
root.order.add_edge(client_meet, final_demo)
root.order.add_edge(client_meet, ship_drone)

# Print the root POWL model
print(root)
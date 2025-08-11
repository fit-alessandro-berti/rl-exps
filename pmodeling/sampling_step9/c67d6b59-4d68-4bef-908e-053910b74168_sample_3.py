import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
vendor_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[vendor_select])
component_order_loop = OperatorPOWL(operator=Operator.LOOP, children=[component_order])
parts_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[parts_inspect])
frame_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[frame_build])
wiring_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[wiring_setup])
software_load_loop = OperatorPOWL(operator=Operator.LOOP, children=[software_load])
flight_sim_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_sim])
quality_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_test])
feedback_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])
adjust_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust_design])
compliance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
final_demo_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_demo])
ship_drone_loop = OperatorPOWL(operator=Operator.LOOP, children=[ship_drone])

# Define the exclusive choice (XOR) for feedback review
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])

# Define the exclusive choice (XOR) for software load
xor_software = OperatorPOWL(operator=Operator.XOR, children=[software_load, skip])

# Define the exclusive choice (XOR) for flight sim
xor_flight = OperatorPOWL(operator=Operator.XOR, children=[flight_sim, skip])

# Define the exclusive choice (XOR) for quality test
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_test, skip])

# Define the exclusive choice (XOR) for adjust design
xor_adjust = OperatorPOWL(operator=Operator.XOR, children=[adjust_design, skip])

# Define the exclusive choice (XOR) for compliance check
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define the exclusive choice (XOR) for packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

# Define the exclusive choice (XOR) for final demo
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_demo, skip])

# Define the exclusive choice (XOR) for shipping drone
xor_ship = OperatorPOWL(operator=Operator.XOR, children=[ship_drone, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    client_meet,
    design_draft,
    vendor_select_loop,
    component_order_loop,
    parts_inspect_loop,
    frame_build_loop,
    wiring_setup_loop,
    software_load_loop,
    flight_sim_loop,
    quality_test_loop,
    feedback_review_loop,
    adjust_design_loop,
    compliance_check_loop,
    packaging_prep_loop,
    final_demo_loop,
    ship_drone_loop,
    xor_feedback,
    xor_software,
    xor_flight,
    xor_quality,
    xor_adjust,
    xor_compliance,
    xor_packaging,
    xor_final,
    xor_ship
])

# Add the edges to the root POWL model
root.order.add_edge(client_meet, design_draft)
root.order.add_edge(design_draft, vendor_select_loop)
root.order.add_edge(vendor_select_loop, component_order_loop)
root.order.add_edge(component_order_loop, parts_inspect_loop)
root.order.add_edge(parts_inspect_loop, frame_build_loop)
root.order.add_edge(frame_build_loop, wiring_setup_loop)
root.order.add_edge(wiring_setup_loop, software_load_loop)
root.order.add_edge(software_load_loop, flight_sim_loop)
root.order.add_edge(flight_sim_loop, quality_test_loop)
root.order.add_edge(quality_test_loop, feedback_review_loop)
root.order.add_edge(feedback_review_loop, adjust_design_loop)
root.order.add_edge(adjust_design_loop, compliance_check_loop)
root.order.add_edge(compliance_check_loop, packaging_prep_loop)
root.order.add_edge(packaging_prep_loop, final_demo_loop)
root.order.add_edge(final_demo_loop, ship_drone_loop)
root.order.add_edge(feedback_review_loop, xor_feedback)
root.order.add_edge(software_load_loop, xor_software)
root.order.add_edge(flight_sim_loop, xor_flight)
root.order.add_edge(quality_test_loop, xor_quality)
root.order.add_edge(adjust_design_loop, xor_adjust)
root.order.add_edge(compliance_check_loop, xor_compliance)
root.order.add_edge(packaging_prep_loop, xor_packaging)
root.order.add_edge(final_demo_loop, xor_final)
root.order.add_edge(ship_drone_loop, xor_ship)

# Print the root POWL model
print(root)
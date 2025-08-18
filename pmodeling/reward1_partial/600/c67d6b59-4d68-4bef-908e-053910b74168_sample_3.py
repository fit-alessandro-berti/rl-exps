from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the loop for the design and quality testing process
design_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, quality_test])

# Define the multi-phase quality testing process
quality_test_process = OperatorPOWL(operator=Operator.XOR, children=[quality_test, feedback_review, adjust_design, compliance_check])

# Define the final demo process
final_demo_process = OperatorPOWL(operator=Operator.XOR, children=[final_demo, packaging_prep])

# Define the root process
root = StrictPartialOrder(nodes=[client_meet, vendor_select, component_order, parts_inspect, frame_build, wiring_setup, software_load, design_quality_loop, quality_test_process, final_demo_process, ship_drone])

# Define the dependencies
root.order.add_edge(client_meet, vendor_select)
root.order.add_edge(vendor_select, component_order)
root.order.add_edge(component_order, parts_inspect)
root.order.add_edge(parts_inspect, frame_build)
root.order.add_edge(frame_build, wiring_setup)
root.order.add_edge(wiring_setup, software_load)
root.order.add_edge(software_load, design_quality_loop)
root.order.add_edge(design_quality_loop, quality_test_process)
root.order.add_edge(quality_test_process, final_demo_process)
root.order.add_edge(final_demo_process, packaging_prep)
root.order.add_edge(packaging_prep, ship_drone)

print(root)
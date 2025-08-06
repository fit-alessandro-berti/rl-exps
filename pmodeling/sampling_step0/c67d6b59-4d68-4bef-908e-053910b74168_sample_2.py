import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions for pauses or delays
pause1 = SilentTransition()
pause2 = SilentTransition()
pause3 = SilentTransition()

# Define the loop for the component sourcing and assembly
loop_component = OperatorPOWL(operator=Operator.LOOP, children=[vendor_select, component_order, parts_inspect, frame_build, wiring_setup])
loop_flight_test = OperatorPOWL(operator=Operator.LOOP, children=[flight_sim, software_load, quality_test, feedback_review, adjust_design, compliance_check, packaging_prep])

# Define the exclusive choice for the feedback review and final demo
xor_final_demo = OperatorPOWL(operator=Operator.XOR, children=[final_demo, ship_drone])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[client_meet, design_draft, loop_component, loop_flight_test, xor_final_demo])

# Add dependencies between the nodes
root.order.add_edge(client_meet, design_draft)
root.order.add_edge(design_draft, loop_component)
root.order.add_edge(loop_component, loop_flight_test)
root.order.add_edge(loop_flight_test, xor_final_demo)
root.order.add_edge(xor_final_demo, ship_drone)
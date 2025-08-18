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

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[client_meet, design_draft, vendor_select, component_order, parts_inspect, frame_build, wiring_setup, software_load, flight_sim, quality_test])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review, adjust_design, compliance_check, packaging_prep])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[final_demo, ship_drone])

# Define XOR nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, loop_2])

# Define the root node
root = StrictPartialOrder(nodes=[xor_1, xor_2])
root.order.add_edge(xor_1, xor_2)

print(root)
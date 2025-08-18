import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[vendor_select, component_order])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[parts_inspect, frame_build])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[wiring_setup, software_load])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[flight_sim, quality_test])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, adjust_design])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, packaging_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_demo, ship_drone])

# Define loop
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define root
root = StrictPartialOrder(nodes=[client_meet, loop1])
root.order.add_edge(client_meet, loop1)

print(root)
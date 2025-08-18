import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the POWL model structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[client_meet, vendor_select])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, component_order])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[parts_inspect, frame_build])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[wiring_setup, software_load])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[flight_sim, quality_test])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, adjust_design])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, packaging_prep])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_demo, ship_drone])

# Define the loop for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

print(root)
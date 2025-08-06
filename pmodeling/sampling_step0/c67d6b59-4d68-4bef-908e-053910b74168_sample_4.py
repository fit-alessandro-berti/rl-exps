import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.powl.obj import Transition

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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[frame_build, wiring_setup, software_load, flight_sim, quality_test])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, packaging_prep, final_demo])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[vendor_select, component_order])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, adjust_design])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[client_meet, feedback_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop1)
root.order.add_edge(xor3, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, final_demo)

# Print the root POWL model
print(root)
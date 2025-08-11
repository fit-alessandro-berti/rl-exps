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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, vendor_select])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[component_order, parts_inspect])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[frame_build, wiring_setup])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[software_load, flight_sim])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[quality_test, feedback_review])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[adjust_design, compliance_check])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, final_demo])

# Define exclusive choices
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_6, skip])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[loop_7, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7, ship_drone])
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(xor_3, loop_3)
root.order.add_edge(xor_4, loop_4)
root.order.add_edge(xor_5, loop_5)
root.order.add_edge(xor_6, loop_6)
root.order.add_edge(xor_7, loop_7)
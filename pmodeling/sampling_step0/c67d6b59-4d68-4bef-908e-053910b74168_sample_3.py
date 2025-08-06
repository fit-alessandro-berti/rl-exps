import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, vendor_select])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[component_order, parts_inspect])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[frame_build, wiring_setup])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[software_load, flight_sim])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[quality_test, feedback_review])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[adjust_design, compliance_check])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, final_demo])
loop_8 = OperatorPOWL(operator=Operator.LOOP, children=[ship_drone, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4, loop_5, loop_6, loop_7, loop_8])
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)
root.order.add_edge(loop_5, loop_6)
root.order.add_edge(loop_6, loop_7)
root.order.add_edge(loop_7, loop_8)
root.order.add_edge(loop_8, loop_1)

# Print the root
print(root)
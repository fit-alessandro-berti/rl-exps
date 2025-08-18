import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, packaging_prep])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_demo, ship_drone])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[adjust_design, quality_test])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[flight_sim])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[software_load])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[wiring_setup])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[frame_build, parts_inspect])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[vendor_select, component_order])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, client_meet])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, loop1, loop2, loop3, xor4, xor5, xor6])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(xor4, loop1)
root.order.add_edge(xor5, loop2)
root.order.add_edge(xor6, loop3)

print(root)
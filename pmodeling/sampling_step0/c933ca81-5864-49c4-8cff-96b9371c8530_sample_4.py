import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_consult = Transition(label='Client Consult')
spec_finalize = Transition(label='Spec Finalize')
design_draft = Transition(label='Design Draft')
aerodynamics_test = Transition(label='Aerodynamics Test')
ai_integration = Transition(label='AI Integration')
material_sourcing = Transition(label='Material Sourcing')
component_order = Transition(label='Component Order')
assembly_line = Transition(label='Assembly Line')
firmware_install = Transition(label='Firmware Install')
environmental_test = Transition(label='Environmental Test')
quality_check = Transition(label='Quality Check')
brand_packaging = Transition(label='Brand Packaging')
shipping_prep = Transition(label='Shipping Prep')
delivery_schedule = Transition(label='Delivery Schedule')
post_sale_support = Transition(label='Post-Sale Support')

# Define the workflow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[spec_finalize, client_consult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, aerodynamics_test, ai_integration])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_order])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[assembly_line, firmware_install])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[environmental_test, quality_check])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, post_sale_support])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor5])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor6])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)
root.order.add_edge(loop6, xor6)
root.order.add_edge(loop7, xor7)

print(root)
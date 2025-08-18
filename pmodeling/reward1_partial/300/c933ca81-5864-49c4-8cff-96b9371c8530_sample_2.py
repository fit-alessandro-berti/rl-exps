import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define process structure
xor = OperatorPOWL(operator=Operator.XOR, children=[spec_finalize, client_consult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, aerodynamics_test, ai_integration])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_order])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[assembly_line, firmware_install, environmental_test, quality_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, post_sale_support])

# Connect activities
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor6)
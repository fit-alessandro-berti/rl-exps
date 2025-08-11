import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[assembly_line, component_order, material_sourcing, design_draft, client_consult, ai_integration, aerodynamics_test, quality_check, brand_packaging, shipping_prep, delivery_schedule, post_sale_support])

xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Save the final result in the variable 'root'
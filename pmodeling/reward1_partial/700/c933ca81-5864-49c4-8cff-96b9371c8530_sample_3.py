import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, aerodynamics_test, ai_integration])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_order])
xor_assembly = OperatorPOWL(operator=Operator.XOR, children=[assembly_line, firmware_install])
xor_env = OperatorPOWL(operator=Operator.XOR, children=[environmental_test, quality_check])
xor_brand = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep])
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, post_sale_support])

root = StrictPartialOrder(nodes=[client_consult, spec_finalize, loop_design, xor_material, xor_assembly, xor_env, xor_brand, xor_delivery])
root.order.add_edge(client_consult, spec_finalize)
root.order.add_edge(spec_finalize, loop_design)
root.order.add_edge(loop_design, xor_material)
root.order.add_edge(xor_material, xor_assembly)
root.order.add_edge(xor_assembly, xor_env)
root.order.add_edge(xor_env, xor_brand)
root.order.add_edge(xor_brand, xor_delivery)
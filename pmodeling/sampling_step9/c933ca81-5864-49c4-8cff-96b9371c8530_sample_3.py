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

# Client Consult to Spec Finalize
client_consult_to_spec_finalize = OperatorPOWL(operator=Operator.XOR, children=[client_consult, spec_finalize])

# Spec Finalize to Design Draft
spec_finalize_to_design_draft = OperatorPOWL(operator=Operator.XOR, children=[spec_finalize, design_draft])

# Design Draft to Aerodynamics Test
design_draft_to_aerodynamics_test = OperatorPOWL(operator=Operator.XOR, children=[design_draft, aerodynamics_test])

# Aerodynamics Test to AI Integration
aerodynamics_test_to_ai_integration = OperatorPOWL(operator=Operator.XOR, children=[aerodynamics_test, ai_integration])

# AI Integration to Material Sourcing
ai_integration_to_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[ai_integration, material_sourcing])

# Material Sourcing to Component Order
material_sourcing_to_component_order = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_order])

# Component Order to Assembly Line
component_order_to_assembly_line = OperatorPOWL(operator=Operator.XOR, children=[component_order, assembly_line])

# Assembly Line to Firmware Install
assembly_line_to_firmware_install = OperatorPOWL(operator=Operator.XOR, children=[assembly_line, firmware_install])

# Firmware Install to Environmental Test
firmware_install_to_environmental_test = OperatorPOWL(operator=Operator.XOR, children=[firmware_install, environmental_test])

# Environmental Test to Quality Check
environmental_test_to_quality_check = OperatorPOWL(operator=Operator.XOR, children=[environmental_test, quality_check])

# Quality Check to Brand Packaging
quality_check_to_brand_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_check, brand_packaging])

# Brand Packaging to Shipping Prep
brand_packaging_to_shipping_prep = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep])

# Shipping Prep to Delivery Schedule
shipping_prep_to_delivery_schedule = OperatorPOWL(operator=Operator.XOR, children=[shipping_prep, delivery_schedule])

# Delivery Schedule to Post-Sale Support
delivery_schedule_to_post_sale_support = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, post_sale_support])

root = StrictPartialOrder(nodes=[client_consult_to_spec_finalize, spec_finalize_to_design_draft, design_draft_to_aerodynamics_test, aerodynamics_test_to_ai_integration, ai_integration_to_material_sourcing, material_sourcing_to_component_order, component_order_to_assembly_line, assembly_line_to_firmware_install, firmware_install_to_environmental_test, environmental_test_to_quality_check, quality_check_to_brand_packaging, brand_packaging_to_shipping_prep, shipping_prep_to_delivery_schedule, delivery_schedule_to_post_sale_support])
root.order.add_edge(client_consult_to_spec_finalize, spec_finalize_to_design_draft)
root.order.add_edge(spec_finalize_to_design_draft, design_draft_to_aerodynamics_test)
root.order.add_edge(design_draft_to_aerodynamics_test, aerodynamics_test_to_ai_integration)
root.order.add_edge(aerodynamics_test_to_ai_integration, ai_integration_to_material_sourcing)
root.order.add_edge(ai_integration_to_material_sourcing, material_sourcing_to_component_order)
root.order.add_edge(material_sourcing_to_component_order, component_order_to_assembly_line)
root.order.add_edge(component_order_to_assembly_line, assembly_line_to_firmware_install)
root.order.add_edge(assembly_line_to_firmware_install, firmware_install_to_environmental_test)
root.order.add_edge(firmware_install_to_environmental_test, environmental_test_to_quality_check)
root.order.add_edge(environmental_test_to_quality_check, quality_check_to_brand_packaging)
root.order.add_edge(quality_check_to_brand_packaging, brand_packaging_to_shipping_prep)
root.order.add_edge(brand_packaging_to_shipping_prep, shipping_prep_to_delivery_schedule)
root.order.add_edge(shipping_prep_to_delivery_schedule, delivery_schedule_to_post_sale_support)
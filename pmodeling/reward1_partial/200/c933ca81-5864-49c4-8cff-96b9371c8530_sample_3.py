from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        client_consult, 
        spec_finalize, 
        design_draft, 
        aerodynamics_test, 
        ai_integration, 
        material_sourcing, 
        component_order, 
        assembly_line, 
        firmware_install, 
        environmental_test, 
        quality_check, 
        brand_packaging, 
        shipping_prep, 
        delivery_schedule, 
        post_sale_support
    ],
    order=[
        (client_consult, spec_finalize), 
        (spec_finalize, design_draft), 
        (design_draft, aerodynamics_test), 
        (aerodynamics_test, ai_integration), 
        (ai_integration, material_sourcing), 
        (material_sourcing, component_order), 
        (component_order, assembly_line), 
        (assembly_line, firmware_install), 
        (firmware_install, environmental_test), 
        (environmental_test, quality_check), 
        (quality_check, brand_packaging), 
        (brand_packaging, shipping_prep), 
        (shipping_prep, delivery_schedule), 
        (delivery_schedule, post_sale_support)
    ]
)
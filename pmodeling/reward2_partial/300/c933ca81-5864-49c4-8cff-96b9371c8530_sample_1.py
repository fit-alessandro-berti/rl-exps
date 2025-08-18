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

root = StrictPartialOrder(nodes=[
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
])

root.order.add_edge(client_consult, spec_finalize)
root.order.add_edge(spec_finalize, design_draft)
root.order.add_edge(design_draft, aerodynamics_test)
root.order.add_edge(aerodynamics_test, ai_integration)
root.order.add_edge(ai_integration, material_sourcing)
root.order.add_edge(material_sourcing, component_order)
root.order.add_edge(component_order, assembly_line)
root.order.add_edge(assembly_line, firmware_install)
root.order.add_edge(firmware_install, environmental_test)
root.order.add_edge(environmental_test, quality_check)
root.order.add_edge(quality_check, brand_packaging)
root.order.add_edge(brand_packaging, shipping_prep)
root.order.add_edge(shipping_prep, delivery_schedule)
root.order.add_edge(delivery_schedule, post_sale_support)
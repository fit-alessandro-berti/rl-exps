import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
client_brief    = Transition(label='Client Brief')
concept_sketch  = Transition(label='Concept Sketch')
design_review   = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
vendor_coordination = Transition(label='Vendor Coordination')
prototype_build = Transition(label='Prototype Build')
quality_check   = Transition(label='Quality Check')
client_approval = Transition(label='Client Approval')
packaging_prep  = Transition(label='Packaging Prep')
shipping_arrange = Transition(label='Shipping Arrange')
feedback_collect = Transition(label='Feedback Collect')
portfolio_update = Transition(label='Portfolio Update')
contract_sign   = Transition(label='Contract Sign')
ip_management   = Transition(label='IP Management')
future_schedule = Transition(label='Future Schedule')
maintenance_plan = Transition(label='Maintenance Plan')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    client_brief,
    concept_sketch,
    design_review,
    material_sourcing,
    vendor_coordination,
    prototype_build,
    quality_check,
    client_approval,
    packaging_prep,
    shipping_arrange,
    feedback_collect,
    portfolio_update,
    contract_sign,
    ip_management,
    future_schedule,
    maintenance_plan
])

# Sequence and parallel dependencies
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, design_review)
root.order.add_edge(design_review, material_sourcing)
root.order.add_edge(design_review, vendor_coordination)

root.order.add_edge(material_sourcing, prototype_build)
root.order.add_edge(vendor_coordination, prototype_build)

root.order.add_edge(prototype_build, quality_check)
root.order.add_edge(material_sourcing, quality_check)
root.order.add_edge(vendor_coordination, quality_check)

root.order.add_edge(quality_check, client_approval)
root.order.add_edge(prototype_build, client_approval)
root.order.add_edge(material_sourcing, client_approval)
root.order.add_edge(vendor_coordination, client_approval)

root.order.add_edge(client_approval, packaging_prep)
root.order.add_edge(client_approval, shipping_arrange)

root.order.add_edge(packaging_prep, feedback_collect)
root.order.add_edge(shipping_arrange, feedback_collect)

root.order.add_edge(feedback_collect, portfolio_update)
root.order.add_edge(feedback_collect, contract_sign)

root.order.add_edge(portfolio_update, ip_management)
root.order.add_edge(contract_sign, ip_management)

root.order.add_edge(ip_management, future_schedule)
root.order.add_edge(ip_management, maintenance_plan)
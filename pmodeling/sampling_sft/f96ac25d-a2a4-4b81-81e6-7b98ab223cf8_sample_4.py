import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
client_brief    = Transition(label='Client Brief')
concept_sketch  = Transition(label='Concept Sketch')
design_review   = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
vendor_coordination = Transition(label='Vendor Coordination')
prototype_build = Transition(label='Prototype Build')
quality_check   = Transition(label='Quality Check')
client_approval = Transition(label='Client Approval')
packaging_prep  = Transition(label='Packaging Prep')
shipping_arrange= Transition(label='Shipping Arrange')
feedback_collect= Transition(label='Feedback Collect')
portfolio_update= Transition(label='Portfolio Update')
contract_sign   = Transition(label='Contract Sign')
ip_management   = Transition(label='IP Management')
future_schedule = Transition(label='Future Schedule')
maintenance_plan= Transition(label='Maintenance Plan')

# Build the design phase as a partial order
design_po = StrictPartialOrder(nodes=[
    concept_sketch, design_review, material_sourcing, vendor_coordination, prototype_build, quality_check
])
design_po.order.add_edge(concept_sketch, design_review)
design_po.order.add_edge(design_review, material_sourcing)
design_po.order.add_edge(material_sourcing, vendor_coordination)
design_po.order.add_edge(vendor_coordination, prototype_build)
design_po.order.add_edge(prototype_build, quality_check)

# Build the post-delivery phase as a partial order
post_po = StrictPartialOrder(nodes=[
    feedback_collect, portfolio_update, contract_sign, ip_management, future_schedule, maintenance_plan
])
post_po.order.add_edge(feedback_collect, portfolio_update)
post_po.order.add_edge(portfolio_update, contract_sign)
post_po.order.add_edge(contract_sign, ip_management)
post_po.order.add_edge(ip_management, future_schedule)
post_po.order.add_edge(future_schedule, maintenance_plan)

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    design_po,
    client_approval,
    packaging_prep,
    shipping_arrange,
    post_po
])
root.order.add_edge(client_brief, design_po)
root.order.add_edge(design_po, client_approval)
root.order.add_edge(client_approval, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)
root.order.add_edge(shipping_arrange, post_po)
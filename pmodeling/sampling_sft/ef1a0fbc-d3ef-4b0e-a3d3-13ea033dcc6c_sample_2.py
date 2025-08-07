import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
milk_sourcing    = Transition(label='Milk Sourcing')
farm_selection   = Transition(label='Farm Selection')
quality_testing  = Transition(label='Quality Testing')
milk_pasteurize  = Transition(label='Milk Pasteurize')
starter_culture  = Transition(label='Starter Culture')
coagulation      = Transition(label='Coagulation')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
mold_inoculate   = Transition(label='Mold Inoculate')
aging_control    = Transition(label='Aging Control')
flavor_tasting   = Transition(label='Flavor Tasting')
packaging_design = Transition(label='Packaging Design')
label_approval   = Transition(label='Label Approval')
inventory_audit  = Transition(label='Inventory Audit')
order_fulfill    = Transition(label='Order Fulfill')
retail_shipping  = Transition(label='Retail Shipping')

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    farm_selection,
    quality_testing,
    milk_pasteurize,
    starter_culture,
    coagulation,
    curd_cutting,
    whey_draining,
    mold_inoculate,
    aging_control,
    flavor_tasting,
    packaging_design,
    label_approval,
    inventory_audit,
    order_fulfill,
    retail_shipping
])

# Define the control-flow dependencies
# 1. Milk Sourcing -> Farm Selection
root.order.add_edge(milk_sourcing, farm_selection)

# 2. Farm Selection -> Quality Testing
root.order.add_edge(farm_selection, quality_testing)

# 3. Quality Testing -> Milk Pasteurize
root.order.add_edge(quality_testing, milk_pasteurize)

# 4. Milk Pasteurize -> Starter Culture
root.order.add_edge(milk_pasteurize, starter_culture)

# 5. Starter Culture -> Coagulation
root.order.add_edge(starter_culture, coagulation)

# 6. Coagulation -> Curd Cutting
root.order.add_edge(coagulation, curd_cutting)

# 7. Curd Cutting -> Whey Draining
root.order.add_edge(curd_cutting, whey_draining)

# 8. Whey Draining -> Mold Inoculate
root.order.add_edge(whey_draining, mold_inoculate)

# 9. Mold Inoculate -> Aging Control
root.order.add_edge(mold_inoculate, aging_control)

# 10. Aging Control -> Flavor Tasting
root.order.add_edge(aging_control, flavor_tasting)

# 11. Flavor Tasting -> Packaging Design
root.order.add_edge(flavor_tasting, packaging_design)

# 12. Packaging Design -> Label Approval
root.order.add_edge(packaging_design, label_approval)

# 13. Label Approval -> Inventory Audit
root.order.add_edge(label_approval, inventory_audit)

# 14. Inventory Audit -> Order Fulfill
root.order.add_edge(inventory_audit, order_fulfill)

# 15. Order Fulfill -> Retail Shipping
root.order.add_edge(order_fulfill, retail_shipping)
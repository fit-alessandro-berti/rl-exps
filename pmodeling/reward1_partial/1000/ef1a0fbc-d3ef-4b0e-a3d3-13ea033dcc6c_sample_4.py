from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[])

# Milk Sourcing
milk_sourcing = Transition(label='Milk Sourcing')
root.nodes.append(milk_sourcing)

# Farm Selection
farm_selection = Transition(label='Farm Selection')
root.nodes.append(farm_selection)
root.order.add_edge(milk_sourcing, farm_selection)

# Quality Testing
quality_testing = Transition(label='Quality Testing')
root.nodes.append(quality_testing)
root.order.add_edge(farm_selection, quality_testing)

# Milk Pasteurize
milk_pasteurize = Transition(label='Milk Pasteurize')
root.nodes.append(milk_pasteurize)
root.order.add_edge(quality_testing, milk_pasteurize)

# Starter Culture
starter_culture = Transition(label='Starter Culture')
root.nodes.append(starter_culture)
root.order.add_edge(milk_pasteurize, starter_culture)

# Coagulation
coagulation = Transition(label='Coagulation')
root.nodes.append(coagulation)
root.order.add_edge(starter_culture, coagulation)

# Curd Cutting
curd_cutting = Transition(label='Curd Cutting')
root.nodes.append(curd_cutting)
root.order.add_edge(coagulation, curd_cutting)

# Whey Draining
whey_draining = Transition(label='Whey Draining')
root.nodes.append(whey_draining)
root.order.add_edge(curd_cutting, whey_draining)

# Mold Inoculate
mold_inoculate = Transition(label='Mold Inoculate')
root.nodes.append(mold_inoculate)
root.order.add_edge(whey_draining, mold_inoculate)

# Aging Control
aging_control = Transition(label='Aging Control')
root.nodes.append(aging_control)
root.order.add_edge(mold_inoculate, aging_control)

# Flavor Tasting
flavor_tasting = Transition(label='Flavor Tasting')
root.nodes.append(flavor_tasting)
root.order.add_edge(aging_control, flavor_tasting)

# Packaging Design
packaging_design = Transition(label='Packaging Design')
root.nodes.append(packaging_design)
root.order.add_edge(flavor_tasting, packaging_design)

# Label Approval
label_approval = Transition(label='Label Approval')
root.nodes.append(label_approval)
root.order.add_edge(packaging_design, label_approval)

# Inventory Audit
inventory_audit = Transition(label='Inventory Audit')
root.nodes.append(inventory_audit)
root.order.add_edge(label_approval, inventory_audit)

# Order Fulfill
order_fulfill = Transition(label='Order Fulfill')
root.nodes.append(order_fulfill)
root.order.add_edge(inventory_audit, order_fulfill)

# Retail Shipping
retail_shipping = Transition(label='Retail Shipping')
root.nodes.append(retail_shipping)
root.order.add_edge(order_fulfill, retail_shipping)

# Final Root
root
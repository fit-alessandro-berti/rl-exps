from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
farm_selection = Transition(label='Farm Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_fulfill = Transition(label='Order Fulfill')
retail_shipping = Transition(label='Retail Shipping')

# Define the loop for the aging control process
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])

# Define the exclusive choice for the flavor tasting and packaging design processes
flavor_tasting_packaging = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, packaging_design])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, farm_selection, quality_testing, milk_pasteurize, starter_culture, coagulation, curd_cutting, whey_draining, mold_inoculate, aging_loop, flavor_tasting_packaging, label_approval, inventory_audit, order_fulfill, retail_shipping])

# Define the dependencies between the nodes
root.order.add_edge(milk_sourcing, farm_selection)
root.order.add_edge(farm_selection, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, aging_control)
root.order.add_edge(aging_control, aging_loop)
root.order.add_edge(aging_loop, aging_control)
root.order.add_edge(aging_control, flavor_tasting)
root.order.add_edge(flavor_tasting, packaging_design)
root.order.add_edge(packaging_design, flavor_tasting)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfill)
root.order.add_edge(order_fulfill, retail_shipping)
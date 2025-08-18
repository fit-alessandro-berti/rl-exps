from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the XOR for the quality testing process
quality_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, milk_pasteurize])

# Define the XOR for the milk sourcing process
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])

# Define the XOR for the starter culture process
starter_culture_xor = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, quality_xor])

# Define the XOR for the coagulation process
coagulation_xor = OperatorPOWL(operator=Operator.XOR, children=[coagulation, starter_culture_xor])

# Define the XOR for the curd cutting process
curd_cutting_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, coagulation_xor])

# Define the XOR for the whey draining process
whey_draining_xor = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, curd_cutting_xor])

# Define the XOR for the mold inoculate process
mold_inoculate_xor = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, whey_draining_xor])

# Define the XOR for the aging control process
aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control, mold_inoculate_xor])

# Define the XOR for the flavor tasting process
flavor_tasting_xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, aging_control_xor])

# Define the XOR for the packaging design process
packaging_design_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, flavor_tasting_xor])

# Define the XOR for the label approval process
label_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_design_xor])

# Define the XOR for the inventory audit process
inventory_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, label_approval_xor])

# Define the XOR for the order fulfillment process
order_fulfillment_xor = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, inventory_audit_xor])

# Define the XOR for the retail shipping process
retail_shipping_xor = OperatorPOWL(operator=Operator.XOR, children=[retail_shipping, order_fulfillment_xor])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing_xor, farm_selection, quality_testing, milk_pasteurize, starter_culture, coagulation, curd_cutting, whey_draining, mold_inoculate, aging_control, flavor_tasting, packaging_design, label_approval, inventory_audit, order_fulfill, retail_shipping])
root.order.add_edge(milk_sourcing_xor, farm_selection)
root.order.add_edge(milk_sourcing_xor, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(farm_selection, starter_culture)
root.order.add_edge(starter_culture, quality_xor)
root.order.add_edge(quality_xor, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, aging_control)
root.order.add_edge(aging_control, flavor_tasting)
root.order.add_edge(flavor_tasting, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfill)
root.order.add_edge(order_fulfill, retail_shipping)
root.order.add_edge(retail_shipping, aging_loop)

# Print the POWL model
print(root)
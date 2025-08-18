import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define a loop for aging control
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_tasting])

# Define a choice for flavor tasting
flavor_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, labeling])

# Define a loop for labeling
labeling_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_approval, inventory_audit])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, farm_selection, quality_testing, milk_pasteurize, starter_culture, coagulation, curd_cutting, whey_draining, mold_inoculate, aging_loop, flavor_choice, labeling_loop, packaging_design, order_fulfill, retail_shipping])
root.order.add_edge(milk_sourcing, farm_selection)
root.order.add_edge(farm_selection, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, aging_loop)
root.order.add_edge(aging_loop, flavor_choice)
root.order.add_edge(flavor_choice, labeling_loop)
root.order.add_edge(labeling_loop, packaging_design)
root.order.add_edge(packaging_design, order_fulfill)
root.order.add_edge(order_fulfill, retail_shipping)
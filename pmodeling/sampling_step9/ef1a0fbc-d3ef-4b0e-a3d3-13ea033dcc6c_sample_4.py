import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
farm_selection = Transition(label='Farm Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define the silent activities (tau labels)
skip = SilentTransition()

# Define the loops
milk_processing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, milk_pasturize, starter_culture, coagulation, curd_cutting, whey_draining, mold_inoculate, aging_control, flavor_tasting])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_approval])
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, order_fulfill, retail_shipping])

# Define the choices
seasonal_adjustment = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
order_fulfillment = OperatorPOWL(operator=Operator.XOR, children=[inventory_loop, seasonal_adjustment])

# Define the root
root = StrictPartialOrder(nodes=[milk_processing_loop, packaging_loop, order_fulfillment])
root.order.add_edge(milk_processing_loop, packaging_loop)
root.order.add_edge(packaging_loop, order_fulfillment)
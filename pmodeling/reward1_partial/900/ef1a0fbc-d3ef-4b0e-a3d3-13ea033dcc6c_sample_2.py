import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define exclusive choice for milk pasteurize and starter culture
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, starter_culture])

# Define exclusive choice for quality testing and aging control
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, aging_control])

# Define exclusive choice for mold inoculate and flavor tasting
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, flavor_tasting])

# Define exclusive choice for packaging design and label approval
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define exclusive choice for order fulfill and retail shipping
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, retail_shipping])

# Define loop for inventory audit
inventory_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit])

# Define root process
root = StrictPartialOrder(nodes=[milk_sourcing, farm_selection, exclusive_choice, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, inventory_audit_loop])
root.order.add_edge(milk_sourcing, farm_selection)
root.order.add_edge(farm_selection, exclusive_choice)
root.order.add_edge(exclusive_choice, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, inventory_audit_loop)
root.order.add_edge(inventory_audit_loop, inventory_audit)
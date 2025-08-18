import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, farm_selection, quality_testing, milk_pasturize, starter_culture, coagulation, curd_cutting, whey_draining, mold_inoculate, aging_control, flavor_tasting])
xor_packing = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval, inventory_audit])
xor_order_fulfill = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, retail_shipping])

root = StrictPartialOrder(nodes=[loop_milk_sourcing, xor_packing, xor_order_fulfill])
root.order.add_edge(loop_milk_sourcing, xor_packing)
root.order.add_edge(loop_milk_sourcing, xor_order_fulfill)
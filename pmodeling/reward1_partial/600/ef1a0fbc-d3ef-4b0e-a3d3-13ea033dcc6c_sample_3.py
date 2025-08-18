import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, milk_pasteurize])
xor = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, coagulation])
xor = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, aging_control])
xor = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, packaging_design])
xor = OperatorPOWL(operator=Operator.XOR, children=[label_approval, inventory_audit])
xor = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, retail_shipping])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)
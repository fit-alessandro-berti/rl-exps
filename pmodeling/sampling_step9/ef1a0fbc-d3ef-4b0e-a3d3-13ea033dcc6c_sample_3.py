import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Selection = Transition(label='Farm Selection')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculate = Transition(label='Mold Inoculate')
Aging_Control = Transition(label='Aging Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Fulfill = Transition(label='Order Fulfill')
Retail_Shipping = Transition(label='Retail Shipping')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Farm_Selection, Quality_Testing, Milk_Pasteurize, Starter_Culture, Coagulation, Curd_Cutting, Whey_Draining, Mold_Inoculate, Aging_Control, Flavor_Tasting, Packaging_Design, Label_Approval, Inventory_Audit, Order_Fulfill, Retail_Shipping])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
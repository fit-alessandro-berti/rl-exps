import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Fermentation = Transition(label='Fermentation')
Aging_Control = Transition(label='Aging Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Direct_Delivery = Transition(label='Direct Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Starter_Culture, Quality_Testing, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Pressing_Cheese, Salting_Stage, Fermentation, Aging_Control, Flavor_Tasting, Packaging_Artisanal, Label_Printing, Direct_Delivery, Customer_Feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[Order_Processing, Direct_Delivery])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
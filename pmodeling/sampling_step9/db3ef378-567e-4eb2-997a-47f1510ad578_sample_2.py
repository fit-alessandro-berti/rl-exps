import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Collection = Transition(label='Milk Collection')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Initial_Aging = Transition(label='Initial Aging')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Check = Transition(label='Temperature Check')
Flavor_Testing = Transition(label='Flavor Testing')
Final_Aging = Transition(label='Final Aging')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Fulfillment = Transition(label='Order Fulfillment')
Subscription_Setup = Transition(label='Subscription Setup')
Event_Marketing = Transition(label='Event Marketing')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Collection, Culture_Prep, Curd_Formation, Whey_Separation, Molding_Cheese, Salting_Process, Initial_Aging, Humidity_Control, Temperature_Check, Flavor_Testing, Final_Aging, Packaging_Artisanal, Label_Printing])
xor = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Audit, Order_Fulfillment])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Subscription_Setup, Event_Marketing])

root = StrictPartialOrder(nodes=[loop, xor, xor2])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
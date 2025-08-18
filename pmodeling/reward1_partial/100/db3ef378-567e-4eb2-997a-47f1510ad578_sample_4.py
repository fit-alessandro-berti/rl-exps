import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choices and loops
Whey_Separation_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Whey_Separation])
Salting_Process_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Salting_Process])
Final_Aging_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Final_Aging])
Flavor_Testing_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Flavor_Testing])

Molding_Cheese_XOR = OperatorPOWL(operator=Operator.XOR, children=[Molding_Cheese, Flavor_Testing_Loop])
Culture_Prep_XOR = OperatorPOWL(operator=Operator.XOR, children=[Culture_Prep, Initial_Aging])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Milk_Collection, Culture_Prep_XOR, Whey_Separation_Loop, Salting_Process_Loop, Molding_Cheese_XOR, Final_Aging_Loop, Packaging_Artisanal, Label_Printing, Inventory_Audit, Order_Fulfillment, Subscription_Setup, Event_Marketing])
root.order.add_edge(Milk_Collection, Culture_Prep_XOR)
root.order.add_edge(Culture_Prep_XOR, Whey_Separation_Loop)
root.order.add_edge(Whey_Separation_Loop, Salting_Process_Loop)
root.order.add_edge(Salting_Process_Loop, Molding_Cheese_XOR)
root.order.add_edge(Molding_Cheese_XOR, Final_Aging_Loop)
root.order.add_edge(Final_Aging_Loop, Packaging_Artisanal)
root.order.add_edge(Packaging_Artisanal, Label_Printing)
root.order.add_edge(Label_Printing, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Fulfillment)
root.order.add_edge(Order_Fulfillment, Subscription_Setup)
root.order.add_edge(Subscription_Setup, Event_Marketing)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for the initial aging process
loop_initial_aging = OperatorPOWL(operator=Operator.LOOP, children=[Initial_Aging, Humidity_Control, Temperature_Check, Flavor_Testing])

# Define the choice for the final aging process
choice_final_aging = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the loop for the packaging and labeling process
loop_packaging_labeling = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Artisanal, Label_Printing])

# Define the loop for the inventory audit process
loop_inventory_audit = OperatorPOWL(operator=Operator.LOOP, children=[Inventory_Audit, Order_Fulfillment])

# Define the loop for the subscription setup and event marketing process
loop_subscription_event = OperatorPOWL(operator=Operator.LOOP, children=[Subscription_Setup, Event_Marketing])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_initial_aging, choice_final_aging, loop_packaging_labeling, loop_inventory_audit, loop_subscription_event])
root.order.add_edge(loop_initial_aging, choice_final_aging)
root.order.add_edge(loop_initial_aging, loop_packaging_labeling)
root.order.add_edge(loop_initial_aging, loop_inventory_audit)
root.order.add_edge(loop_initial_aging, loop_subscription_event)
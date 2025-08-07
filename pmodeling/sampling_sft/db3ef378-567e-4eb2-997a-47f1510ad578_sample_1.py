import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
milk_col = Transition(label='Milk Collection')
culture_prep = Transition(label='Culture Prep')
curd_form = Transition(label='Curd Formation')
whey_sep = Transition(label='Whey Separation')
molding = Transition(label='Molding Cheese')
salting = Transition(label='Salting Process')
initial_aging = Transition(label='Initial Aging')
humidity_ctrl = Transition(label='Humidity Control')
temp_check = Transition(label='Temperature Check')
flavor_test = Transition(label='Flavor Testing')
final_aging = Transition(label='Final Aging')
pack_artisanal = Transition(label='Packaging Artisanal')
label_print = Transition(label='Label Printing')
inventory_audit = Transition(label='Inventory Audit')
order_fulfill = Transition(label='Order Fulfillment')
subscription_setup = Transition(label='Subscription Setup')
event_marketing = Transition(label='Event Marketing')

# Loop for repeated flavor testing and aging cycles
flavor_loop = OperatorPOWL(operator=Operator.LOOP, children=[flavor_test, final_aging])

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    milk_col, culture_prep, curd_form, whey_sep, molding, salting,
    initial_aging, humidity_ctrl, temp_check, flavor_loop,
    pack_artisanal, label_print, inventory_audit, order_fulfill,
    subscription_setup, event_marketing
])

# Define the control‐flow dependencies
root.order.add_edge(milk_col, culture_prep)
root.order.add_edge(milk_col, curd_form)
root.order.add_edge(culture_prep, curd_form)
root.order.add_edge(curd_form, whey_sep)
root.order.add_edge(whey_sep, molding)
root.order.add_edge(molding, salting)
root.order.add_edge(salting, initial_aging)
root.order.add_edge(initial_aging, humidity_ctrl)
root.order.add_edge(humidity_ctrl, temp_check)
root.order.add_edge(temp_check, flavor_loop)
root.order.add_edge(flavor_loop, humidity_ctrl)
root.order.add_edge(flavor_loop, temp_check)
root.order.add_edge(flavor_loop, pack_artisanal)
root.order.add_edge(flavor_loop, label_print)
root.order.add_edge(pack_artisanal, inventory_audit)
root.order.add_edge(label_print, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfill)
root.order.add_edge(order_fulfill, subscription_setup)
root.order.add_edge(subscription_setup, event_marketing)

# Print the root model (optional)
print(root)
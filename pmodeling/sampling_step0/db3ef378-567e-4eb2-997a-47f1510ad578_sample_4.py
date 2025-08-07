import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_collection = Transition(label='Milk Collection')
culture_prep = Transition(label='Culture Prep')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
initial_aging = Transition(label='Initial Aging')
humidity_control = Transition(label='Humidity Control')
temperature_check = Transition(label='Temperature Check')
flavor_testing = Transition(label='Flavor Testing')
final_aging = Transition(label='Final Aging')
packaging_artisanal = Transition(label='Packaging Artisanal')
label_printing = Transition(label='Label Printing')
inventory_audit = Transition(label='Inventory Audit')
order_fulfillment = Transition(label='Order Fulfillment')
subscription_setup = Transition(label='Subscription Setup')
event_marketing = Transition(label='Event Marketing')

# Define the partial order
loop_initial_aging = OperatorPOWL(operator=Operator.LOOP, children=[initial_aging, humidity_control, temperature_check, flavor_testing])
xor_order_fulfillment = OperatorPOWL(operator=Operator.XOR, children=[order_fulfillment, subscription_setup])
xor_event_marketing = OperatorPOWL(operator=Operator.XOR, children=[event_marketing, inventory_audit])

# Define the root node
root = StrictPartialOrder(nodes=[milk_collection, culture_prep, curd_formation, whey_separation, molding_cheese, salting_process, loop_initial_aging, xor_order_fulfillment, xor_event_marketing])
root.order.add_edge(milk_collection, culture_prep)
root.order.add_edge(culture_prep, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, loop_initial_aging)
root.order.add_edge(loop_initial_aging, xor_order_fulfillment)
root.order.add_edge(xor_order_fulfillment, xor_event_marketing)
root.order.add_edge(xor_event_marketing, packaging_artisanal)
root.order.add_edge(packaging_artisanal, label_printing)
root.order.add_edge(label_printing, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfillment)
root.order.add_edge(order_fulfillment, subscription_setup)
root.order.add_edge(subscription_setup, event_marketing)
root.order.add_edge(event_marketing, inventory_audit)
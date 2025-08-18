import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define partial order
root = StrictPartialOrder(nodes=[milk_collection, culture_prep, curd_formation, whey_separation, molding_cheese, salting_process, initial_aging, humidity_control, temperature_check, flavor_testing, final_aging, packaging_artisanal, label_printing, inventory_audit, order_fulfillment, subscription_setup, event_marketing])

# Define dependencies between activities
root.order.add_edge(milk_collection, culture_prep)
root.order.add_edge(culture_prep, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, initial_aging)
root.order.add_edge(initial_aging, humidity_control)
root.order.add_edge(humidity_control, temperature_check)
root.order.add_edge(temperature_check, flavor_testing)
root.order.add_edge(flavor_testing, final_aging)
root.order.add_edge(final_aging, packaging_artisanal)
root.order.add_edge(packaging_artisanal, label_printing)
root.order.add_edge(label_printing, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfillment)
root.order.add_edge(order_fulfillment, subscription_setup)
root.order.add_edge(subscription_setup, event_marketing)
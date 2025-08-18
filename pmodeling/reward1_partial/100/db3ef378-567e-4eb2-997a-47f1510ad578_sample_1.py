from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for aging
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, temperature_check, flavor_testing, final_aging])

# Define the choice between initial and final aging
choice_aging = OperatorPOWL(operator=Operator.XOR, children=[initial_aging, loop_aging])

# Define the sequence of activities
sequence = StrictPartialOrder(nodes=[milk_collection, culture_prep, curd_formation, whey_separation, molding_cheese, salting_process, choice_aging, packaging_artisanal, label_printing, inventory_audit, order_fulfillment, subscription_setup, event_marketing])

# Define the edges between nodes
sequence.order.add_edge(milk_collection, culture_prep)
sequence.order.add_edge(culture_prep, curd_formation)
sequence.order.add_edge(curd_formation, whey_separation)
sequence.order.add_edge(whey_separation, molding_cheese)
sequence.order.add_edge(molding_cheese, salting_process)
sequence.order.add_edge(salting_process, choice_aging)
sequence.order.add_edge(choice_aging, packaging_artisanal)
sequence.order.add_edge(packaging_artisanal, label_printing)
sequence.order.add_edge(label_printing, inventory_audit)
sequence.order.add_edge(inventory_audit, order_fulfillment)
sequence.order.add_edge(order_fulfillment, subscription_setup)
sequence.order.add_edge(subscription_setup, event_marketing)

# Save the root
root = sequence
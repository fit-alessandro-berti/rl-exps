import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Milk Sourcing': Transition(label='Milk Sourcing'),
    'Culture Selection': Transition(label='Culture Selection'),
    'Milk Testing': Transition(label='Milk Testing'),
    'Curd Formation': Transition(label='Curd Formation'),
    'Whey Separation': Transition(label='Whey Separation'),
    'Molding Cheese': Transition(label='Molding Cheese'),
    'Salting Process': Transition(label='Salting Process'),
    'Aging Setup': Transition(label='Aging Setup'),
    'Env Monitoring': Transition(label='Env Monitoring'),
    'Flavor Profiling': Transition(label='Flavor Profiling'),
    'Packaging Design': Transition(label='Packaging Design'),
    'Blockchain Entry': Transition(label='Blockchain Entry'),
    'Quality Audit': Transition(label='Quality Audit'),
    'Retail Sync': Transition(label='Retail Sync'),
    'Transport Prep': Transition(label='Transport Prep'),
    'Delivery Tracking': Transition(label='Delivery Tracking'),
    'Customer Feedback': Transition(label='Customer Feedback')
}

# Define the partial order model
root = StrictPartialOrder(nodes=[
    activities['Milk Sourcing'],
    activities['Culture Selection'],
    activities['Milk Testing'],
    activities['Curd Formation'],
    activities['Whey Separation'],
    activities['Molding Cheese'],
    activities['Salting Process'],
    activities['Aging Setup'],
    activities['Env Monitoring'],
    activities['Flavor Profiling'],
    activities['Packaging Design'],
    activities['Blockchain Entry'],
    activities['Quality Audit'],
    activities['Retail Sync'],
    activities['Transport Prep'],
    activities['Delivery Tracking'],
    activities['Customer Feedback']
])

# Define the partial order dependencies
root.order.add_edge(activities['Milk Sourcing'], activities['Culture Selection'])
root.order.add_edge(activities['Milk Sourcing'], activities['Milk Testing'])
root.order.add_edge(activities['Culture Selection'], activities['Curd Formation'])
root.order.add_edge(activities['Curd Formation'], activities['Whey Separation'])
root.order.add_edge(activities['Whey Separation'], activities['Molding Cheese'])
root.order.add_edge(activities['Molding Cheese'], activities['Salting Process'])
root.order.add_edge(activities['Salting Process'], activities['Aging Setup'])
root.order.add_edge(activities['Aging Setup'], activities['Env Monitoring'])
root.order.add_edge(activities['Env Monitoring'], activities['Flavor Profiling'])
root.order.add_edge(activities['Flavor Profiling'], activities['Packaging Design'])
root.order.add_edge(activities['Packaging Design'], activities['Blockchain Entry'])
root.order.add_edge(activities['Blockchain Entry'], activities['Quality Audit'])
root.order.add_edge(activities['Quality Audit'], activities['Retail Sync'])
root.order.add_edge(activities['Retail Sync'], activities['Transport Prep'])
root.order.add_edge(activities['Transport Prep'], activities['Delivery Tracking'])
root.order.add_edge(activities['Delivery Tracking'], activities['Customer Feedback'])

# Print the final POWL model
print(root)
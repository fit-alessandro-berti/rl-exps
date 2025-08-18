import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Milk Sourcing': Transition(label='Milk Sourcing'),
    'Quality Testing': Transition(label='Quality Testing'),
    'Starter Prep': Transition(label='Starter Prep'),
    'Curd Cutting': Transition(label='Curd Cutting'),
    'Molding Cheese': Transition(label='Molding Cheese'),
    'Salting Process': Transition(label='Salting Process'),
    'Aging Control': Transition(label='Aging Control'),
    'Humidity Check': Transition(label='Humidity Check'),
    'Packaging Design': Transition(label='Packaging Design'),
    'Label Printing': Transition(label='Label Printing'),
    'Inventory Audit': Transition(label='Inventory Audit'),
    'Cold Storage': Transition(label='Cold Storage'),
    'Order Processing': Transition(label='Order Processing'),
    'Logistics Planning': Transition(label='Logistics Planning'),
    'Retail Delivery': Transition(label='Retail Delivery'),
    'Consumer Feedback': Transition(label='Consumer Feedback'),
    'Batch Adjustment': Transition(label='Batch Adjustment'),
    'Event Coordination': Transition(label='Event Coordination')
}

# Define the partial order and its dependencies
root = StrictPartialOrder()
root.order.add_edge(activities['Milk Sourcing'], activities['Quality Testing'])
root.order.add_edge(activities['Quality Testing'], activities['Starter Prep'])
root.order.add_edge(activities['Starter Prep'], activities['Curd Cutting'])
root.order.add_edge(activities['Curd Cutting'], activities['Molding Cheese'])
root.order.add_edge(activities['Molding Cheese'], activities['Salting Process'])
root.order.add_edge(activities['Salting Process'], activities['Aging Control'])
root.order.add_edge(activities['Aging Control'], activities['Humidity Check'])
root.order.add_edge(activities['Humidity Check'], activities['Packaging Design'])
root.order.add_edge(activities['Packaging Design'], activities['Label Printing'])
root.order.add_edge(activities['Label Printing'], activities['Inventory Audit'])
root.order.add_edge(activities['Inventory Audit'], activities['Cold Storage'])
root.order.add_edge(activities['Cold Storage'], activities['Order Processing'])
root.order.add_edge(activities['Order Processing'], activities['Logistics Planning'])
root.order.add_edge(activities['Logistics Planning'], activities['Retail Delivery'])
root.order.add_edge(activities['Retail Delivery'], activities['Consumer Feedback'])
root.order.add_edge(activities['Consumer Feedback'], activities['Batch Adjustment'])
root.order.add_edge(activities['Batch Adjustment'], activities['Event Coordination'])

print(root)
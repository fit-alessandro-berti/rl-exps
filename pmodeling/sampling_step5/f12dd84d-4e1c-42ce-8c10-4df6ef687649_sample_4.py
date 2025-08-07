import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with their labels
activities = {
    'Milk Sourcing': Transition(label='Milk Sourcing'),
    'Quality Testing': Transition(label='Quality Testing'),
    'Curd Processing': Transition(label='Curd Processing'),
    'Salt Application': Transition(label='Salt Application'),
    'Mold Inoculation': Transition(label='Mold Inoculation'),
    'Press Molding': Transition(label='Press Molding'),
    'Brine Soaking': Transition(label='Brine Soaking'),
    'Aging Setup': Transition(label='Aging Setup'),
    'Humidity Control': Transition(label='Humidity Control'),
    'Microbial Check': Transition(label='Microbial Check'),
    'Packaging Design': Transition(label='Packaging Design'),
    'Label Printing': Transition(label='Label Printing'),
    'Trace Logging': Transition(label='Trace Logging'),
    'Distribution Plan': Transition(label='Distribution Plan'),
    'Customer Review': Transition(label='Customer Review'),
    'Inventory Audit': Transition(label='Inventory Audit'),
    'Sustainability Audit': Transition(label='Sustainability Audit')
}

# Create partial order nodes for each activity
nodes = [activities[activity] for activity in activities]

# Define dependencies between activities
root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(activities['Milk Sourcing'], activities['Quality Testing'])
root.order.add_edge(activities['Quality Testing'], activities['Curd Processing'])
root.order.add_edge(activities['Curd Processing'], activities['Salt Application'])
root.order.add_edge(activities['Salt Application'], activities['Mold Inoculation'])
root.order.add_edge(activities['Mold Inoculation'], activities['Press Molding'])
root.order.add_edge(activities['Press Molding'], activities['Brine Soaking'])
root.order.add_edge(activities['Brine Soaking'], activities['Aging Setup'])
root.order.add_edge(activities['Aging Setup'], activities['Humidity Control'])
root.order.add_edge(activities['Humidity Control'], activities['Microbial Check'])
root.order.add_edge(activities['Microbial Check'], activities['Packaging Design'])
root.order.add_edge(activities['Packaging Design'], activities['Label Printing'])
root.order.add_edge(activities['Label Printing'], activities['Trace Logging'])
root.order.add_edge(activities['Trace Logging'], activities['Distribution Plan'])
root.order.add_edge(activities['Distribution Plan'], activities['Customer Review'])
root.order.add_edge(activities['Customer Review'], activities['Inventory Audit'])
root.order.add_edge(activities['Inventory Audit'], activities['Sustainability Audit'])
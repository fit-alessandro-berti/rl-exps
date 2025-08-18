import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their respective labels
activities = {
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Risk Assess': Transition(label='Risk Assess'),
    'Supplier Audit': Transition(label='Supplier Audit'),
    'Inventory Scan': Transition(label='Inventory Scan'),
    'Route Optimize': Transition(label='Route Optimize'),
    'Order Prioritize': Transition(label='Order Prioritize'),
    'Contract Review': Transition(label='Contract Review'),
    'Delay Monitor': Transition(label='Delay Monitor'),
    'Shipment Reroute': Transition(label='Shipment Reroute'),
    'Cost Analyze': Transition(label='Cost Analyze'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Alternative Engage': Transition(label='Alternative Engage'),
    'Inventory Reallocate': Transition(label='Inventory Reallocate'),
    'Performance Track': Transition(label='Performance Track'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'Strategy Update': Transition(label='Strategy Update')
}

# Define the partial order model
root = StrictPartialOrder()

# Define the edges in the partial order model
root.order.add_edge(activities['Demand Forecast'], activities['Risk Assess'])
root.order.add_edge(activities['Risk Assess'], activities['Supplier Audit'])
root.order.add_edge(activities['Supplier Audit'], activities['Inventory Scan'])
root.order.add_edge(activities['Inventory Scan'], activities['Route Optimize'])
root.order.add_edge(activities['Route Optimize'], activities['Order Prioritize'])
root.order.add_edge(activities['Order Prioritize'], activities['Contract Review'])
root.order.add_edge(activities['Contract Review'], activities['Delay Monitor'])
root.order.add_edge(activities['Delay Monitor'], activities['Shipment Reroute'])
root.order.add_edge(activities['Shipment Reroute'], activities['Cost Analyze'])
root.order.add_edge(activities['Cost Analyze'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Alternative Engage'])
root.order.add_edge(activities['Alternative Engage'], activities['Inventory Reallocate'])
root.order.add_edge(activities['Inventory Reallocate'], activities['Performance Track'])
root.order.add_edge(activities['Performance Track'], activities['Feedback Loop'])
root.order.add_edge(activities['Feedback Loop'], activities['Strategy Update'])

# Print the final result
print(root)
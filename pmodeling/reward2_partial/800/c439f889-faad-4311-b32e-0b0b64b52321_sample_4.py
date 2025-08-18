import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Seed Sourcing': Transition(label='Seed Sourcing'),
    'Farm Scheduling': Transition(label='Farm Scheduling'),
    'Sensor Monitoring': Transition(label='Sensor Monitoring'),
    'Nutrient Cycling': Transition(label='Nutrient Cycling'),
    'Crop Forecasting': Transition(label='Crop Forecasting'),
    'Pest Inspection': Transition(label='Pest Inspection'),
    'Harvest Timing': Transition(label='Harvest Timing'),
    'Quality Check': Transition(label='Quality Check'),
    'Eco Packaging': Transition(label='Eco Packaging'),
    'Storage Allocation': Transition(label='Storage Allocation'),
    'Order Processing': Transition(label='Order Processing'),
    'Route Planning': Transition(label='Route Planning'),
    'Vehicle Dispatch': Transition(label='Vehicle Dispatch'),
    'Customer Feedback': Transition(label='Customer Feedback'),
    'Demand Analysis': Transition(label='Demand Analysis'),
    'Waste Management': Transition(label='Waste Management'),
    'Community Outreach': Transition(label='Community Outreach')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
root.order.add_edge(activities['Seed Sourcing'], activities['Farm Scheduling'])
root.order.add_edge(activities['Farm Scheduling'], activities['Sensor Monitoring'])
root.order.add_edge(activities['Sensor Monitoring'], activities['Nutrient Cycling'])
root.order.add_edge(activities['Nutrient Cycling'], activities['Crop Forecasting'])
root.order.add_edge(activities['Crop Forecasting'], activities['Pest Inspection'])
root.order.add_edge(activities['Pest Inspection'], activities['Harvest Timing'])
root.order.add_edge(activities['Harvest Timing'], activities['Quality Check'])
root.order.add_edge(activities['Quality Check'], activities['Eco Packaging'])
root.order.add_edge(activities['Eco Packaging'], activities['Storage Allocation'])
root.order.add_edge(activities['Storage Allocation'], activities['Order Processing'])
root.order.add_edge(activities['Order Processing'], activities['Route Planning'])
root.order.add_edge(activities['Route Planning'], activities['Vehicle Dispatch'])
root.order.add_edge(activities['Vehicle Dispatch'], activities['Customer Feedback'])
root.order.add_edge(activities['Customer Feedback'], activities['Demand Analysis'])
root.order.add_edge(activities['Demand Analysis'], activities['Waste Management'])
root.order.add_edge(activities['Waste Management'], activities['Community Outreach'])
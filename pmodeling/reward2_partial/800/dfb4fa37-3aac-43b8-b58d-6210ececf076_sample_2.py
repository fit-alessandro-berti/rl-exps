import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their corresponding labels
activities = {
    'Site Analysis': Transition(label='Site Analysis'),
    'Permit Securing': Transition(label='Permit Securing'),
    'Unit Designing': Transition(label='Unit Designing'),
    'LED Sourcing': Transition(label='LED Sourcing'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Staff Hiring': Transition(label='Staff Hiring'),
    'Pilot Cultivation': Transition(label='Pilot Cultivation'),
    'Data Integration': Transition(label='Data Integration'),
    'Waste Recycling': Transition(label='Waste Recycling'),
    'Local Distribution': Transition(label='Local Distribution'),
    'Subscription Setup': Transition(label='Subscription Setup'),
    'IoT Deployment': Transition(label='IoT Deployment'),
    'Sustainability Audit': Transition(label='Sustainability Audit'),
    'Market Testing': Transition(label='Market Testing'),
    'Process Refinement': Transition(label='Process Refinement')
}

# Define the partial order
root = StrictPartialOrder(nodes=[
    activities['Site Analysis'],
    activities['Permit Securing'],
    activities['Unit Designing'],
    activities['LED Sourcing'],
    activities['Hydroponic Setup'],
    activities['Staff Hiring'],
    activities['Pilot Cultivation'],
    activities['Data Integration'],
    activities['Waste Recycling'],
    activities['Local Distribution'],
    activities['Subscription Setup'],
    activities['IoT Deployment'],
    activities['Sustainability Audit'],
    activities['Market Testing'],
    activities['Process Refinement']
])

# Define the dependencies between activities
root.order.add_edge(activities['Site Analysis'], activities['Permit Securing'])
root.order.add_edge(activities['Permit Securing'], activities['Unit Designing'])
root.order.add_edge(activities['Unit Designing'], activities['LED Sourcing'])
root.order.add_edge(activities['LED Sourcing'], activities['Hydroponic Setup'])
root.order.add_edge(activities['Hydroponic Setup'], activities['Staff Hiring'])
root.order.add_edge(activities['Staff Hiring'], activities['Pilot Cultivation'])
root.order.add_edge(activities['Pilot Cultivation'], activities['Data Integration'])
root.order.add_edge(activities['Data Integration'], activities['Waste Recycling'])
root.order.add_edge(activities['Waste Recycling'], activities['Local Distribution'])
root.order.add_edge(activities['Local Distribution'], activities['Subscription Setup'])
root.order.add_edge(activities['Subscription Setup'], activities['IoT Deployment'])
root.order.add_edge(activities['IoT Deployment'], activities['Sustainability Audit'])
root.order.add_edge(activities['Sustainability Audit'], activities['Market Testing'])
root.order.add_edge(activities['Market Testing'], activities['Process Refinement'])

# Print the final POWL model
print(root)
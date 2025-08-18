import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their respective labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Design Modules': Transition(label='Design Modules'),
    'Install Hydroponics': Transition(label='Install Hydroponics'),
    'Integrate Sensors': Transition(label='Integrate Sensors'),
    'Calibrate Nutrients': Transition(label='Calibrate Nutrients'),
    'Program Climate': Transition(label='Program Climate'),
    'Select Crops': Transition(label='Select Crops'),
    'Optimize Lighting': Transition(label='Optimize Lighting'),
    'Train Staff': Transition(label='Train Staff'),
    'Plan Harvest': Transition(label='Plan Harvest'),
    'Recycle Waste': Transition(label='Recycle Waste'),
    'Analyze Demand': Transition(label='Analyze Demand'),
    'Plan Logistics': Transition(label='Plan Logistics'),
    'Monitor Systems': Transition(label='Monitor Systems')
}

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Regulation Check'],
    activities['Design Modules'],
    activities['Install Hydroponics'],
    activities['Integrate Sensors'],
    activities['Calibrate Nutrients'],
    activities['Program Climate'],
    activities['Select Crops'],
    activities['Optimize Lighting'],
    activities['Train Staff'],
    activities['Plan Harvest'],
    activities['Recycle Waste'],
    activities['Analyze Demand'],
    activities['Plan Logistics'],
    activities['Monitor Systems']
])

# Add dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Design Modules'])
root.order.add_edge(activities['Design Modules'], activities['Install Hydroponics'])
root.order.add_edge(activities['Install Hydroponics'], activities['Integrate Sensors'])
root.order.add_edge(activities['Integrate Sensors'], activities['Calibrate Nutrients'])
root.order.add_edge(activities['Calibrate Nutrients'], activities['Program Climate'])
root.order.add_edge(activities['Program Climate'], activities['Select Crops'])
root.order.add_edge(activities['Select Crops'], activities['Optimize Lighting'])
root.order.add_edge(activities['Optimize Lighting'], activities['Train Staff'])
root.order.add_edge(activities['Train Staff'], activities['Plan Harvest'])
root.order.add_edge(activities['Plan Harvest'], activities['Recycle Waste'])
root.order.add_edge(activities['Recycle Waste'], activities['Analyze Demand'])
root.order.add_edge(activities['Analyze Demand'], activities['Plan Logistics'])
root.order.add_edge(activities['Plan Logistics'], activities['Monitor Systems'])

# Print the final POWL model
print(root)
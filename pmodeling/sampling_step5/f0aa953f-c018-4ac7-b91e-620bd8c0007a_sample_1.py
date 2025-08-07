import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'System Assembly': Transition(label='System Assembly'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Light Calibration': Transition(label='Light Calibration'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Seedling Prep': Transition(label='Seedling Prep'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Data Integration': Transition(label='Data Integration'),
    'Waste Routing': Transition(label='Waste Routing'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Operational Test': Transition(label='Operational Test'),
    'Community Outreach': Transition(label='Community Outreach')
}

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Design Layout'],
    activities['System Assembly'],
    activities['Climate Setup'],
    activities['Light Calibration'],
    activities['Seed Selection'],
    activities['Seedling Prep'],
    activities['Nutrient Mix'],
    activities['Irrigation Setup'],
    activities['Sensor Install'],
    activities['Data Integration'],
    activities['Waste Routing'],
    activities['Energy Audit'],
    activities['Regulation Check'],
    activities['Operational Test'],
    activities['Community Outreach']
])

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['System Assembly'])
root.order.add_edge(activities['System Assembly'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Light Calibration'])
root.order.add_edge(activities['Light Calibration'], activities['Seed Selection'])
root.order.add_edge(activities['Seed Selection'], activities['Seedling Prep'])
root.order.add_edge(activities['Seedling Prep'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Irrigation Setup'])
root.order.add_edge(activities['Irrigation Setup'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Data Integration'])
root.order.add_edge(activities['Data Integration'], activities['Waste Routing'])
root.order.add_edge(activities['Waste Routing'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Operational Test'])
root.order.add_edge(activities['Operational Test'], activities['Community Outreach'])

# Print the root node for verification
print(root)
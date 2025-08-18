import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Climate Scan': Transition(label='Climate Scan'),
    'Module Setup': Transition(label='Module Setup'),
    'Crop Choice': Transition(label='Crop Choice'),
    'Nutrient Feed': Transition(label='Nutrient Feed'),
    'Pest Control': Transition(label='Pest Control'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Waste Cycle': Transition(label='Waste Cycle'),
    'Growth Track': Transition(label='Growth Track'),
    'Demand Plan': Transition(label='Demand Plan'),
    'Community Link': Transition(label='Community Link'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Supply Sync': Transition(label='Supply Sync'),
    'System Upgrade': Transition(label='System Upgrade'),
    'Data Backup': Transition(label='Data Backup')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
root.order.add_edge(activities['Site Survey'], activities['Climate Scan'])
root.order.add_edge(activities['Climate Scan'], activities['Module Setup'])
root.order.add_edge(activities['Module Setup'], activities['Crop Choice'])
root.order.add_edge(activities['Crop Choice'], activities['Nutrient Feed'])
root.order.add_edge(activities['Nutrient Feed'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Waste Cycle'])
root.order.add_edge(activities['Waste Cycle'], activities['Growth Track'])
root.order.add_edge(activities['Growth Track'], activities['Demand Plan'])
root.order.add_edge(activities['Demand Plan'], activities['Community Link'])
root.order.add_edge(activities['Community Link'], activities['Regulation Check'])
root.order.add_edge(activities['Regulation Check'], activities['Supply Sync'])
root.order.add_edge(activities['Supply Sync'], activities['System Upgrade'])
root.order.add_edge(activities['System Upgrade'], activities['Data Backup'])

# Print the result
print(root)
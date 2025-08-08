import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with exactly the same names as in the description
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Install Lighting': Transition(label='Install Lighting'),
    'Setup Hydroponics': Transition(label='Setup Hydroponics'),
    'Calibrate Sensors': Transition(label='Calibrate Sensors'),
    'Select Crops': Transition(label='Select Crops'),
    'Mix Nutrients': Transition(label='Mix Nutrients'),
    'Deploy IoT': Transition(label='Deploy IoT'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Train Staff': Transition(label='Train Staff'),
    'Pest Control': Transition(label='Pest Control'),
    'Legal Review': Transition(label='Legal Review'),
    'Market Analysis': Transition(label='Market Analysis'),
    'Plan Logistics': Transition(label='Plan Logistics'),
    'Yield Review': Transition(label='Yield Review')
}

# Define the partial order
root = StrictPartialOrder(nodes=activities.values())

# Define the order of activities
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Install Lighting'])
root.order.add_edge(activities['Install Lighting'], activities['Setup Hydroponics'])
root.order.add_edge(activities['Setup Hydroponics'], activities['Calibrate Sensors'])
root.order.add_edge(activities['Calibrate Sensors'], activities['Select Crops'])
root.order.add_edge(activities['Select Crops'], activities['Mix Nutrients'])
root.order.add_edge(activities['Mix Nutrients'], activities['Deploy IoT'])
root.order.add_edge(activities['Deploy IoT'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Train Staff'])
root.order.add_edge(activities['Train Staff'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Legal Review'])
root.order.add_edge(activities['Legal Review'], activities['Market Analysis'])
root.order.add_edge(activities['Market Analysis'], activities['Plan Logistics'])
root.order.add_edge(activities['Plan Logistics'], activities['Yield Review'])

# Print the final POWL model
print(root)
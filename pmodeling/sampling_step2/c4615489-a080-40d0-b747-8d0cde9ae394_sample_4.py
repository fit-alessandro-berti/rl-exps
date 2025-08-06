import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Audit': Transition(label='Structural Audit'),
    'Permit Filing': Transition(label='Permit Filing'),
    'Design Layout': Transition(label='Design Layout'),
    'Install HVAC': Transition(label='Install HVAC'),
    'Set Lighting': Transition(label='Set Lighting'),
    'Build Racks': Transition(label='Build Racks'),
    'Install Hydroponics': Transition(label='Install Hydroponics'),
    'Configure Sensors': Transition(label='Configure Sensors'),
    'Select Crops': Transition(label='Select Crops'),
    'Seed Planting': Transition(label='Seed Planting'),
    'Monitor Growth': Transition(label='Monitor Growth'),
    'Nutrient Mixing': Transition(label='Nutrient Mixing'),
    'Staff Training': Transition(label='Staff Training'),
    'Market Launch': Transition(label='Market Launch'),
    'Waste Recycling': Transition(label='Waste Recycling'),
    'Customer Onboarding': Transition(label='Customer Onboarding')
}

# Create a strict partial order with the defined activities
root = StrictPartialOrder(nodes=list(activities.values()))

# Add edges to define the order of activities
root.order.add_edge(activities['Site Survey'], activities['Structural Audit'])
root.order.add_edge(activities['Structural Audit'], activities['Permit Filing'])
root.order.add_edge(activities['Permit Filing'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Install HVAC'])
root.order.add_edge(activities['Install HVAC'], activities['Set Lighting'])
root.order.add_edge(activities['Set Lighting'], activities['Build Racks'])
root.order.add_edge(activities['Build Racks'], activities['Install Hydroponics'])
root.order.add_edge(activities['Install Hydroponics'], activities['Configure Sensors'])
root.order.add_edge(activities['Configure Sensors'], activities['Select Crops'])
root.order.add_edge(activities['Select Crops'], activities['Seed Planting'])
root.order.add_edge(activities['Seed Planting'], activities['Monitor Growth'])
root.order.add_edge(activities['Monitor Growth'], activities['Nutrient Mixing'])
root.order.add_edge(activities['Nutrient Mixing'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Market Launch'])
root.order.add_edge(activities['Market Launch'], activities['Waste Recycling'])
root.order.add_edge(activities['Waste Recycling'], activities['Customer Onboarding'])

# Print the root POWL model
print(root)
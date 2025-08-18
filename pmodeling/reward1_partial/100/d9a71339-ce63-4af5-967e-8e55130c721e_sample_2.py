import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Check': Transition(label='Structural Check'),
    'Modular Install': Transition(label='Modular Install'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'AI Training': Transition(label='AI Training'),
    'Data Capture': Transition(label='Data Capture'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Sync': Transition(label='Harvest Sync'),
    'Quality Test': Transition(label='Quality Test'),
    'Package Prep': Transition(label='Package Prep'),
    'Logistics Plan': Transition(label='Logistics Plan')
}

# Create the POWL model
root = StrictPartialOrder()

# Define the sequence of activities
sequence = [
    activities['Site Survey'],
    activities['Structural Check'],
    activities['Modular Install'],
    activities['Hydroponic Setup'],
    activities['Nutrient Mix'],
    activities['Sensor Setup'],
    activities['AI Training'],
    activities['Data Capture'],
    activities['Maintenance Plan'],
    activities['Pest Scan'],
    activities['Growth Monitor'],
    activities['Harvest Sync'],
    activities['Quality Test'],
    activities['Package Prep'],
    activities['Logistics Plan']
]

# Add the sequence to the root model
for activity in sequence:
    root.add_transition(activity)

# Define the loops and choices (if any, as specified in the process)
# For example, if there are loops or choices, you would add them here
# Example: root.add_loop(...) or root.add_choice(...)

# Add the dependencies between nodes (if any, as specified in the process)
# For example, if there are dependencies, you would add them here
# Example: root.add_edge(...) or root.add_edge(...)

# Return the root of the POWL model
return root
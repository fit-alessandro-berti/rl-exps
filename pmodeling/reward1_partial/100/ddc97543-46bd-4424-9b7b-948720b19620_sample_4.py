import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
transitions = {
    'Site Survey': Transition(label='Site Survey'),
    'Structure Prep': Transition(label='Structure Prep'),
    'System Install': Transition(label='System Install'),
    'Env Control': Transition(label='Env Control'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Crop Select': Transition(label='Crop Select'),
    'AI Setup': Transition(label='AI Setup'),
    'Worker Train': Transition(label='Worker Train'),
    'Pest Control': Transition(label='Pest Control'),
    'Irrigation Plan': Transition(label='Irrigation Plan'),
    'Data Monitor': Transition(label='Data Monitor'),
    'Yield Forecast': Transition(label='Yield Forecast'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Market Setup': Transition(label='Market Setup'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Waste Manage': Transition(label='Waste Manage')
}

# Create a StrictPartialOrder model
root = StrictPartialOrder(nodes=[])

# Define the dependencies between transitions (POWL structure)
root.order.add_edge(transitions['Site Survey'], transitions['Structure Prep'])
root.order.add_edge(transitions['Structure Prep'], transitions['System Install'])
root.order.add_edge(transitions['System Install'], transitions['Env Control'])
root.order.add_edge(transitions['Env Control'], transitions['Nutrient Mix'])
root.order.add_edge(transitions['Nutrient Mix'], transitions['Crop Select'])
root.order.add_edge(transitions['Crop Select'], transitions['AI Setup'])
root.order.add_edge(transitions['AI Setup'], transitions['Worker Train'])
root.order.add_edge(transitions['Worker Train'], transitions['Pest Control'])
root.order.add_edge(transitions['Pest Control'], transitions['Irrigation Plan'])
root.order.add_edge(transitions['Irrigation Plan'], transitions['Data Monitor'])
root.order.add_edge(transitions['Data Monitor'], transitions['Yield Forecast'])
root.order.add_edge(transitions['Yield Forecast'], transitions['Energy Audit'])
root.order.add_edge(transitions['Energy Audit'], transitions['Market Setup'])
root.order.add_edge(transitions['Market Setup'], transitions['Logistics Plan'])
root.order.add_edge(transitions['Logistics Plan'], transitions['Waste Manage'])

# Print the final root model
print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Add activities to the root node
root.add_transition(Transition(label='Site Survey'))
root.add_transition(Transition(label='Design Modules'))
root.add_transition(Transition(label='Climate Setup'))
root.add_transition(Transition(label='Nutrient Mix'))
root.add_transition(Transition(label='LED Tuning'))
root.add_transition(Transition(label='Seed Automation'))
root.add_transition(Transition(label='Growth Monitor'))
root.add_transition(Transition(label='Pest Control'))
root.add_transition(Transition(label='Yield Forecast'))
root.add_transition(Transition(label='Energy Audit'))
root.add_transition(Transition(label='Waste System'))
root.add_transition(Transition(label='Community Meet'))
root.add_transition(Transition(label='Compliance Check'))
root.add_transition(Transition(label='Crop Packing'))
root.add_transition(Transition(label='Logistics Plan'))

# Define dependencies between activities
root.add_edge(root.get_transition('Site Survey'), root.get_transition('Design Modules'))
root.add_edge(root.get_transition('Design Modules'), root.get_transition('Climate Setup'))
root.add_edge(root.get_transition('Design Modules'), root.get_transition('Nutrient Mix'))
root.add_edge(root.get_transition('Design Modules'), root.get_transition('LED Tuning'))
root.add_edge(root.get_transition('Design Modules'), root.get_transition('Seed Automation'))
root.add_edge(root.get_transition('Climate Setup'), root.get_transition('Growth Monitor'))
root.add_edge(root.get_transition('Nutrient Mix'), root.get_transition('Growth Monitor'))
root.add_edge(root.get_transition('LED Tuning'), root.get_transition('Growth Monitor'))
root.add_edge(root.get_transition('Seed Automation'), root.get_transition('Growth Monitor'))
root.add_edge(root.get_transition('Growth Monitor'), root.get_transition('Pest Control'))
root.add_edge(root.get_transition('Pest Control'), root.get_transition('Yield Forecast'))
root.add_edge(root.get_transition('Yield Forecast'), root.get_transition('Energy Audit'))
root.add_edge(root.get_transition('Energy Audit'), root.get_transition('Waste System'))
root.add_edge(root.get_transition('Waste System'), root.get_transition('Community Meet'))
root.add_edge(root.get_transition('Community Meet'), root.get_transition('Compliance Check'))
root.add_edge(root.get_transition('Compliance Check'), root.get_transition('Crop Packing'))
root.add_edge(root.get_transition('Crop Packing'), root.get_transition('Logistics Plan'))

# Print the root node
print(root)
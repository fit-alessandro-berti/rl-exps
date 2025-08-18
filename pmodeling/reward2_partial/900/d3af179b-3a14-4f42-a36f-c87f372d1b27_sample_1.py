import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Modules': Transition(label='Design Modules'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'LED Tuning': Transition(label='LED Tuning'),
    'Seed Automation': Transition(label='Seed Automation'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Pest Control': Transition(label='Pest Control'),
    'Yield Forecast': Transition(label='Yield Forecast'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Waste System': Transition(label='Waste System'),
    'Community Meet': Transition(label='Community Meet'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Crop Packing': Transition(label='Crop Packing'),
    'Logistics Plan': Transition(label='Logistics Plan')
}

# Define the partial order workflow
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Modules'])
root.order.add_edge(activities['Design Modules'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['LED Tuning'])
root.order.add_edge(activities['LED Tuning'], activities['Seed Automation'])
root.order.add_edge(activities['Seed Automation'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Yield Forecast'])
root.order.add_edge(activities['Yield Forecast'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Waste System'])
root.order.add_edge(activities['Waste System'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Crop Packing'])
root.order.add_edge(activities['Crop Packing'], activities['Logistics Plan'])

# Print the final POWL model
print(root)
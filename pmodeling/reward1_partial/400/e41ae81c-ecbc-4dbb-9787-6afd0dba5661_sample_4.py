import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their respective labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structure Reinforce': Transition(label='Structure Reinforce'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Climate Install': Transition(label='Climate Install'),
    'AI Integration': Transition(label='AI Integration'),
    'Seed Sourcing': Transition(label='Seed Sourcing'),
    'Nutrient Prep': Transition(label='Nutrient Prep'),
    'System Testing': Transition(label='System Testing'),
    'Staff Training': Transition(label='Staff Training'),
    'Crop Planting': Transition(label='Crop Planting'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Pest Control': Transition(label='Pest Control'),
    'Harvest Schedule': Transition(label='Harvest Schedule'),
    'Quality Check': Transition(label='Quality Check'),
    'Market Dispatch': Transition(label='Market Dispatch'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'Data Analysis': Transition(label='Data Analysis')
}

# Define the partial order relationships between activities
root = StrictPartialOrder(nodes=list(activities.values()))
root.order.add_edge(activities['Site Survey'], activities['Structure Reinforce'])
root.order.add_edge(activities['Structure Reinforce'], activities['Hydroponic Setup'])
root.order.add_edge(activities['Hydroponic Setup'], activities['Climate Install'])
root.order.add_edge(activities['Climate Install'], activities['AI Integration'])
root.order.add_edge(activities['AI Integration'], activities['Seed Sourcing'])
root.order.add_edge(activities['Seed Sourcing'], activities['Nutrient Prep'])
root.order.add_edge(activities['Nutrient Prep'], activities['System Testing'])
root.order.add_edge(activities['System Testing'], activities['Staff Training'])
root.order.add_edge(activities['Staff Training'], activities['Crop Planting'])
root.order.add_edge(activities['Crop Planting'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Harvest Schedule'])
root.order.add_edge(activities['Harvest Schedule'], activities['Quality Check'])
root.order.add_edge(activities['Quality Check'], activities['Market Dispatch'])
root.order.add_edge(activities['Market Dispatch'], activities['Waste Recycle'])
root.order.add_edge(activities['Waste Recycle'], activities['Data Analysis'])

# Print the root POWL model
print(root)
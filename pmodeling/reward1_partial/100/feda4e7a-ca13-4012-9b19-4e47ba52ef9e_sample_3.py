import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Analysis': Transition(label='Site Analysis'),
    'Env Scanning': Transition(label='Env Scanning'),
    'Farm Design': Transition(label='Farm Design'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Seed Automation': Transition(label='Seed Automation'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Pest Control': Transition(label='Pest Control'),
    'AI Diagnostics': Transition(label='AI Diagnostics'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Robotic Sort': Transition(label='Robotic Sort'),
    'Packaging Line': Transition(label='Packaging Line'),
    'Community Input': Transition(label='Community Input'),
    'Data Aggregation': Transition(label='Data Aggregation'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'Sustainability': Transition(label='Sustainability')
}

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        activities['Site Analysis'],
        activities['Env Scanning'],
        activities['Farm Design'],
        activities['Nutrient Mix'],
        activities['Seed Automation'],
        activities['Growth Monitor'],
        activities['Pest Control'],
        activities['AI Diagnostics'],
        activities['Harvest Plan'],
        activities['Robotic Sort'],
        activities['Packaging Line'],
        activities['Community Input'],
        activities['Data Aggregation'],
        activities['Waste Recycle'],
        activities['Sustainability']
    ]
)

# Add dependencies between nodes (partial order)
root.order.add_edge(activities['Site Analysis'], activities['Env Scanning'])
root.order.add_edge(activities['Site Analysis'], activities['Farm Design'])
root.order.add_edge(activities['Env Scanning'], activities['Farm Design'])
root.order.add_edge(activities['Farm Design'], activities['Nutrient Mix'])
root.order.add_edge(activities['Farm Design'], activities['Seed Automation'])
root.order.add_edge(activities['Seed Automation'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['AI Diagnostics'])
root.order.add_edge(activities['AI Diagnostics'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Robotic Sort'])
root.order.add_edge(activities['Robotic Sort'], activities['Packaging Line'])
root.order.add_edge(activities['Packaging Line'], activities['Community Input'])
root.order.add_edge(activities['Community Input'], activities['Data Aggregation'])
root.order.add_edge(activities['Data Aggregation'], activities['Waste Recycle'])
root.order.add_edge(activities['Waste Recycle'], activities['Sustainability'])

print(root)
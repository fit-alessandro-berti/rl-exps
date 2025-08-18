import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Structure Reinforce', 'Hydroponic Setup', 'Climate Install', 'AI Integration', 'Seed Sourcing', 'Nutrient Prep', 'System Testing', 'Staff Training', 'Crop Planting', 'Growth Monitor', 'Pest Control', 'Harvest Schedule', 'Quality Check', 'Market Dispatch', 'Waste Recycle', 'Data Analysis']

# Create the POWL model
root = StrictPartialOrder(nodes=[Transition(label=activity) for activity in activities])

# Define the dependencies
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Structure Reinforce'))
root.order.add_edge(Transition(label='Structure Reinforce'), Transition(label='Hydroponic Setup'))
root.order.add_edge(Transition(label='Hydroponic Setup'), Transition(label='Climate Install'))
root.order.add_edge(Transition(label='Climate Install'), Transition(label='AI Integration'))
root.order.add_edge(Transition(label='AI Integration'), Transition(label='Seed Sourcing'))
root.order.add_edge(Transition(label='Seed Sourcing'), Transition(label='Nutrient Prep'))
root.order.add_edge(Transition(label='Nutrient Prep'), Transition(label='System Testing'))
root.order.add_edge(Transition(label='System Testing'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Crop Planting'))
root.order.add_edge(Transition(label='Crop Planting'), Transition(label='Growth Monitor'))
root.order.add_edge(Transition(label='Growth Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Harvest Schedule'))
root.order.add_edge(Transition(label='Harvest Schedule'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Market Dispatch'))
root.order.add_edge(Transition(label='Market Dispatch'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Data Analysis'))

print(root)
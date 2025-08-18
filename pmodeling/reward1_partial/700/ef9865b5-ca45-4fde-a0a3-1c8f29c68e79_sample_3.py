import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Permit Review', 'Design Layout', 'Material Sourcing', 'Irrigation Setup', 'Sensor Install', 'Structural Test', 'Recruit Farmers', 'Trial Planting', 'Pest Control', 'Soilless Prep', 'System Calibrate', 'Data Monitor', 'Harvest Plan', 'Community Outreach']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)

# Define the partial order
root.order.add_edge('Site Survey', 'Permit Review')
root.order.add_edge('Permit Review', 'Design Layout')
root.order.add_edge('Design Layout', 'Material Sourcing')
root.order.add_edge('Material Sourcing', 'Irrigation Setup')
root.order.add_edge('Irrigation Setup', 'Sensor Install')
root.order.add_edge('Sensor Install', 'Structural Test')
root.order.add_edge('Structural Test', 'Recruit Farmers')
root.order.add_edge('Recruit Farmers', 'Trial Planting')
root.order.add_edge('Trial Planting', 'Pest Control')
root.order.add_edge('Pest Control', 'Soilless Prep')
root.order.add_edge('Soilless Prep', 'System Calibrate')
root.order.add_edge('System Calibrate', 'Data Monitor')
root.order.add_edge('Data Monitor', 'Harvest Plan')
root.order.add_edge('Harvest Plan', 'Community Outreach')

# Print the POWL model
print(root)
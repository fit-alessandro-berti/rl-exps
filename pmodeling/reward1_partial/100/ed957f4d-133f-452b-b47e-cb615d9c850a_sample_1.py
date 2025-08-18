import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban beekeeping equipment process
# Activities: Source Materials, Vet Suppliers, Design Modules, Prototype Build, Test Durability, Secure Permits, Map Habitats, Micro Warehouse, Inventory Sync, Pack Sustainably, Route Optimize, Engage Community, Collect Feedback, Adjust Production, Partner NGOs, Launch Campaign, Monitor Sensors, Report Impact
activities = ['Source Materials', 'Vet Suppliers', 'Design Modules', 'Prototype Build', 'Test Durability', 'Secure Permits', 'Map Habitats', 'Micro Warehouse', 'Inventory Sync', 'Pack Sustainably', 'Route Optimize', 'Engage Community', 'Collect Feedback', 'Adjust Production', 'Partner NGOs', 'Launch Campaign', 'Monitor Sensors', 'Report Impact']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)
root.order.add_edge(activities[0], activities[1])
root.order.add_edge(activities[1], activities[2])
root.order.add_edge(activities[2], activities[3])
root.order.add_edge(activities[3], activities[4])
root.order.add_edge(activities[4], activities[5])
root.order.add_edge(activities[5], activities[6])
root.order.add_edge(activities[6], activities[7])
root.order.add_edge(activities[7], activities[8])
root.order.add_edge(activities[8], activities[9])
root.order.add_edge(activities[9], activities[10])
root.order.add_edge(activities[10], activities[11])
root.order.add_edge(activities[11], activities[12])
root.order.add_edge(activities[12], activities[13])
root.order.add_edge(activities[13], activities[14])
root.order.add_edge(activities[14], activities[15])
root.order.add_edge(activities[15], activities[16])
root.order.add_edge(activities[16], activities[17])
root.order.add_edge(activities[17], activities[18])
root.order.add_edge(activities[18], activities[19])
root.order.add_edge(activities[19], activities[20])

print(root)
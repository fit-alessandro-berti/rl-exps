import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
activities = [Transition(label=label) for label in ['Site Survey', 'Impact Study', 'Structure Check', 'Soil Testing', 'System Design', 'Seed Selection', 'Irrigation Setup', 'Lighting Install', 'Pest Control', 'Community Meet', 'Regulation Review', 'Waste Plan', 'Crop Monitor', 'Harvest Prep', 'Market Launch']]

# Define the partial order model
root = StrictPartialOrder(nodes=activities)

# Define the dependencies between activities
root.order.add_edge(activities[0], activities[1])  # Site Survey -> Impact Study
root.order.add_edge(activities[0], activities[2])  # Site Survey -> Structure Check
root.order.add_edge(activities[0], activities[3])  # Site Survey -> Soil Testing
root.order.add_edge(activities[1], activities[4])  # Impact Study -> System Design
root.order.add_edge(activities[1], activities[5])  # Impact Study -> Seed Selection
root.order.add_edge(activities[2], activities[6])  # Structure Check -> Irrigation Setup
root.order.add_edge(activities[2], activities[7])  # Structure Check -> Lighting Install
root.order.add_edge(activities[3], activities[8])  # Soil Testing -> Pest Control
root.order.add_edge(activities[3], activities[9])  # Soil Testing -> Community Meet
root.order.add_edge(activities[4], activities[10]) # System Design -> Regulation Review
root.order.add_edge(activities[5], activities[11]) # Seed Selection -> Waste Plan
root.order.add_edge(activities[6], activities[12]) # Irrigation Setup -> Crop Monitor
root.order.add_edge(activities[7], activities[13]) # Lighting Install -> Harvest Prep
root.order.add_edge(activities[8], activities[14]) # Pest Control -> Market Launch
root.order.add_edge(activities[9], activities[14]) # Community Meet -> Market Launch
root.order.add_edge(activities[10], activities[14]) # Regulation Review -> Market Launch
root.order.add_edge(activities[11], activities[14]) # Waste Plan -> Market Launch
root.order.add_edge(activities[12], activities[14]) # Crop Monitor -> Market Launch
root.order.add_edge(activities[13], activities[14]) # Harvest Prep -> Market Launch

# The root variable now contains the fully defined POWL model
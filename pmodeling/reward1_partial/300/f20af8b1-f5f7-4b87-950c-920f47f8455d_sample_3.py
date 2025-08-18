import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
activities = [Transition(label=activity) for activity in ['Site Survey', 'Env Analysis', 'Modular Build', 'Hydroponic Setup', 'Seed Select', 'Nutrient Prep', 'Climate Calibrate', 'Sensor Install', 'AI Integration', 'Crop Monitor', 'Growth Adjust', 'Harvest Sort', 'Packaging', 'Distribution Plan', 'Sustain Audit', 'Energy Optimize']]

# Define the POWL model
root = StrictPartialOrder(nodes=activities)

# Define the dependencies between activities
root.order.add_edge(activities[0], activities[1])  # Site Survey -> Env Analysis
root.order.add_edge(activities[1], activities[2])  # Env Analysis -> Modular Build
root.order.add_edge(activities[2], activities[3])  # Modular Build -> Hydroponic Setup
root.order.add_edge(activities[3], activities[4])  # Hydroponic Setup -> Seed Select
root.order.add_edge(activities[4], activities[5])  # Seed Select -> Nutrient Prep
root.order.add_edge(activities[5], activities[6])  # Nutrient Prep -> Climate Calibrate
root.order.add_edge(activities[6], activities[7])  # Climate Calibrate -> Sensor Install
root.order.add_edge(activities[7], activities[8])  # Sensor Install -> AI Integration
root.order.add_edge(activities[8], activities[9])  # AI Integration -> Crop Monitor
root.order.add_edge(activities[9], activities[10])  # Crop Monitor -> Growth Adjust
root.order.add_edge(activities[10], activities[11])  # Growth Adjust -> Harvest Sort
root.order.add_edge(activities[11], activities[12])  # Harvest Sort -> Packaging
root.order.add_edge(activities[12], activities[13])  # Packaging -> Distribution Plan
root.order.add_edge(activities[13], activities[14])  # Distribution Plan -> Sustain Audit
root.order.add_edge(activities[14], activities[15])  # Sustain Audit -> Energy Optimize

# Print the POWL model
print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'Module Build', 'System Install', 'Water Prep', 'Seed Selection', 'Nutrient Mix', 'Climate Setup', 'Sensor Deploy', 'Pest Scan', 'Growth Monitor', 'Data Sync', 'Energy Manage', 'Harvest Plan', 'Community Link']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order
loop_survey = OperatorPOWL(operator=Operator.LOOP, children=[transitions[0], transitions[1]])
xor_prep = OperatorPOWL(operator=Operator.XOR, children=[transitions[2], transitions[3]])
xor_water = OperatorPOWL(operator=Operator.XOR, children=[transitions[4], SilentTransition()])
xor_seed = OperatorPOWL(operator=Operator.XOR, children=[transitions[5], SilentTransition()])
xor_nutrient = OperatorPOWL(operator=Operator.XOR, children=[transitions[6], SilentTransition()])
xor_climate = OperatorPOWL(operator=Operator.XOR, children=[transitions[7], SilentTransition()])
xor_sensor = OperatorPOWL(operator=Operator.XOR, children=[transitions[8], SilentTransition()])
xor_pest = OperatorPOWL(operator=Operator.XOR, children=[transitions[9], SilentTransition()])
xor_growth = OperatorPOWL(operator=Operator.XOR, children=[transitions[10], SilentTransition()])
xor_sync = OperatorPOWL(operator=Operator.XOR, children=[transitions[11], SilentTransition()])
xor_manage = OperatorPOWL(operator=Operator.XOR, children=[transitions[12], SilentTransition()])
xor_harvest = OperatorPOWL(operator=Operator.XOR, children=[transitions[13], SilentTransition()])
xor_community = OperatorPOWL(operator=Operator.XOR, children=[transitions[14], SilentTransition()])

# Create the root node
root = StrictPartialOrder(nodes=[loop_survey, xor_prep, xor_water, xor_seed, xor_nutrient, xor_climate, xor_sensor, xor_pest, xor_growth, xor_sync, xor_manage, xor_harvest, xor_community])

# Add edges to the partial order
root.order.add_edge(loop_survey, xor_prep)
root.order.add_edge(xor_prep, xor_water)
root.order.add_edge(xor_water, xor_seed)
root.order.add_edge(xor_seed, xor_nutrient)
root.order.add_edge(xor_nutrient, xor_climate)
root.order.add_edge(xor_climate, xor_sensor)
root.order.add_edge(xor_sensor, xor_pest)
root.order.add_edge(xor_pest, xor_growth)
root.order.add_edge(xor_growth, xor_sync)
root.order.add_edge(xor_sync, xor_manage)
root.order.add_edge(xor_manage, xor_harvest)
root.order.add_edge(xor_harvest, xor_community)

# Print the root node
print(root)
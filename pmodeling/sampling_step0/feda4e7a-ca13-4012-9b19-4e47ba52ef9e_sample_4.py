import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
site_analysis = Transition(label='Site Analysis')
env_scanning = Transition(label='Env Scanning')
farm_design = Transition(label='Farm Design')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
ai_diagnostics = Transition(label='AI Diagnostics')
harvest_plan = Transition(label='Harvest Plan')
robotic_sort = Transition(label='Robotic Sort')
packaging_line = Transition(label='Packaging Line')
community_input = Transition(label='Community Input')
data_aggregation = Transition(label='Data Aggregation')
waste_recycle = Transition(label='Waste Recycle')
sustainability = Transition(label='Sustainability')

# Define the silent transition
skip = SilentTransition()

# Define the partial order nodes and their dependencies
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_automation, growth_monitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, ai_diagnostics])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[community_input, data_aggregation])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, sustainability])

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])

# Define the root node and its dependencies
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor1, farm_design)
root.order.add_edge(xor2, nutrient_mix)
root.order.add_edge(xor3, harvest_plan)
root.order.add_edge(xor4, packaging_line)
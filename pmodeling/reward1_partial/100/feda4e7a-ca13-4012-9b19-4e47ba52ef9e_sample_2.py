import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[env_scanning, farm_design, nutrient_mix])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_automation, growth_monitor])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ai_diagnostics, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[robotic_sort, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_line, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[community_input, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[data_aggregation, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop2, xor6)
root.order.add_edge(loop2, xor7)
root.order.add_edge(loop2, xor8)
root.order.add_edge(loop2, xor9)
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for nutrient mix and nutrient mix
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])

# Define the exclusive choice for seed automation and growth monitor
xor_seed_growth = OperatorPOWL(operator=Operator.XOR, children=[seed_automation, growth_monitor])

# Define the exclusive choice for pest control and ai diagnostics
xor_pest_ai = OperatorPOWL(operator=Operator.XOR, children=[pest_control, ai_diagnostics])

# Define the loop for harvest plan and robotic sort
loop_harvest_sort = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, robotic_sort])

# Define the exclusive choice for data aggregation and waste recycle
xor_data_waste = OperatorPOWL(operator=Operator.XOR, children=[data_aggregation, waste_recycle])

# Define the loop for community input and sustainability
loop_community_sustainability = OperatorPOWL(operator=Operator.LOOP, children=[community_input, sustainability])

# Define the root process
root = StrictPartialOrder(nodes=[site_analysis, env_scanning, farm_design, loop_nutrient_mix, xor_seed_growth, xor_pest_ai, loop_harvest_sort, xor_data_waste, loop_community_sustainability])
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(env_scanning, farm_design)
root.order.add_edge(farm_design, loop_nutrient_mix)
root.order.add_edge(loop_nutrient_mix, xor_seed_growth)
root.order.add_edge(xor_seed_growth, xor_pest_ai)
root.order.add_edge(xor_pest_ai, loop_harvest_sort)
root.order.add_edge(loop_harvest_sort, xor_data_waste)
root.order.add_edge(xor_data_waste, loop_community_sustainability)
root.order.add_edge(loop_community_sustainability, sustainability)
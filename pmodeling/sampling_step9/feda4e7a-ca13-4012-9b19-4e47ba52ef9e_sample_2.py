import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define silent transitions
skip = SilentTransition()

# Define the loop nodes
farm_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, env_scanning, farm_design, nutrient_mix, seed_automation, growth_monitor, pest_control, ai_diagnostics])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, robotic_sort, packaging_line])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_input, data_aggregation, waste_recycle])

# Define the exclusive choice nodes
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[sustainability_loop, skip])

# Define the root
root = StrictPartialOrder(nodes=[farm_loop, harvest_loop, exclusive_choice])
root.order.add_edge(farm_loop, harvest_loop)
root.order.add_edge(harvest_loop, exclusive_choice)

print(root)
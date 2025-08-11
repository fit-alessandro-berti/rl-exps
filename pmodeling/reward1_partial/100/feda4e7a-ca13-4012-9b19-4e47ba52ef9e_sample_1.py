import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, ai_diagnostics])
loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, robotic_sort, packaging_line, community_input])
partial_order = StrictPartialOrder(nodes=[site_analysis, env_scanning, farm_design, nutrient_mix, seed_automation, growth_monitor, exclusive_choice, loop, data_aggregation, waste_recycle, sustainability])

# Define the order of transitions
partial_order.order.add_edge(site_analysis, env_scanning)
partial_order.order.add_edge(env_scanning, farm_design)
partial_order.order.add_edge(farm_design, nutrient_mix)
partial_order.order.add_edge(nutrient_mix, seed_automation)
partial_order.order.add_edge(seed_automation, growth_monitor)
partial_order.order.add_edge(growth_monitor, exclusive_choice)
partial_order.order.add_edge(exclusive_choice, harvest_plan)
partial_order.order.add_edge(harvest_plan, robotic_sort)
partial_order.order.add_edge(robotic_sort, packaging_line)
partial_order.order.add_edge(packaging_line, community_input)
partial_order.order.add_edge(community_input, data_aggregation)
partial_order.order.add_edge(data_aggregation, waste_recycle)
partial_order.order.add_edge(waste_recycle, sustainability)

# Set the root
root = partial_order
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for Pest Control and AI Diagnostics
pest_control_or_ai_diagnostics = OperatorPOWL(operator=Operator.XOR, children=[pest_control, ai_diagnostics])

# Define loop for Nutrient Mix
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])

# Define exclusive choice for Harvest Plan and Data Aggregation
harvest_plan_or_data_aggregation = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, data_aggregation])

# Define exclusive choice for Waste Recycle and Sustainability
waste_recycle_or_sustainability = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, sustainability])

# Create the root model
root = StrictPartialOrder(nodes=[
    site_analysis, env_scanning, farm_design, loop_nutrient_mix, seed_automation, growth_monitor, pest_control_or_ai_diagnostics,
    harvest_plan_or_data_aggregation, robotic_sort, packaging_line, community_input, data_aggregation, waste_recycle_or_sustainability
])

# Add dependencies
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(env_scanning, farm_design)
root.order.add_edge(farm_design, loop_nutrient_mix)
root.order.add_edge(loop_nutrient_mix, seed_automation)
root.order.add_edge(seed_automation, growth_monitor)
root.order.add_edge(growth_monitor, pest_control_or_ai_diagnostics)
root.order.add_edge(pest_control_or_ai_diagnostics, harvest_plan_or_data_aggregation)
root.order.add_edge(harvest_plan_or_data_aggregation, robotic_sort)
root.order.add_edge(robotic_sort, packaging_line)
root.order.add_edge(packaging_line, community_input)
root.order.add_edge(community_input, data_aggregation)
root.order.add_edge(data_aggregation, waste_recycle_or_sustainability)
root.order.add_edge(waste_recycle_or_sustainability, sustainability)

# Print the root model
print(root)
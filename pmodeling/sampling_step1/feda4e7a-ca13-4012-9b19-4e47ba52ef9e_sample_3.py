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

# Define the process structure
site_analysis_x_env_scanning = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, env_scanning])
farm_design_x_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[farm_design, nutrient_mix])
seed_automation_x_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[seed_automation, growth_monitor])
pest_control_x_ai_diagnostics = OperatorPOWL(operator=Operator.XOR, children=[pest_control, ai_diagnostics])
harvest_plan_x_robotic_sort = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, robotic_sort])
packaging_line_x_data_aggregation = OperatorPOWL(operator=Operator.XOR, children=[packaging_line, data_aggregation])
waste_recycle_x_sustainability = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, sustainability])

# Connect the activities
root = StrictPartialOrder(nodes=[site_analysis_x_env_scanning, farm_design_x_nutrient_mix, seed_automation_x_growth_monitor, pest_control_x_ai_diagnostics, harvest_plan_x_robotic_sort, packaging_line_x_data_aggregation, waste_recycle_x_sustainability])

# Define the partial order
root.order.add_edge(site_analysis_x_env_scanning, farm_design_x_nutrient_mix)
root.order.add_edge(farm_design_x_nutrient_mix, seed_automation_x_growth_monitor)
root.order.add_edge(seed_automation_x_growth_monitor, pest_control_x_ai_diagnostics)
root.order.add_edge(pest_control_x_ai_diagnostics, harvest_plan_x_robotic_sort)
root.order.add_edge(harvest_plan_x_robotic_sort, packaging_line_x_data_aggregation)
root.order.add_edge(packaging_line_x_data_aggregation, waste_recycle_x_sustainability)

print(root)
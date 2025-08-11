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

# Define the loop for nutrient mix and nutrient mix automation
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_automation])

# Define the exclusive choice for growth monitor and AI diagnostics
growth_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, ai_diagnostics])

# Define the loop for pest control and AI diagnostics
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, ai_diagnostics])

# Define the exclusive choice for harvest plan and robotic sort
harvest_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, robotic_sort])

# Define the exclusive choice for packaging line and community input
packaging_line_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_line, community_input])

# Define the loop for data aggregation and waste recycle
data_aggregation_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_aggregation, waste_recycle])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_scanning,
    farm_design,
    nutrient_mix_loop,
    growth_monitor_choice,
    pest_control_loop,
    harvest_plan_choice,
    packaging_line_choice,
    data_aggregation_loop,
    sustainability
])

# Define the order dependencies
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(site_analysis, farm_design)
root.order.add_edge(env_scanning, nutrient_mix_loop)
root.order.add_edge(farm_design, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, growth_monitor_choice)
root.order.add_edge(growth_monitor_choice, pest_control_loop)
root.order.add_edge(pest_control_loop, harvest_plan_choice)
root.order.add_edge(harvest_plan_choice, packaging_line_choice)
root.order.add_edge(packaging_line_choice, data_aggregation_loop)
root.order.add_edge(data_aggregation_loop, sustainability)

# Print the root node
print(root)
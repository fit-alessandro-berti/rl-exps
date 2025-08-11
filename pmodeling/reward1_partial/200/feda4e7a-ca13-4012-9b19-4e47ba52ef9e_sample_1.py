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

# Define the loop for nutrient mix and nutrient mix with community input
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, community_input])
community_input_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_input, nutrient_mix])

# Define the XOR for pest control and AI diagnostics
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, ai_diagnostics])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_scanning,
    farm_design,
    nutrient_mix_loop,
    seed_automation,
    growth_monitor,
    pest_control_xor,
    harvest_plan,
    robotic_sort,
    packaging_line,
    community_input_loop,
    data_aggregation,
    waste_recycle,
    sustainability
])

# Add the edges to the root model
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(env_scanning, farm_design)
root.order.add_edge(farm_design, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, seed_automation)
root.order.add_edge(seed_automation, growth_monitor)
root.order.add_edge(growth_monitor, pest_control_xor)
root.order.add_edge(pest_control_xor, harvest_plan)
root.order.add_edge(harvest_plan, robotic_sort)
root.order.add_edge(robotic_sort, packaging_line)
root.order.add_edge(packaging_line, community_input_loop)
root.order.add_edge(community_input_loop, data_aggregation)
root.order.add_edge(data_aggregation, waste_recycle)
root.order.add_edge(waste_recycle, sustainability)

print(root)
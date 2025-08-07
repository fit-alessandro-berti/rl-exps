import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis    = Transition(label='Site Analysis')
env_scanning     = Transition(label='Env Scanning')
farm_design      = Transition(label='Farm Design')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_automation  = Transition(label='Seed Automation')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
ai_diagnostics   = Transition(label='AI Diagnostics')
harvest_plan     = Transition(label='Harvest Plan')
robotic_sort     = Transition(label='Robotic Sort')
packaging_line   = Transition(label='Packaging Line')
community_input  = Transition(label='Community Input')
data_aggregation = Transition(label='Data Aggregation')
waste_recycle    = Transition(label='Waste Recycle')
sustainability   = Transition(label='Sustainability')

# Build the loop body: Pest Control -> AI Diagnostics
loop_body = StrictPartialOrder(nodes=[pest_control, ai_diagnostics])
# Loop: do Pest Control, then either exit or do AI Diagnostics and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, pest_control])

# Build the main workflow
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_scanning,
    farm_design,
    nutrient_mix,
    seed_automation,
    growth_monitor,
    loop,
    harvest_plan,
    robotic_sort,
    packaging_line,
    community_input,
    data_aggregation,
    waste_recycle,
    sustainability
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(env_scanning, farm_design)
root.order.add_edge(farm_design, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_automation)
root.order.add_edge(seed_automation, growth_monitor)
root.order.add_edge(growth_monitor, loop)
root.order.add_edge(loop, harvest_plan)
root.order.add_edge(harvest_plan, robotic_sort)
root.order.add_edge(robotic_sort, packaging_line)
root.order.add_edge(packaging_line, community_input)
root.order.add_edge(community_input, data_aggregation)
root.order.add_edge(data_aggregation, sustainability)
root.order.add_edge(sustainability, waste_recycle)
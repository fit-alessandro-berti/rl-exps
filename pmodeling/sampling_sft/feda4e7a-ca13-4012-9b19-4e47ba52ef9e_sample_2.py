import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, env_scanning, farm_design, nutrient_mix,
    seed_automation, growth_monitor, pest_control, ai_diagnostics,
    harvest_plan, robotic_sort, packaging_line, community_input,
    data_aggregation, waste_recycle, sustainability
])

# Define the control-flow edges
# Analysis & scanning must finish before design
root.order.add_edge(site_analysis, farm_design)
root.order.add_edge(env_scanning, farm_design)

# Design & nutrient mix can run in parallel before automation
root.order.add_edge(farm_design, nutrient_mix)
root.order.add_edge(farm_design, seed_automation)

# Automation must finish before monitoring
root.order.add_edge(seed_automation, growth_monitor)

# Monitoring can run in parallel until pest control
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(growth_monitor, ai_diagnostics)

# Pest control must finish before harvest plan
root.order.add_edge(pest_control, harvest_plan)

# Harvest plan can run in parallel until sorting
root.order.add_edge(harvest_plan, robotic_sort)
root.order.add_edge(harvest_plan, packaging_line)

# Sorting must finish before community input
root.order.add_edge(robotic_sort, community_input)
root.order.add_edge(packaging_line, community_input)

# Community input can run in parallel until data aggregation
root.order.add_edge(community_input, data_aggregation)
root.order.add_edge(community_input, waste_recycle)

# Data aggregation must finish before sustainability
root.order.add_edge(data_aggregation, sustainability)

# Waste recycling can run in parallel until sustainability
root.order.add_edge(waste_recycle, sustainability)

# The sequence of all activities up to sustainability completes the process
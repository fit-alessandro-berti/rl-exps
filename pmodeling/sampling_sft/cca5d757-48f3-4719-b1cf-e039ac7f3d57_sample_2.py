import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_assess     = Transition(label='Site Assess')
load_testing    = Transition(label='Load Testing')
climate_study   = Transition(label='Climate Study')
medium_prep     = Transition(label='Medium Prep')
bed_install     = Transition(label='Bed Install')
irrigation_setup= Transition(label='Irrigation Setup')
crop_select     = Transition(label='Crop Select')
pest_control    = Transition(label='Pest Control')
community_meet  = Transition(label='Community Meet')
workshop_plan   = Transition(label='Workshop Plan')
monitor_deploy  = Transition(label='Monitor Deploy')
tech_integrate  = Transition(label='Tech Integrate')
waste_cycle     = Transition(label='Waste Cycle')
yield_forecast  = Transition(label='Yield Forecast')
market_link     = Transition(label='Market Link')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_assess, load_testing, climate_study,
    medium_prep, bed_install, irrigation_setup,
    crop_select, pest_control,
    community_meet, workshop_plan,
    monitor_deploy, tech_integrate,
    waste_cycle, yield_forecast, market_link
])

# Sequence: Site Assess -> Load Testing -> Climate Study
root.order.add_edge(site_assess, load_testing)
root.order.add_edge(load_testing, climate_study)

# Parallel: Medium Prep, Bed Install, Irrigation Setup
for seq in [(medium_prep, bed_install), (bed_install, irrigation_setup), (medium_prep, irrigation_setup)]:
    root.order.add_edge(*seq)

# After preparation, do Crop Select -> Pest Control
root.order.add_edge(climate_study, crop_select)
root.order.add_edge(crop_select, pest_control)

# Community engagement before workshops and monitoring
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(community_meet, workshop_plan)
root.order.add_edge(community_meet, monitor_deploy)

# Parallel: Waste Cycle, Yield Forecast, Market Link
for seq in [(waste_cycle, yield_forecast), (yield_forecast, market_link), (waste_cycle, market_link)]:
    root.order.add_edge(*seq)

# Final deployment and integration
root.order.add_edge(workshop_plan, tech_integrate)
root.order.add_edge(monitor_deploy, tech_integrate)
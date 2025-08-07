import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
climate_setup   = Transition(label='Climate Setup')
sensor_install  = Transition(label='Sensor Install')
automation_code = Transition(label='Automation Code')
nutrient_mix    = Transition(label='Nutrient Mix')
crop_planning   = Transition(label='Crop Planning')
pest_control    = Transition(label='Pest Control')
energy_audit    = Transition(label='Energy Audit')
waste_sort      = Transition(label='Waste Sort')
planting_tier   = Transition(label='Planting Tier')
harvest_prep    = Transition(label='Harvest Prep')
logistics_plan  = Transition(label='Logistics Plan')
community_meet  = Transition(label='Community Meet')
data_review     = Transition(label='Data Review')
system_upgrade  = Transition(label='System Upgrade')

# Define the loop body (Sensor Install -> Automation Code -> Nutrient Mix -> Crop Planning -> Pest Control)
body = StrictPartialOrder(nodes=[sensor_install, automation_code, nutrient_mix, crop_planning, pest_control])
body.order.add_edge(sensor_install, automation_code)
body.order.add_edge(automation_code, nutrient_mix)
body.order.add_edge(nutrient_mix, crop_planning)
body.order.add_edge(crop_planning, pest_control)

# Loop: do body, then optionally do data review and system upgrade, repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, DataReview(), SystemUpgrade()])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    climate_setup,
    loop,
    energy_audit,
    waste_sort,
    planting_tier,
    harvest_prep,
    logistics_plan,
    community_meet
])

# Add control-flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(climate_setup, loop)
root.order.add_edge(loop, energy_audit)
root.order.add_edge(energy_audit, waste_sort)
root.order.add_edge(waste_sort, planting_tier)
root.order.add_edge(planting_tier, harvest_prep)
root.order.add_edge(harvest_prep, logistics_plan)
root.order.add_edge(logistics_plan, community_meet)

# Add optional data review and system upgrade after the loop
root.order.add_edge(loop, data_review)
root.order.add_edge(data_review, system_upgrade)
root.order.add_edge(system_upgrade, community_meet)
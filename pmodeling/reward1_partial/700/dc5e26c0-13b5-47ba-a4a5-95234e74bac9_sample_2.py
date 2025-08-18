import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
nutrient_mix = Transition(label='Nutrient Mix')
automation_code = Transition(label='Automation Code')
crop_planning = Transition(label='Crop Planning')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_sort = Transition(label='Waste Sort')
planting_tier = Transition(label='Planting Tier')
harvest_prep = Transition(label='Harvest Prep')
logistics_plan = Transition(label='Logistics Plan')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
system_upgrade = Transition(label='System Upgrade')

skip = SilentTransition()

# Site Survey
root = StrictPartialOrder(nodes=[site_survey])

# Design Layout
root.order.add_edge(root, design_layout)

# Climate Setup
root.order.add_edge(design_layout, climate_setup)

# Sensor Install
root.order.add_edge(climate_setup, sensor_install)

# Nutrient Mix
root.order.add_edge(sensor_install, nutrient_mix)

# Automation Code
root.order.add_edge(nutrient_mix, automation_code)

# Crop Planning
root.order.add_edge(automation_code, crop_planning)

# Pest Control
root.order.add_edge(crop_planning, pest_control)

# Energy Audit
root.order.add_edge(pest_control, energy_audit)

# Waste Sort
root.order.add_edge(energy_audit, waste_sort)

# Planting Tier
root.order.add_edge(waste_sort, planting_tier)

# Harvest Prep
root.order.add_edge(planting_tier, harvest_prep)

# Logistics Plan
root.order.add_edge(harvest_prep, logistics_plan)

# Community Meet
root.order.add_edge(logistics_plan, community_meet)

# Data Review
root.order.add_edge(community_meet, data_review)

# System Upgrade
root.order.add_edge(data_review, system_upgrade)
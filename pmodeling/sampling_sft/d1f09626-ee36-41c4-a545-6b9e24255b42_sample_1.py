import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
load_test        = Transition(label='Load Test')
soil_sample      = Transition(label='Soil Sample')
climate_check    = Transition(label='Climate Check')
crop_select      = Transition(label='Crop Select')
irrigation_plan  = Transition(label='Irrigation Plan')
energy_setup     = Transition(label='Energy Setup')
pest_control     = Transition(label='Pest Control')
permit_obtain    = Transition(label='Permit Obtain')
stakeholder_meet = Transition(label='Stakeholder Meet')
bed_construction = Transition(label='Bed Construction')
seed_planting    = Transition(label='Seed Planting')
water_schedule   = Transition(label='Water Schedule')
growth_monitor   = Transition(label='Growth Monitor')
harvest_plan     = Transition(label='Harvest Plan')
waste_recycle    = Transition(label='Waste Recycle')
yield_report     = Transition(label='Yield Report')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, climate_check,
    crop_select, irrigation_plan, energy_setup, pest_control,
    permit_obtain, stakeholder_meet, bed_construction, seed_planting,
    water_schedule, growth_monitor, harvest_plan, waste_recycle,
    yield_report
])

# Add dependencies
# Site Survey -> Load Test, Soil Sample, Climate Check
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(site_survey, climate_check)

# Load Test, Soil Sample, Climate Check -> Crop Select
root.order.add_edge(load_test, crop_select)
root.order.add_edge(soil_sample, crop_select)
root.order.add_edge(climate_check, crop_select)

# Crop Select -> Irrigation Plan, Energy Setup, Pest Control
root.order.add_edge(crop_select, irrigation_plan)
root.order.add_edge(crop_select, energy_setup)
root.order.add_edge(crop_select, pest_control)

# Permit Obtain -> Stakeholder Meet
root.order.add_edge(permit_obtain, stakeholder_meet)

# Stakeholder Meet -> Bed Construction
root.order.add_edge(stakeholder_meet, bed_construction)

# Bed Construction -> Seed Planting
root.order.add_edge(bed_construction, seed_planting)

# Seed Planting -> Water Schedule, Growth Monitor
root.order.add_edge(seed_planting, water_schedule)
root.order.add_edge(seed_planting, growth_monitor)

# Water Schedule, Growth Monitor -> Harvest Plan
root.order.add_edge(water_schedule, harvest_plan)
root.order.add_edge(growth_monitor, harvest_plan)

# Harvest Plan -> Waste Recycle, Yield Report
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(harvest_plan, yield_report)

# Waste Recycle, Yield Report can happen in parallel after Harvest Plan
# No explicit edge needed; they're both successors of Harvest Plan
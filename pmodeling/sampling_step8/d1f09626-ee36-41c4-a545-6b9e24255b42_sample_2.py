import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
climate_check = Transition(label='Climate Check')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
energy_setup = Transition(label='Energy Setup')
pest_control = Transition(label='Pest Control')
permit_obtain = Transition(label='Permit Obtain')
stakeholder_meet = Transition(label='Stakeholder Meet')
bed_construction = Transition(label='Bed Construction')
seed_planting = Transition(label='Seed Planting')
water_schedule = Transition(label='Water Schedule')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
yield_report = Transition(label='Yield Report')

skip = SilentTransition()

# Site Survey
root = StrictPartialOrder(nodes=[site_survey])
root.order.add_edge(site_survey, load_test)

# Load Test
root.order.add_edge(load_test, soil_sample)

# Soil Sample
root.order.add_edge(soil_sample, climate_check)

# Climate Check
root.order.add_edge(climate_check, crop_select)

# Crop Select
root.order.add_edge(crop_select, irrigation_plan)

# Irrigation Plan
root.order.add_edge(irrigation_plan, energy_setup)

# Energy Setup
root.order.add_edge(energy_setup, pest_control)

# Pest Control
root.order.add_edge(pest_control, permit_obtain)

# Permit Obtain
root.order.add_edge(permit_obtain, stakeholder_meet)

# Stakeholder Meet
root.order.add_edge(stakeholder_meet, bed_construction)

# Bed Construction
root.order.add_edge(bed_construction, seed_planting)

# Seed Planting
root.order.add_edge(seed_planting, water_schedule)

# Water Schedule
root.order.add_edge(water_schedule, growth_monitor)

# Growth Monitor
root.order.add_edge(growth_monitor, harvest_plan)

# Harvest Plan
root.order.add_edge(harvest_plan, waste_recycle)

# Waste Recycle
root.order.add_edge(waste_recycle, yield_report)

# Yield Report
root.order.add_edge(yield_report, skip)
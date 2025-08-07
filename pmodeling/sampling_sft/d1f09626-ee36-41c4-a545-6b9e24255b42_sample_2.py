import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the maintenance loop: Growth Monitor, then Harvest Plan, then Waste Recycle, repeat
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_recycle])])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, climate_check,
    crop_select, irrigation_plan, energy_setup, pest_control,
    permit_obtain, stakeholder_meet, bed_construction, seed_planting,
    water_schedule, maintenance_loop, yield_report
])

# Sequence of site assessment activities
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(soil_sample, climate_check)
root.order.add_edge(climate_check, crop_select)

# Parallelize irrigation, energy, and pest control
root.order.add_edge(crop_select, irrigation_plan)
root.order.add_edge(crop_select, energy_setup)
root.order.add_edge(crop_select, pest_control)

# Sequence of permit and stakeholder activities
root.order.add_edge(irrigation_plan, permit_obtain)
root.order.add_edge(energy_setup, permit_obtain)
root.order.add_edge(pest_control, permit_obtain)
root.order.add_edge(permit_obtain, stakeholder_meet)

# Sequence of construction and planting
root.order.add_edge(stakeholder_meet, bed_construction)
root.order.add_edge(stakeholder_meet, seed_planting)

# Parallelize watering and monitoring
root.order.add_edge(bed_construction, water_schedule)
root.order.add_edge(seed_planting, water_schedule)
root.order.add_edge(water_schedule, growth_monitor)

# Link maintenance loop to the end
root.order.add_edge(maintenance_loop, yield_report)
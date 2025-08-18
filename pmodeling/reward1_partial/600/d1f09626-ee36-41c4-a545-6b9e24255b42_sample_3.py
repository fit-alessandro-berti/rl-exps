import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    soil_sample,
    climate_check,
    crop_select,
    irrigation_plan,
    energy_setup,
    pest_control,
    permit_obtain,
    stakeholder_meet,
    bed_construction,
    seed_planting,
    water_schedule,
    growth_monitor,
    harvest_plan,
    waste_recycle,
    yield_report
])

# Define the dependencies between activities
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(load_test, climate_check)
root.order.add_edge(soil_sample, climate_check)
root.order.add_edge(climate_check, crop_select)
root.order.add_edge(crop_select, irrigation_plan)
root.order.add_edge(irrigation_plan, energy_setup)
root.order.add_edge(energy_setup, pest_control)
root.order.add_edge(pest_control, permit_obtain)
root.order.add_edge(permit_obtain, stakeholder_meet)
root.order.add_edge(stakeholder_meet, bed_construction)
root.order.add_edge(bed_construction, seed_planting)
root.order.add_edge(seed_planting, water_schedule)
root.order.add_edge(water_schedule, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, yield_report)

# Print the final root
print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order structure
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

# Define dependencies (if any)
# In this case, there are no dependencies between activities, so we don't need to add any edges explicitly.

print(root)
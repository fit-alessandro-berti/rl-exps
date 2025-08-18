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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
site_survey_load_test = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test])
soil_sample_climate_check = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, climate_check])
crop_select_irrigation_plan = OperatorPOWL(operator=Operator.XOR, children=[crop_select, irrigation_plan])
energy_setup_pest_control = OperatorPOWL(operator=Operator.XOR, children=[energy_setup, pest_control])
permit_obtain_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, stakeholder_meet])
bed_construction_seed_planting = OperatorPOWL(operator=Operator.XOR, children=[bed_construction, seed_planting])
water_schedule_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[water_schedule, growth_monitor])
harvest_plan_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_recycle])
yield_report = Transition(label='Yield Report')

# Define loop for yield report
yield_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_report])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey_load_test,
    soil_sample_climate_check,
    crop_select_irrigation_plan,
    energy_setup_pest_control,
    permit_obtain_stakeholder_meet,
    bed_construction_seed_planting,
    water_schedule_growth_monitor,
    harvest_plan_waste_recycle,
    yield_report_loop
])

# Define dependencies
root.order.add_edge(site_survey_load_test, soil_sample_climate_check)
root.order.add_edge(soil_sample_climate_check, crop_select_irrigation_plan)
root.order.add_edge(crop_select_irrigation_plan, energy_setup_pest_control)
root.order.add_edge(energy_setup_pest_control, permit_obtain_stakeholder_meet)
root.order.add_edge(permit_obtain_stakeholder_meet, bed_construction_seed_planting)
root.order.add_edge(bed_construction_seed_planting, water_schedule_growth_monitor)
root.order.add_edge(water_schedule_growth_monitor, harvest_plan_waste_recycle)
root.order.add_edge(harvest_plan_waste_recycle, yield_report_loop)

print(root)
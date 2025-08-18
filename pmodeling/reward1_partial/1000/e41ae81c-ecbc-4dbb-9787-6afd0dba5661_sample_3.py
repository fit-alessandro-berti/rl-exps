import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_reinforce = Transition(label='Structure Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_install = Transition(label='Climate Install')
ai_integration = Transition(label='AI Integration')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_prep = Transition(label='Nutrient Prep')
system_testing = Transition(label='System Testing')
staff_training = Transition(label='Staff Training')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_schedule = Transition(label='Harvest Schedule')
quality_check = Transition(label='Quality Check')
market_dispatch = Transition(label='Market Dispatch')
waste_recycle = Transition(label='Waste Recycle')
data_analysis = Transition(label='Data Analysis')

skip = SilentTransition()

# Define the process
site_survey_to_structure_reinforce = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structure_reinforce])
structure_reinforce_to_hydroponic_setup = OperatorPOWL(operator=Operator.XOR, children=[structure_reinforce, hydroponic_setup])
hydroponic_setup_to_climate_install = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, climate_install])
climate_install_to_ai_integration = OperatorPOWL(operator=Operator.XOR, children=[climate_install, ai_integration])
ai_integration_to_seed_sourcing = OperatorPOWL(operator=Operator.XOR, children=[ai_integration, seed_sourcing])
seed_sourcing_to_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, nutrient_prep])
nutrient_prep_to_system_testing = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, system_testing])
system_testing_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[system_testing, staff_training])
staff_training_to_crop_planting = OperatorPOWL(operator=Operator.XOR, children=[staff_training, crop_planting])
crop_planting_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, growth_monitor])
growth_monitor_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
pest_control_to_harvest_schedule = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_schedule])
harvest_schedule_to_quality_check = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, quality_check])
quality_check_to_market_dispatch = OperatorPOWL(operator=Operator.XOR, children=[quality_check, market_dispatch])
market_dispatch_to_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[market_dispatch, waste_recycle])
waste_recycle_to_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, data_analysis])

root = StrictPartialOrder(nodes=[
    site_survey_to_structure_reinforce,
    structure_reinforce_to_hydroponic_setup,
    hydroponic_setup_to_climate_install,
    climate_install_to_ai_integration,
    ai_integration_to_seed_sourcing,
    seed_sourcing_to_nutrient_prep,
    nutrient_prep_to_system_testing,
    system_testing_to_staff_training,
    staff_training_to_crop_planting,
    crop_planting_to_growth_monitor,
    growth_monitor_to_pest_control,
    pest_control_to_harvest_schedule,
    harvest_schedule_to_quality_check,
    quality_check_to_market_dispatch,
    market_dispatch_to_waste_recycle,
    waste_recycle_to_data_analysis
])

root.order.add_edge(site_survey_to_structure_reinforce, structure_reinforce_to_hydroponic_setup)
root.order.add_edge(structure_reinforce_to_hydroponic_setup, hydroponic_setup_to_climate_install)
root.order.add_edge(hydroponic_setup_to_climate_install, climate_install_to_ai_integration)
root.order.add_edge(climate_install_to_ai_integration, ai_integration_to_seed_sourcing)
root.order.add_edge(ai_integration_to_seed_sourcing, seed_sourcing_to_nutrient_prep)
root.order.add_edge(seed_sourcing_to_nutrient_prep, nutrient_prep_to_system_testing)
root.order.add_edge(nutrient_prep_to_system_testing, system_testing_to_staff_training)
root.order.add_edge(system_testing_to_staff_training, staff_training_to_crop_planting)
root.order.add_edge(staff_training_to_crop_planting, crop_planting_to_growth_monitor)
root.order.add_edge(crop_planting_to_growth_monitor, growth_monitor_to_pest_control)
root.order.add_edge(growth_monitor_to_pest_control, pest_control_to_harvest_schedule)
root.order.add_edge(pest_control_to_harvest_schedule, harvest_schedule_to_quality_check)
root.order.add_edge(harvest_schedule_to_quality_check, quality_check_to_market_dispatch)
root.order.add_edge(quality_check_to_market_dispatch, market_dispatch_to_waste_recycle)
root.order.add_edge(market_dispatch_to_waste_recycle, waste_recycle_to_data_analysis)

# Display the POWL model
print(root)
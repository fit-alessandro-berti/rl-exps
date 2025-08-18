from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_reinforce,
    hydroponic_setup,
    climate_install,
    ai_integration,
    seed_sourcing,
    nutrient_prep,
    system_testing,
    staff_training,
    crop_planting,
    growth_monitor,
    pest_control,
    harvest_schedule,
    quality_check,
    market_dispatch,
    waste_recycle,
    data_analysis
])

# Define the dependencies between activities
root.order.add_edge(site_survey, structure_reinforce)
root.order.add_edge(site_survey, hydroponic_setup)
root.order.add_edge(site_survey, climate_install)
root.order.add_edge(site_survey, ai_integration)
root.order.add_edge(site_survey, seed_sourcing)
root.order.add_edge(site_survey, nutrient_prep)
root.order.add_edge(site_survey, system_testing)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, crop_planting)
root.order.add_edge(site_survey, growth_monitor)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, harvest_schedule)
root.order.add_edge(site_survey, quality_check)
root.order.add_edge(site_survey, market_dispatch)
root.order.add_edge(site_survey, waste_recycle)
root.order.add_edge(site_survey, data_analysis)

root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(structure_reinforce, climate_install)
root.order.add_edge(structure_reinforce, ai_integration)
root.order.add_edge(structure_reinforce, seed_sourcing)
root.order.add_edge(structure_reinforce, nutrient_prep)
root.order.add_edge(structure_reinforce, system_testing)
root.order.add_edge(structure_reinforce, staff_training)
root.order.add_edge(structure_reinforce, crop_planting)
root.order.add_edge(structure_reinforce, growth_monitor)
root.order.add_edge(structure_reinforce, pest_control)
root.order.add_edge(structure_reinforce, harvest_schedule)
root.order.add_edge(structure_reinforce, quality_check)
root.order.add_edge(structure_reinforce, market_dispatch)
root.order.add_edge(structure_reinforce, waste_recycle)
root.order.add_edge(structure_reinforce, data_analysis)

root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(hydroponic_setup, ai_integration)
root.order.add_edge(hydroponic_setup, seed_sourcing)
root.order.add_edge(hydroponic_setup, nutrient_prep)
root.order.add_edge(hydroponic_setup, system_testing)
root.order.add_edge(hydroponic_setup, staff_training)
root.order.add_edge(hydroponic_setup, crop_planting)
root.order.add_edge(hydroponic_setup, growth_monitor)
root.order.add_edge(hydroponic_setup, pest_control)
root.order.add_edge(hydroponic_setup, harvest_schedule)
root.order.add_edge(hydroponic_setup, quality_check)
root.order.add_edge(hydroponic_setup, market_dispatch)
root.order.add_edge(hydroponic_setup, waste_recycle)
root.order.add_edge(hydroponic_setup, data_analysis)

root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(climate_install, seed_sourcing)
root.order.add_edge(climate_install, nutrient_prep)
root.order.add_edge(climate_install, system_testing)
root.order.add_edge(climate_install, staff_training)
root.order.add_edge(climate_install, crop_planting)
root.order.add_edge(climate_install, growth_monitor)
root.order.add_edge(climate_install, pest_control)
root.order.add_edge(climate_install, harvest_schedule)
root.order.add_edge(climate_install, quality_check)
root.order.add_edge(climate_install, market_dispatch)
root.order.add_edge(climate_install, waste_recycle)
root.order.add_edge(climate_install, data_analysis)

root.order.add_edge(ai_integration, seed_sourcing)
root.order.add_edge(ai_integration, nutrient_prep)
root.order.add_edge(ai_integration, system_testing)
root.order.add_edge(ai_integration, staff_training)
root.order.add_edge(ai_integration, crop_planting)
root.order.add_edge(ai_integration, growth_monitor)
root.order.add_edge(ai_integration, pest_control)
root.order.add_edge(ai_integration, harvest_schedule)
root.order.add_edge(ai_integration, quality_check)
root.order.add_edge(ai_integration, market_dispatch)
root.order.add_edge(ai_integration, waste_recycle)
root.order.add_edge(ai_integration, data_analysis)

root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(seed_sourcing, system_testing)
root.order.add_edge(seed_sourcing, staff_training)
root.order.add_edge(seed_sourcing, crop_planting)
root.order.add_edge(seed_sourcing, growth_monitor)
root.order.add_edge(seed_sourcing, pest_control)
root.order.add_edge(seed_sourcing, harvest_schedule)
root.order.add_edge(seed_sourcing, quality_check)
root.order.add_edge(seed_sourcing, market_dispatch)
root.order.add_edge(seed_sourcing, waste_recycle)
root.order.add_edge(seed_sourcing, data_analysis)

root.order.add_edge(nutrient_prep, system_testing)
root.order.add_edge(nutrient_prep, staff_training)
root.order.add_edge(nutrient_prep, crop_planting)
root.order.add_edge(nutrient_prep, growth_monitor)
root.order.add_edge(nutrient_prep, pest_control)
root.order.add_edge(nutrient_prep, harvest_schedule)
root.order.add_edge(nutrient_prep, quality_check)
root.order.add_edge(nutrient_prep, market_dispatch)
root.order.add_edge(nutrient_prep, waste_recycle)
root.order.add_edge(nutrient_prep, data_analysis)

root.order.add_edge(system_testing, staff_training)
root.order.add_edge(system_testing, crop_planting)
root.order.add_edge(system_testing, growth_monitor)
root.order.add_edge(system_testing, pest_control)
root.order.add_edge(system_testing, harvest_schedule)
root.order.add_edge(system_testing, quality_check)
root.order.add_edge(system_testing, market_dispatch)
root.order.add_edge(system_testing, waste_recycle)
root.order.add_edge(system_testing, data_analysis)

root.order.add_edge(staff_training, crop_planting)
root.order.add_edge(staff_training, growth_monitor)
root.order.add_edge(staff_training, pest_control)
root.order.add_edge(staff_training, harvest_schedule)
root.order.add_edge(staff_training, quality_check)
root.order.add_edge(staff_training, market_dispatch)
root.order.add_edge(staff_training, waste_recycle)
root.order.add_edge(staff_training, data_analysis)

root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(crop_planting, pest_control)
root.order.add_edge(crop_planting, harvest_schedule)
root.order.add_edge(crop_planting, quality_check)
root.order.add_edge(crop_planting, market_dispatch)
root.order.add_edge(crop_planting, waste_recycle)
root.order.add_edge(crop_planting, data_analysis)

root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(growth_monitor, harvest_schedule)
root.order.add_edge(growth_monitor, quality_check)
root.order.add_edge(growth_monitor, market_dispatch)
root.order.add_edge(growth_monitor, waste_recycle)
root.order.add_edge(growth_monitor, data_analysis)

root.order.add_edge(pest_control, harvest_schedule)
root.order.add_edge(pest_control, quality_check)
root.order.add_edge(pest_control, market_dispatch)
root.order.add_edge(pest_control, waste_recycle)
root.order.add_edge(pest_control, data_analysis)

root.order.add_edge(harvest_schedule, quality_check)
root.order.add_edge(harvest_schedule, market_dispatch)
root.order.add_edge(harvest_schedule, waste_recycle)
root.order.add_edge(harvest_schedule, data_analysis)

root.order.add_edge(quality_check, market_dispatch)
root.order.add_edge(quality_check, waste_recycle)
root.order.add_edge(quality_check, data_analysis)

root.order.add_edge(market_dispatch, waste_recycle)
root.order.add_edge(market_dispatch, data_analysis)

root.order.add_edge(waste_recycle, data_analysis)

print(root)
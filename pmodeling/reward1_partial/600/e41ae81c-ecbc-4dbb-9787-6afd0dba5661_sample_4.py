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

site_survey_order = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
structure_reinforce_order = OperatorPOWL(operator=Operator.XOR, children=[structure_reinforce, skip])
hydroponic_setup_order = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, skip])
climate_install_order = OperatorPOWL(operator=Operator.XOR, children=[climate_install, skip])
ai_integration_order = OperatorPOWL(operator=Operator.XOR, children=[ai_integration, skip])
seed_sourcing_order = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, skip])
nutrient_prep_order = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
system_testing_order = OperatorPOWL(operator=Operator.XOR, children=[system_testing, skip])
staff_training_order = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
crop_planting_order = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])
growth_monitor_order = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
pest_control_order = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
harvest_schedule_order = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, skip])
quality_check_order = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
market_dispatch_order = OperatorPOWL(operator=Operator.XOR, children=[market_dispatch, skip])
waste_recycle_order = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
data_analysis_order = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])

root = StrictPartialOrder(nodes=[
    site_survey_order,
    structure_reinforce_order,
    hydroponic_setup_order,
    climate_install_order,
    ai_integration_order,
    seed_sourcing_order,
    nutrient_prep_order,
    system_testing_order,
    staff_training_order,
    crop_planting_order,
    growth_monitor_order,
    pest_control_order,
    harvest_schedule_order,
    quality_check_order,
    market_dispatch_order,
    waste_recycle_order,
    data_analysis_order
])

root.order.add_edge(site_survey_order, structure_reinforce_order)
root.order.add_edge(structure_reinforce_order, hydroponic_setup_order)
root.order.add_edge(hydroponic_setup_order, climate_install_order)
root.order.add_edge(climate_install_order, ai_integration_order)
root.order.add_edge(ai_integration_order, seed_sourcing_order)
root.order.add_edge(seed_sourcing_order, nutrient_prep_order)
root.order.add_edge(nutrient_prep_order, system_testing_order)
root.order.add_edge(system_testing_order, staff_training_order)
root.order.add_edge(staff_training_order, crop_planting_order)
root.order.add_edge(crop_planting_order, growth_monitor_order)
root.order.add_edge(growth_monitor_order, pest_control_order)
root.order.add_edge(pest_control_order, harvest_schedule_order)
root.order.add_edge(harvest_schedule_order, quality_check_order)
root.order.add_edge(quality_check_order, market_dispatch_order)
root.order.add_edge(market_dispatch_order, waste_recycle_order)
root.order.add_edge(waste_recycle_order, data_analysis_order)
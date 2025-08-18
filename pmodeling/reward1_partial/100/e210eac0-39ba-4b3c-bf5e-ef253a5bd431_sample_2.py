import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
modular_design = Transition(label='Modular Design')
material_sourcing = Transition(label='Material Sourcing')
energy_integration = Transition(label='Energy Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
system_assembly = Transition(label='System Assembly')
automation_config = Transition(label='Automation Config')
crop_seeding = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
waste_handling = Transition(label='Waste Handling')
community_meet = Transition(label='Community Meet')
data_analysis = Transition(label='Data Analysis')
feedback_loop = Transition(label='Feedback Loop')
yield_forecast = Transition(label='Yield Forecast')

# Define partial order nodes
site_survey_node = OperatorPOWL(operator=Operator.POWL, children=[site_survey, regulation_check])
modular_design_node = OperatorPOWL(operator=Operator.POWL, children=[modular_design, material_sourcing, energy_integration])
climate_setup_node = OperatorPOWL(operator=Operator.POWL, children=[climate_setup, nutrient_mix, system_assembly, automation_config])
crop_seeding_node = OperatorPOWL(operator=Operator.POWL, children=[crop_seeding, growth_monitoring, waste_handling])
community_meet_node = OperatorPOWL(operator=Operator.POWL, children=[community_meet])
data_analysis_node = OperatorPOWL(operator=Operator.POWL, children=[data_analysis])
feedback_loop_node = OperatorPOWL(operator=Operator.POWL, children=[feedback_loop])
yield_forecast_node = OperatorPOWL(operator=Operator.POWL, children=[yield_forecast])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey_node, modular_design_node, climate_setup_node, crop_seeding_node, community_meet_node, data_analysis_node, feedback_loop_node, yield_forecast_node])

# Add dependencies
root.order.add_edge(site_survey_node, modular_design_node)
root.order.add_edge(modular_design_node, climate_setup_node)
root.order.add_edge(climate_setup_node, crop_seeding_node)
root.order.add_edge(crop_seeding_node, community_meet_node)
root.order.add_edge(community_meet_node, data_analysis_node)
root.order.add_edge(data_analysis_node, feedback_loop_node)
root.order.add_edge(feedback_loop_node, yield_forecast_node)

print(root)
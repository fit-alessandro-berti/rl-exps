from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process tree
site_survey_process = OperatorPOWL(operator=Operator.XOR, children=[site_survey, regulation_check])
modular_design_process = OperatorPOWL(operator=Operator.XOR, children=[modular_design, material_sourcing])
energy_integration_process = OperatorPOWL(operator=Operator.XOR, children=[energy_integration, climate_setup])
nutrient_mix_process = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, system_assembly])
automation_config_process = OperatorPOWL(operator=Operator.XOR, children=[automation_config, crop_seeding])
growth_monitoring_process = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, waste_handling])
community_meet_process = OperatorPOWL(operator=Operator.XOR, children=[community_meet, data_analysis])
feedback_loop_process = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, yield_forecast])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey_process,
    modular_design_process,
    energy_integration_process,
    nutrient_mix_process,
    automation_config_process,
    growth_monitoring_process,
    community_meet_process,
    feedback_loop_process
])

# Add edges to the root POWL model
root.order.add_edge(site_survey_process, modular_design_process)
root.order.add_edge(site_survey_process, energy_integration_process)
root.order.add_edge(modular_design_process, nutrient_mix_process)
root.order.add_edge(modular_design_process, automation_config_process)
root.order.add_edge(energy_integration_process, nutrient_mix_process)
root.order.add_edge(energy_integration_process, automation_config_process)
root.order.add_edge(nutrient_mix_process, growth_monitoring_process)
root.order.add_edge(automation_config_process, growth_monitoring_process)
root.order.add_edge(growth_monitoring_process, community_meet_process)
root.order.add_edge(community_meet_process, feedback_loop_process)

# Print the root POWL model
print(root)
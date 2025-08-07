import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey     = Transition(label='Site Survey')
regulation_check= Transition(label='Regulation Check')
modular_design  = Transition(label='Modular Design')
material_sourcing= Transition(label='Material Sourcing')
energy_integration= Transition(label='Energy Integration')
climate_setup   = Transition(label='Climate Setup')
automation_config= Transition(label='Automation Config')
crop_seeding    = Transition(label='Crop Seeding')
system_assembly = Transition(label='System Assembly')
nutrient_mix    = Transition(label='Nutrient Mix')
growth_monitoring= Transition(label='Growth Monitoring')
waste_handling  = Transition(label='Waste Handling')
community_meet  = Transition(label='Community Meet')
data_analysis   = Transition(label='Data Analysis')
feedback_loop   = Transition(label='Feedback Loop')
yield_forecast  = Transition(label='Yield Forecast')

# Build the loop for continuous monitoring and feedback
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, feedback_loop])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    site_survey, regulation_check, modular_design, material_sourcing,
    energy_integration, climate_setup, automation_config, crop_seeding,
    system_assembly, nutrient_mix, monitoring_loop, waste_handling,
    community_meet, data_analysis, yield_forecast
])

# Define the sequence and concurrent dependencies
root.order.add_edge(site_survey,     regulation_check)
root.order.add_edge(regulation_check, modular_design)
root.order.add_edge(modular_design, material_sourcing)
root.order.add_edge(material_sourcing, energy_integration)
root.order.add_edge(energy_integration, climate_setup)
root.order.add_edge(climate_setup, automation_config)
root.order.add_edge(automation_config, crop_seeding)
root.order.add_edge(crop_seeding, system_assembly)
root.order.add_edge(system_assembly, nutrient_mix)
root.order.add_edge(nutrient_mix, monitoring_loop)
root.order.add_edge(monitoring_loop, waste_handling)
root.order.add_edge(waste_handling, community_meet)
root.order.add_edge(community_meet, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)

# The yield forecast can optionally occur after all other activities
# This is represented by a silent transition (tau label) as the exit condition
skip = SilentTransition()
root.order.add_edge(yield_forecast, skip)
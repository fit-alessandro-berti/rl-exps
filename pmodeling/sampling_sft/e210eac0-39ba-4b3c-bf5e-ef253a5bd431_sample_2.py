import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
regulation_check  = Transition(label='Regulation Check')
modular_design    = Transition(label='Modular Design')
material_sourcing = Transition(label='Material Sourcing')
energy_integration= Transition(label='Energy Integration')
climate_setup     = Transition(label='Climate Setup')
automation_config = Transition(label='Automation Config')
crop_seeding      = Transition(label='Crop Seeding')
system_assembly   = Transition(label='System Assembly')
data_analysis     = Transition(label='Data Analysis')
growth_monitoring = Transition(label='Growth Monitoring')
waste_handling    = Transition(label='Waste Handling')
community_meet    = Transition(label='Community Meet')
feedback_loop     = Transition(label='Feedback Loop')
yield_forecast    = Transition(label='Yield Forecast')

# Define the growth and monitoring loop: do Growth Monitoring, then optionally do Waste Handling and Feedback Loop, repeat until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, WasteHandlingLoop])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey, regulation_check, modular_design, material_sourcing,
    energy_integration, climate_setup, automation_config, crop_seeding,
    system_assembly, data_analysis, growth_loop, community_meet, feedback_loop, yield_forecast
])

# Sequential dependencies
root.order.add_edge(site_survey, regulation_check)
root.order.add_edge(regulation_check, modular_design)
root.order.add_edge(modular_design, material_sourcing)
root.order.add_edge(material_sourcing, energy_integration)
root.order.add_edge(energy_integration, climate_setup)
root.order.add_edge(climate_setup, automation_config)
root.order.add_edge(automation_config, crop_seeding)
root.order.add_edge(crop_seeding, system_assembly)

# Assemble and analyze after system assembly
root.order.add_edge(system_assembly, data_analysis)

# Growth monitoring and feedback loop after data analysis
root.order.add_edge(data_analysis, growth_loop)

# Community engagement after growth loop completes
root.order.add_edge(growth_loop, community_meet)

# Feedback loop can happen after community meet
root.order.add_edge(community_meet, feedback_loop)

# Yield forecast can happen after feedback loop
root.order.add_edge(feedback_loop, yield_forecast)
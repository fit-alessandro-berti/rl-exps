import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and exclusive choices
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, regulation_check])
modular_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_design, material_sourcing])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_integration, climate_setup])
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, system_assembly])
automation_loop = OperatorPOWL(operator=Operator.LOOP, children=[automation_config, crop_seeding])
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, waste_handling])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, data_analysis])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, yield_forecast])

# Define the root node with partial order
root = StrictPartialOrder(nodes=[
    site_loop, modular_loop, energy_loop, nutrient_loop, automation_loop, growth_loop,
    community_loop, feedback_loop, yield_forecast
])

# Define the order of execution
root.order.add_edge(site_loop, modular_loop)
root.order.add_edge(modular_loop, energy_loop)
root.order.add_edge(energy_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, automation_loop)
root.order.add_edge(automation_loop, growth_loop)
root.order.add_edge(growth_loop, community_loop)
root.order.add_edge(community_loop, feedback_loop)
root.order.add_edge(feedback_loop, yield_forecast)

print(root)
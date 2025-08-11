import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_seeding, growth_monitoring, waste_handling, community_meet, data_analysis, feedback_loop, yield_forecast])
xor = OperatorPOWL(operator=Operator.XOR, children=[modular_design, material_sourcing, energy_integration, climate_setup, nutrient_mix, system_assembly, automation_config])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)
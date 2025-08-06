import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
system_assembly = Transition(label='System Assembly')
sensor_install = Transition(label='Sensor Install')
nutrient_prep = Transition(label='Nutrient Prep')
water_testing = Transition(label='Water Testing')
climate_setup = Transition(label='Climate Setup')
data_integration = Transition(label='Data Integration')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
waste_sorting = Transition(label='Waste Sorting')
harvest_plan = Transition(label='Harvest Plan')
produce_pack = Transition(label='Produce Pack')
energy_audit = Transition(label='Energy Audit')
community_setup = Transition(label='Community Setup')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for system assembly and sensor install
system_choice = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, sensor_install])

# Define loop for nutrient preparation and water testing
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep, water_testing])

# Define exclusive choice for climate setup and data integration
climate_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, data_integration])

# Define exclusive choice for growth monitoring and pest control
monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_control])

# Define exclusive choice for waste sorting and harvest plan
waste_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, harvest_plan])

# Define exclusive choice for produce pack and energy audit
pack_choice = OperatorPOWL(operator=Operator.XOR, children=[produce_pack, energy_audit])

# Define exclusive choice for community setup and energy audit
community_choice = OperatorPOWL(operator=Operator.XOR, children=[community_setup, energy_audit])

# Define root partial order
root = StrictPartialOrder(nodes=[
    system_choice,
    nutrient_loop,
    climate_choice,
    monitor_choice,
    waste_choice,
    pack_choice,
    community_choice
])

# Add edges to the root partial order
root.order.add_edge(system_choice, climate_choice)
root.order.add_edge(nutrient_loop, climate_choice)
root.order.add_edge(climate_choice, monitor_choice)
root.order.add_edge(monitor_choice, waste_choice)
root.order.add_edge(waste_choice, pack_choice)
root.order.add_edge(pack_choice, community_choice)

# Print the root partial order
print(root)
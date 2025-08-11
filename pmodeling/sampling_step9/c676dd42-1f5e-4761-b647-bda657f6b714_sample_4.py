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

# Define exclusive choice for sensor install
sensor_install_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])

# Define loop for nutrient prep
nutrient_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep, water_testing])

# Define loop for climate setup
climate_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, data_integration])

# Define loop for growth monitoring
growth_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, pest_control])

# Define loop for waste sorting
waste_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting, energy_audit])

# Define loop for community setup
community_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_setup, harvest_plan])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    material_sourcing,
    system_assembly,
    sensor_install_choice,
    nutrient_prep_loop,
    climate_setup_loop,
    growth_monitoring_loop,
    waste_sorting_loop,
    community_setup_loop
])

# Define dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, system_assembly)
root.order.add_edge(system_assembly, sensor_install_choice)
root.order.add_edge(sensor_install_choice, nutrient_prep_loop)
root.order.add_edge(nutrient_prep_loop, climate_setup_loop)
root.order.add_edge(climate_setup_loop, growth_monitoring_loop)
root.order.add_edge(growth_monitoring_loop, waste_sorting_loop)
root.order.add_edge(waste_sorting_loop, community_setup_loop)

# Print the root model
print(root)
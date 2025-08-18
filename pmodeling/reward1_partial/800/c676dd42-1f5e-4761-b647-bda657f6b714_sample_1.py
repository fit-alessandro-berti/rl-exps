import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the transitions for the partial order
partial_order = StrictPartialOrder(nodes=[site_survey, design_layout, material_sourcing, system_assembly, sensor_install, nutrient_prep, water_testing, climate_setup, data_integration, growth_monitoring, pest_control, waste_sorting, harvest_plan, produce_pack, energy_audit, community_setup])

# Define the partial order dependencies
partial_order.order.add_edge(site_survey, design_layout)
partial_order.order.add_edge(design_layout, material_sourcing)
partial_order.order.add_edge(material_sourcing, system_assembly)
partial_order.order.add_edge(system_assembly, sensor_install)
partial_order.order.add_edge(sensor_install, nutrient_prep)
partial_order.order.add_edge(nutrient_prep, water_testing)
partial_order.order.add_edge(water_testing, climate_setup)
partial_order.order.add_edge(climate_setup, data_integration)
partial_order.order.add_edge(data_integration, growth_monitoring)
partial_order.order.add_edge(growth_monitoring, pest_control)
partial_order.order.add_edge(pest_control, waste_sorting)
partial_order.order.add_edge(waste_sorting, harvest_plan)
partial_order.order.add_edge(harvest_plan, produce_pack)
partial_order.order.add_edge(produce_pack, energy_audit)
partial_order.order.add_edge(energy_audit, community_setup)

# Save the result in the variable 'root'
root = partial_order
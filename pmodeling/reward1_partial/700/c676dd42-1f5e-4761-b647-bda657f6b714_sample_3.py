import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
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

# Create the partial order
root = StrictPartialOrder()

# Define the dependencies between activities
root.add_transition(site_survey)
root.add_transition(design_layout)
root.add_transition(material_sourcing)
root.add_transition(system_assembly)
root.add_transition(sensor_install)
root.add_transition(nutrient_prep)
root.add_transition(water_testing)
root.add_transition(climate_setup)
root.add_transition(data_integration)
root.add_transition(growth_monitoring)
root.add_transition(pest_control)
root.add_transition(waste_sorting)
root.add_transition(harvest_plan)
root.add_transition(produce_pack)
root.add_transition(energy_audit)
root.add_transition(community_setup)

# Define the partial order structure
root.add_edge(site_survey, design_layout)
root.add_edge(design_layout, material_sourcing)
root.add_edge(material_sourcing, system_assembly)
root.add_edge(system_assembly, sensor_install)
root.add_edge(sensor_install, nutrient_prep)
root.add_edge(nutrient_prep, water_testing)
root.add_edge(water_testing, climate_setup)
root.add_edge(climate_setup, data_integration)
root.add_edge(data_integration, growth_monitoring)
root.add_edge(growth_monitoring, pest_control)
root.add_edge(pest_control, waste_sorting)
root.add_edge(waste_sorting, harvest_plan)
root.add_edge(harvest_plan, produce_pack)
root.add_edge(produce_pack, energy_audit)
root.add_edge(energy_audit, community_setup)

# Print the root to see the partial order model
print(root)
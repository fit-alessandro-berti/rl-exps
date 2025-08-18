import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for system assembly
system_assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_assembly, material_sourcing])

# Define the XOR for nutrient prep and water testing
nutrient_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, water_testing])

# Define the XOR for climate setup and data integration
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, data_integration])

# Define the XOR for growth monitoring and pest control
growth_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_control])

# Define the XOR for waste sorting and produce pack
waste_sorting_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, produce_pack])

# Define the XOR for energy audit and community setup
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, community_setup])

# Define the root POWL model
root = StrictPartialOrder(nodes=[system_assembly_loop, nutrient_prep_xor, climate_setup_xor, growth_monitoring_xor, waste_sorting_xor, energy_audit_xor])
root.order.add_edge(system_assembly_loop, nutrient_prep_xor)
root.order.add_edge(nutrient_prep_xor, climate_setup_xor)
root.order.add_edge(climate_setup_xor, growth_monitoring_xor)
root.order.add_edge(growth_monitoring_xor, waste_sorting_xor)
root.order.add_edge(waste_sorting_xor, energy_audit_xor)

# Print the root POWL model
print(root)
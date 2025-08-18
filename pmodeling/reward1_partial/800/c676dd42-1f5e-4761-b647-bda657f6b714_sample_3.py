import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Survey -> Design Layout
site_survey_to_design_layout = OperatorPOWL(operator=Operator.SEQ, children=[site_survey, design_layout])

# Design Layout -> Material Sourcing
design_layout_to_material_sourcing = OperatorPOWL(operator=Operator.SEQ, children=[design_layout, material_sourcing])

# Material Sourcing -> System Assembly
material_sourcing_to_system_assembly = OperatorPOWL(operator=Operator.SEQ, children=[material_sourcing, system_assembly])

# System Assembly -> Sensor Install
system_assembly_to_sensor_install = OperatorPOWL(operator=Operator.SEQ, children=[system_assembly, sensor_install])

# Sensor Install -> Nutrient Prep
sensor_install_to_nutrient_prep = OperatorPOWL(operator=Operator.SEQ, children=[sensor_install, nutrient_prep])

# Nutrient Prep -> Water Testing
nutrient_prep_to_water_testing = OperatorPOWL(operator=Operator.SEQ, children=[nutrient_prep, water_testing])

# Water Testing -> Climate Setup
water_testing_to_climate_setup = OperatorPOWL(operator=Operator.SEQ, children=[water_testing, climate_setup])

# Climate Setup -> Data Integration
climate_setup_to_data_integration = OperatorPOWL(operator=Operator.SEQ, children=[climate_setup, data_integration])

# Data Integration -> Growth Monitoring
data_integration_to_growth_monitoring = OperatorPOWL(operator=Operator.SEQ, children=[data_integration, growth_monitoring])

# Growth Monitoring -> Pest Control
growth_monitoring_to_pest_control = OperatorPOWL(operator=Operator.SEQ, children=[growth_monitoring, pest_control])

# Pest Control -> Waste Sorting
pest_control_to_waste_sorting = OperatorPOWL(operator=Operator.SEQ, children=[pest_control, waste_sorting])

# Waste Sorting -> Harvest Plan
waste_sorting_to_harvest_plan = OperatorPOWL(operator=Operator.SEQ, children=[waste_sorting, harvest_plan])

# Harvest Plan -> Produce Pack
harvest_plan_to_produce_pack = OperatorPOWL(operator=Operator.SEQ, children=[harvest_plan, produce_pack])

# Produce Pack -> Energy Audit
produce_pack_to_energy_audit = OperatorPOWL(operator=Operator.SEQ, children=[produce_pack, energy_audit])

# Energy Audit -> Community Setup
energy_audit_to_community_setup = OperatorPOWL(operator=Operator.SEQ, children=[energy_audit, community_setup])

root = StrictPartialOrder(nodes=[site_survey, design_layout, material_sourcing, system_assembly, sensor_install, nutrient_prep, water_testing, climate_setup, data_integration, growth_monitoring, pest_control, waste_sorting, harvest_plan, produce_pack, energy_audit, community_setup])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, system_assembly)
root.order.add_edge(system_assembly, sensor_install)
root.order.add_edge(sensor_install, nutrient_prep)
root.order.add_edge(nutrient_prep, water_testing)
root.order.add_edge(water_testing, climate_setup)
root.order.add_edge(climate_setup, data_integration)
root.order.add_edge(data_integration, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_control)
root.order.add_edge(pest_control, waste_sorting)
root.order.add_edge(waste_sorting, harvest_plan)
root.order.add_edge(harvest_plan, produce_pack)
root.order.add_edge(produce_pack, energy_audit)
root.order.add_edge(energy_audit, community_setup)
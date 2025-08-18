import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
light_calibration = Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing = Transition(label='Waste Routing')
energy_audit = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach = Transition(label='Community Outreach')

skip = SilentTransition()

site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
design_layout_to_system_assembly = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
system_assembly_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, skip])
climate_setup_to_light_calibration = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
light_calibration_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[light_calibration, skip])
seed_selection_to_seedling_prep = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
seedling_prep_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seedling_prep, skip])
nutrient_mix_to_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
irrigation_setup_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])
sensor_install_to_data_integration = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
data_integration_to_waste_routing = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])
waste_routing_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[waste_routing, skip])
energy_audit_to_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
regulation_check_to_operational_test = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
operational_test_to_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[operational_test, skip])

root = StrictPartialOrder(nodes=[
    site_survey_to_design_layout,
    design_layout_to_system_assembly,
    system_assembly_to_climate_setup,
    climate_setup_to_light_calibration,
    light_calibration_to_seed_selection,
    seed_selection_to_seedling_prep,
    seedling_prep_to_nutrient_mix,
    nutrient_mix_to_irrigation_setup,
    irrigation_setup_to_sensor_install,
    sensor_install_to_data_integration,
    data_integration_to_waste_routing,
    waste_routing_to_energy_audit,
    energy_audit_to_regulation_check,
    regulation_check_to_operational_test,
    operational_test_to_community_outreach
])
root.order.add_edge(site_survey_to_design_layout, design_layout_to_system_assembly)
root.order.add_edge(design_layout_to_system_assembly, system_assembly_to_climate_setup)
root.order.add_edge(system_assembly_to_climate_setup, climate_setup_to_light_calibration)
root.order.add_edge(climate_setup_to_light_calibration, light_calibration_to_seed_selection)
root.order.add_edge(light_calibration_to_seed_selection, seed_selection_to_seedling_prep)
root.order.add_edge(seed_selection_to_seedling_prep, seedling_prep_to_nutrient_mix)
root.order.add_edge(seedling_prep_to_nutrient_mix, nutrient_mix_to_irrigation_setup)
root.order.add_edge(nutrient_mix_to_irrigation_setup, irrigation_setup_to_sensor_install)
root.order.add_edge(irrigation_setup_to_sensor_install, sensor_install_to_data_integration)
root.order.add_edge(sensor_install_to_data_integration, data_integration_to_waste_routing)
root.order.add_edge(data_integration_to_waste_routing, waste_routing_to_energy_audit)
root.order.add_edge(waste_routing_to_energy_audit, energy_audit_to_regulation_check)
root.order.add_edge(energy_audit_to_regulation_check, regulation_check_to_operational_test)
root.order.add_edge(regulation_check_to_operational_test, operational_test_to_community_outreach)
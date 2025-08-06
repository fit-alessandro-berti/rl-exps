from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
unit_assembly = Transition(label='Unit Assembly')
system_wiring = Transition(label='System Wiring')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_setup = Transition(label='Planting Setup')
climate_control = Transition(label='Climate Control')
pest_management = Transition(label='Pest Management')
data_calibration = Transition(label='Data Calibration')
yield_analysis = Transition(label='Yield Analysis')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
expansion_plan = Transition(label='Expansion Plan')

# Define the transitions
site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[design_layout, material_sourcing])
material_sourcing_to_unit_assembly = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, unit_assembly])
unit_assembly_to_system_wiring = OperatorPOWL(operator=Operator.XOR, children=[unit_assembly, system_wiring])
system_wiring_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[system_wiring, sensor_install])
sensor_install_to_water_testing = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])
water_testing_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[water_testing, nutrient_mix])
nutrient_mix_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_selection_to_planting_setup = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, planting_setup])
planting_setup_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, climate_control])
climate_control_to_pest_management = OperatorPOWL(operator=Operator.XOR, children=[climate_control, pest_management])
pest_management_to_data_calibration = OperatorPOWL(operator=Operator.XOR, children=[pest_management, data_calibration])
data_calibration_to_yield_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_calibration, yield_analysis])
yield_analysis_to_community_meet = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, community_meet])
community_meet_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[community_meet, compliance_check])
compliance_check_to_expansion_plan = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, expansion_plan])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey_to_design_layout,
    design_layout_to_material_sourcing,
    material_sourcing_to_unit_assembly,
    unit_assembly_to_system_wiring,
    system_wiring_to_sensor_install,
    sensor_install_to_water_testing,
    water_testing_to_nutrient_mix,
    nutrient_mix_to_seed_selection,
    seed_selection_to_planting_setup,
    planting_setup_to_climate_control,
    climate_control_to_pest_management,
    pest_management_to_data_calibration,
    data_calibration_to_yield_analysis,
    yield_analysis_to_community_meet,
    community_meet_to_compliance_check,
    compliance_check_to_expansion_plan
])
root.order.add_edge(site_survey_to_design_layout, design_layout_to_material_sourcing)
root.order.add_edge(design_layout_to_material_sourcing, material_sourcing_to_unit_assembly)
root.order.add_edge(material_sourcing_to_unit_assembly, unit_assembly_to_system_wiring)
root.order.add_edge(unit_assembly_to_system_wiring, system_wiring_to_sensor_install)
root.order.add_edge(system_wiring_to_sensor_install, sensor_install_to_water_testing)
root.order.add_edge(sensor_install_to_water_testing, water_testing_to_nutrient_mix)
root.order.add_edge(water_testing_to_nutrient_mix, nutrient_mix_to_seed_selection)
root.order.add_edge(nutrient_mix_to_seed_selection, seed_selection_to_planting_setup)
root.order.add_edge(seed_selection_to_planting_setup, planting_setup_to_climate_control)
root.order.add_edge(planting_setup_to_climate_control, climate_control_to_pest_management)
root.order.add_edge(climate_control_to_pest_management, pest_management_to_data_calibration)
root.order.add_edge(pest_management_to_data_calibration, data_calibration_to_yield_analysis)
root.order.add_edge(data_calibration_to_yield_analysis, yield_analysis_to_community_meet)
root.order.add_edge(yield_analysis_to_community_meet, community_meet_to_compliance_check)
root.order.add_edge(community_meet_to_compliance_check, compliance_check_to_expansion_plan)

print(root)
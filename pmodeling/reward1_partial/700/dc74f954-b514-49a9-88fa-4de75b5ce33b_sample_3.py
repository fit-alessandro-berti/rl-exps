import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_filing = Transition(label='Permit Filing')
module_build = Transition(label='Module Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
lighting_configure = Transition(label='Lighting Configure')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix = Transition(label='Nutrient Mix')
pest_check = Transition(label='Pest Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
data_integration = Transition(label='Data Integration')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
yield_analyze = Transition(label='Yield Analyze')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')

# Define the control flow operators
site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[design_layout, permit_filing])
permit_filing_to_module_build = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, module_build])
module_build_to_system_install = OperatorPOWL(operator=Operator.XOR, children=[module_build, system_install])
system_install_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[system_install, climate_setup])
climate_setup_to_lighting_configure = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, lighting_configure])
lighting_configure_to_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, irrigation_setup])
irrigation_setup_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, nutrient_mix])
nutrient_mix_to_pest_check = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_check])
pest_check_to_sensor_calibrate = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])
sensor_calibrate_to_data_integration = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibrate, data_integration])
data_integration_to_crop_planting = OperatorPOWL(operator=Operator.XOR, children=[data_integration, crop_planting])
crop_planting_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, growth_monitor])
growth_monitor_to_yield_analyze = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, yield_analyze])
yield_analyze_to_waste_manage = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, waste_manage])
waste_manage_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, energy_audit])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_filing, module_build, system_install, climate_setup,
    lighting_configure, irrigation_setup, nutrient_mix, pest_check, sensor_calibrate, data_integration,
    crop_planting, growth_monitor, yield_analyze, waste_manage, energy_audit
])

# Add the edges based on the control flow
root.order.add_edge(site_survey, design_layout_to_design_layout)
root.order.add_edge(design_layout, permit_filing_to_permit_filing)
root.order.add_edge(permit_filing, module_build_to_module_build)
root.order.add_edge(module_build, system_install_to_system_install)
root.order.add_edge(system_install, climate_setup_to_climate_setup)
root.order.add_edge(climate_setup, lighting_configure_to_lighting_configure)
root.order.add_edge(lighting_configure, irrigation_setup_to_irrigation_setup)
root.order.add_edge(irrigation_setup, nutrient_mix_to_nutrient_mix)
root.order.add_edge(nutrient_mix, pest_check_to_pest_check)
root.order.add_edge(pest_check, sensor_calibrate_to_sensor_calibrate)
root.order.add_edge(sensor_calibrate, data_integration_to_data_integration)
root.order.add_edge(data_integration, crop_planting_to_crop_planting)
root.order.add_edge(crop_planting, growth_monitor_to_growth_monitor)
root.order.add_edge(growth_monitor, yield_analyze_to_yield_analyze)
root.order.add_edge(yield_analyze, waste_manage_to_waste_manage)
root.order.add_edge(waste_manage, energy_audit_to_energy_audit)
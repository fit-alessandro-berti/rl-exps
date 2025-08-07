import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
permit_filing    = Transition(label='Permit Filing')
module_build     = Transition(label='Module Build')
system_install   = Transition(label='System Install')
climate_setup    = Transition(label='Climate Setup')
lighting_config  = Transition(label='Lighting Configure')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_calibrate = Transition(label='Sensor Calibrate')
data_integration = Transition(label='Data Integration')
crop_planting    = Transition(label='Crop Planting')
growth_monitor   = Transition(label='Growth Monitor')
yield_analyze    = Transition(label='Yield Analyze')
pest_check       = Transition(label='Pest Check')
waste_manage     = Transition(label='Waste Manage')
energy_audit     = Transition(label='Energy Audit')

# Loop for continuous growth monitoring and yield analysis
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, yield_analyze])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_filing, module_build,
    system_install, climate_setup, lighting_config,
    irrigation_setup, nutrient_mix, sensor_calibrate,
    data_integration, crop_planting, growth_loop,
    pest_check, waste_manage, energy_audit
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_filing)
root.order.add_edge(permit_filing, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(system_install, lighting_config)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(system_install, sensor_calibrate)
root.order.add_edge(climate_setup, data_integration)
root.order.add_edge(lighting_config, data_integration)
root.order.add_edge(irrigation_setup, data_integration)
root.order.add_edge(nutrient_mix, data_integration)
root.order.add_edge(sensor_calibrate, data_integration)
root.order.add_edge(data_integration, crop_planting)
root.order.add_edge(crop_planting, growth_loop)
root.order.add_edge(growth_loop, pest_check)
root.order.add_edge(pest_check, growth_loop)
root.order.add_edge(growth_loop, waste_manage)
root.order.add_edge(growth_loop, energy_audit)
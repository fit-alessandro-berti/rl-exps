import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
permit_filing     = Transition(label='Permit Filing')
module_build      = Transition(label='Module Build')
system_install    = Transition(label='System Install')
climate_setup     = Transition(label='Climate Setup')
lighting_configure= Transition(label='Lighting Configure')
irrigation_setup  = Transition(label='Irrigation Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_check        = Transition(label='Pest Check')
sensor_calibrate  = Transition(label='Sensor Calibrate')
data_integration  = Transition(label='Data Integration')
crop_planting     = Transition(label='Crop Planting')
growth_monitor    = Transition(label='Growth Monitor')
yield_analyze     = Transition(label='Yield Analyze')
waste_manage      = Transition(label='Waste Manage')
energy_audit      = Transition(label='Energy Audit')

# Loop for continuous monitoring and analysis
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, yield_analyze]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_filing,
    module_build,
    system_install,
    climate_setup,
    lighting_configure,
    irrigation_setup,
    nutrient_mix,
    pest_check,
    sensor_calibrate,
    data_integration,
    crop_planting,
    monitor_loop,
    waste_manage,
    energy_audit
])

# Sequence: Site Survey -> Design Layout -> Permit Filing -> Module Build -> System Install
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_filing)
root.order.add_edge(permit_filing, module_build)
root.order.add_edge(module_build, system_install)

# Parallel: Climate Setup, Lighting Configure, Irrigation Setup, Nutrient Mix
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(system_install, lighting_configure)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, nutrient_mix)

# Sequential pest check after mixing nutrients
root.order.add_edge(nutrient_mix, pest_check)

# Parallel: Sensor Calibration, Data Integration
root.order.add_edge(climate_setup, sensor_calibrate)
root.order.add_edge(climate_setup, data_integration)
root.order.add_edge(lighting_configure, sensor_calibrate)
root.order.add_edge(lighting_configure, data_integration)
root.order.add_edge(irrigation_setup, sensor_calibrate)
root.order.add_edge(irrigation_setup, data_integration)

# After sensor/data integration, start planting and monitoring
root.order.add_edge(data_integration, crop_planting)
root.order.add_edge(data_integration, monitor_loop)

# After crop planting, perform waste management and energy audit
root.order.add_edge(crop_planting, waste_manage)
root.order.add_edge(crop_planting, energy_audit)
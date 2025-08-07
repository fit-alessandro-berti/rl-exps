import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the growth cycle partial order (concurrent after planting)
growth_cycle = StrictPartialOrder(nodes=[
    growth_monitor,
    yield_analyze,
    waste_manage,
    energy_audit
])
# No order edges, all are concurrent

# Define the monitoring loop: after growth_monitor, optionally do yield_analyze, waste_manage, energy_audit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_integration]
)

# Build the top-level partial order
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
    crop_planting,
    monitor_loop,
    growth_cycle
])

# Add the control-flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_filing)
root.order.add_edge(permit_filing, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(system_install, lighting_configure)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(climate_setup, pest_check)
root.order.add_edge(lighting_configure, nutrient_mix)
root.order.add_edge(lighting_configure, pest_check)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(irrigation_setup, pest_check)
root.order.add_edge(nutrient_mix, sensor_calibrate)
root.order.add_edge(pest_check, sensor_calibrate)
root.order.add_edge(sensor_calibrate, crop_planting)
root.order.add_edge(crop_planting, monitor_loop)
root.order.add_edge(crop_planting, growth_cycle)
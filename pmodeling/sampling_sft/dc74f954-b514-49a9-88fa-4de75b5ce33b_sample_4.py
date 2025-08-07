import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
permit_filing  = Transition(label='Permit Filing')
module_build   = Transition(label='Module Build')
system_install = Transition(label='System Install')
climate_setup  = Transition(label='Climate Setup')
lighting_conf  = Transition(label='Lighting Configure')
irrigation_set = Transition(label='Irrigation Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
pest_check     = Transition(label='Pest Check')
sensor_cal     = Transition(label='Sensor Calibrate')
data_integrate = Transition(label='Data Integration')
crop_planting  = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
yield_analyze  = Transition(label='Yield Analyze')
waste_manage   = Transition(label='Waste Manage')
energy_audit   = Transition(label='Energy Audit')

# Define the loop for continuous monitoring and analysis
# A = monitoring + analysis
monitoring = StrictPartialOrder(nodes=[growth_monitor, yield_analyze])
monitoring.order.add_edge(growth_monitor, yield_analyze)

# B = waste management + energy audit
waste_energy = StrictPartialOrder(nodes=[waste_manage, energy_audit])
waste_energy.order.add_edge(waste_manage, energy_audit)

# LOOP(children=[A, B]) means: do A, then either exit or do B then A again...
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, waste_energy])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_filing,
    module_build, system_install,
    climate_setup, lighting_conf, irrigation_set, nutrient_mix,
    pest_check, sensor_cal, data_integrate,
    crop_planting,
    monitor_loop
])

# Sequence of activities before the monitoring loop
root.order.add_edge(site_survey,     design_layout)
root.order.add_edge(design_layout,   permit_filing)
root.order.add_edge(permit_filing,   module_build)
root.order.add_edge(module_build,    system_install)
root.order.add_edge(system_install,  climate_setup)
root.order.add_edge(climate_setup,   lighting_conf)
root.order.add_edge(lighting_conf,   irrigation_set)
root.order.add_edge(irrigation_set,  nutrient_mix)
root.order.add_edge(nutrient_mix,    pest_check)
root.order.add_edge(pest_check,      sensor_cal)
root.order.add_edge(sensor_cal,      data_integrate)
root.order.add_edge(data_integrate,  crop_planting)

# After planting, start the monitoring loop
root.order.add_edge(crop_planting, monitor_loop)
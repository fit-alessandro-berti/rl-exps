import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess    = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_test      = Transition(label='Soil Test')
climate_eval   = Transition(label='Climate Eval')
permit_obtain  = Transition(label='Permit Obtain')
design_layout  = Transition(label='Design Layout')
seed_sourcing  = Transition(label='Seed Sourcing')
irrigation_set = Transition(label='Irrigation Set')
nutrient_mix   = Transition(label='Nutrient Mix')
pest_control   = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train    = Transition(label='Staff Train')
crop_planting  = Transition(label='Crop Planting')
yield_monitor  = Transition(label='Yield Monitor')
market_setup   = Transition(label='Market Setup')
maintenance    = Transition(label='Maintenance')
waste_manage   = Transition(label='Waste Manage')

# Define the main growing cycle as a partial order
growing_cycle = StrictPartialOrder(nodes=[
    irrigation_set, nutrient_mix, pest_control, sensor_install,
    crop_planting, yield_monitor, market_setup
])
# Define the order dependencies within the cycle
growing_cycle.order.add_edge(irrigation_set, nutrient_mix)
growing_cycle.order.add_edge(nutrient_mix, pest_control)
growing_cycle.order.add_edge(pest_control, sensor_install)
growing_cycle.order.add_edge(sensor_install, crop_planting)
growing_cycle.order.add_edge(crop_planting, yield_monitor)
growing_cycle.order.add_edge(yield_monitor, market_setup)

# Define the adaptive maintenance loop: perform maintenance, then optionally repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance, waste_manage]
)

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_check, soil_test, climate_eval,
    permit_obtain, design_layout, seed_sourcing, growing_cycle,
    maintenance_loop
])
# Add the initial dependencies
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(site_assess, soil_test)
root.order.add_edge(site_assess, climate_eval)
root.order.add_edge(structure_check, permit_obtain)
root.order.add_edge(soil_test, permit_obtain)
root.order.add_edge(climate_eval, permit_obtain)
root.order.add_edge(permit_obtain, design_layout)
root.order.add_edge(design_layout, seed_sourcing)
# Add the growing cycle after design layout
root.order.add_edge(design_layout, growing_cycle)
# Add the maintenance loop after the growing cycle
root.order.add_edge(growing_cycle, maintenance_loop)
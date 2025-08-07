import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_assess       = Transition(label='Site Assess')
structure_check   = Transition(label='Structure Check')
soil_test         = Transition(label='Soil Test')
climate_eval      = Transition(label='Climate Eval')
permit_obtain     = Transition(label='Permit Obtain')
design_layout     = Transition(label='Design Layout')
seed_sourcing     = Transition(label='Seed Sourcing')
irrigation_set    = Transition(label='Irrigation Set')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_control      = Transition(label='Pest Control')
sensor_install    = Transition(label='Sensor Install')
staff_train       = Transition(label='Staff Train')
crop_planting     = Transition(label='Crop Planting')
yield_monitor     = Transition(label='Yield Monitor')
market_setup      = Transition(label='Market Setup')
maintenance       = Transition(label='Maintenance')
waste_manage      = Transition(label='Waste Manage')

# Create a partial‐order workflow where all activities are concurrent at the start
root = StrictPartialOrder(nodes=[
    site_assess,
    structure_check,
    soil_test,
    climate_eval,
    permit_obtain,
    design_layout,
    seed_sourcing,
    irrigation_set,
    nutrient_mix,
    pest_control,
    sensor_install,
    staff_train,
    crop_planting
])

# Define the monitoring‐loop: do yield_monitor, then either exit or do maintenance and waste_manage then yield_monitor again
monitor_body = yield_monitor
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, maintenance])

# Add the full sequence of activities to the partial‐order
root.order.add_edge(site_assess, permit_obtain)
root.order.add_edge(permit_obtain, design_layout)
root.order.add_edge(design_layout, seed_sourcing)
root.order.add_edge(seed_sourcing, irrigation_set)
root.order.add_edge(irrigation_set, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(pest_control, sensor_install)
root.order.add_edge(sensor_install, staff_train)
root.order.add_edge(staff_train, crop_planting)
root.order.add_edge(crop_planting, monitor_loop)
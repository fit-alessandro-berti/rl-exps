import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the basic activities
seed_select      = Transition(label='Seed Select')
germinate        = Transition(label='Germinate Seeds')
transplant       = Transition(label='Transplant Seedlings')
mix_nutrients    = Transition(label='Mix Nutrients')
adjust_pH        = Transition(label='Adjust pH')
monitor_climate  = Transition(label='Monitor Climate')
control_humidity = Transition(label='Control Humidity')
co2_regulation   = Transition(label='CO2 Regulation')
detect_pests     = Transition(label='Detect Pests')
deploy_biocontrols = Transition(label='Deploy Biocontrols')
schedule_harvest = Transition(label='Schedule Harvest')
automate_picking = Transition(label='Automate Picking')
package_produce  = Transition(label='Package Produce')
compost_waste    = Transition(label='Compost Waste')
recycle_water    = Transition(label='Recycle Water')
data_logging     = Transition(label='Data Logging')
system_maintenance = Transition(label='System Maintenance')

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    germinate,
    transplant,
    mix_nutrients,
    adjust_pH,
    monitor_climate,
    control_humidity,
    co2_regulation,
    detect_pests,
    deploy_biocontrols,
    schedule_harvest,
    automate_picking,
    package_produce,
    compost_waste,
    recycle_water,
    data_logging,
    system_maintenance
])

# Define the control-flow dependencies
root.order.add_edge(seed_select, germinate)
root.order.add_edge(germinate, transplant)
root.order.add_edge(transplant, mix_nutrients)
root.order.add_edge(mix_nutrients, adjust_pH)
root.order.add_edge(adjust_pH, monitor_climate)
root.order.add_edge(monitor_climate, control_humidity)
root.order.add_edge(control_humidity, co2_regulation)
root.order.add_edge(co2_regulation, detect_pests)
root.order.add_edge(detect_pests, deploy_biocontrols)
root.order.add_edge(deploy_biocontrols, schedule_harvest)
root.order.add_edge(schedule_harvest, automate_picking)
root.order.add_edge(automate_picking, package_produce)
root.order.add_edge(package_produce, compost_waste)
root.order.add_edge(compost_waste, recycle_water)
root.order.add_edge(recycle_water, data_logging)
root.order.add_edge(data_logging, system_maintenance)
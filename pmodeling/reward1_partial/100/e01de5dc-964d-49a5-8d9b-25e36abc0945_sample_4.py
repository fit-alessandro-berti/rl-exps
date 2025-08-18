import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
transplant_seedlings = Transition(label='Transplant Seedlings')
mix_nutrients = Transition(label='Mix Nutrients')
adjust_pH = Transition(label='Adjust pH')
monitor_climate = Transition(label='Monitor Climate')
control_humidity = Transition(label='Control Humidity')
co2_regulation = Transition(label='CO2 Regulation')
detect_pests = Transition(label='Detect Pests')
deploy_biocontrols = Transition(label='Deploy Biocontrols')
schedule_harvest = Transition(label='Schedule Harvest')
automate_picking = Transition(label='Automate Picking')
package_produce = Transition(label='Package Produce')
compost_waste = Transition(label='Compost Waste')
recycle_water = Transition(label='Recycle Water')
data_logging = Transition(label='Data Logging')
system_maintenance = Transition(label='System Maintenance')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define loops and choices in the process
loop_seedling_management = OperatorPOWL(operator=Operator.LOOP, children=[mix_nutrients, adjust_pH, monitor_climate, control_humidity, co2_regulation, detect_pests, deploy_biocontrols])
xor_harvest_and_picking = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, automate_picking])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[seed_select, germinate_seeds, transplant_seedlings, loop_seedling_management, xor_harvest_and_picking, package_produce, compost_waste, recycle_water, data_logging, system_maintenance])
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, transplant_seedlings)
root.order.add_edge(transplant_seedlings, loop_seedling_management)
root.order.add_edge(loop_seedling_management, xor_harvest_and_picking)
root.order.add_edge(xor_harvest_and_picking, package_produce)
root.order.add_edge(xor_harvest_and_picking, compost_waste)
root.order.add_edge(compost_waste, recycle_water)
root.order.add_edge(recycle_water, data_logging)
root.order.add_edge(data_logging, system_maintenance)
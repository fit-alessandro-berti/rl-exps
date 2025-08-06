import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_climate, control_humidity, co2_regulation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[detect_pests, deploy_biocontrols])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, automate_picking])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[package_produce, compost_waste])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[recycle_water, data_logging])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[seed_select, germinate_seeds, transplant_seedlings, mix_nutrients, adjust_pH, loop1, loop2, xor1, xor2, xor3, xor4])
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, transplant_seedlings)
root.order.add_edge(transplant_seedlings, mix_nutrients)
root.order.add_edge(mix_nutrients, adjust_pH)
root.order.add_edge(adjust_pH, loop1)
root.order.add_edge(loop1, monitor_climate)
root.order.add_edge(monitor_climate, control_humidity)
root.order.add_edge(control_humidity, co2_regulation)
root.order.add_edge(co2_regulation, loop1)
root.order.add_edge(loop1, detect_pests)
root.order.add_edge(detect_pests, deploy_biocontrols)
root.order.add_edge(deploy_biocontrols, loop2)
root.order.add_edge(loop2, schedule_harvest)
root.order.add_edge(schedule_harvest, automate_picking)
root.order.add_edge(automate_picking, xor1)
root.order.add_edge(xor1, package_produce)
root.order.add_edge(package_produce, xor2)
root.order.add_edge(xor2, compost_waste)
root.order.add_edge(compost_waste, xor3)
root.order.add_edge(xor3, recycle_water)
root.order.add_edge(recycle_water, xor4)
root.order.add_edge(xor4, data_logging)
root.order.add_edge(data_logging, system_maintenance)
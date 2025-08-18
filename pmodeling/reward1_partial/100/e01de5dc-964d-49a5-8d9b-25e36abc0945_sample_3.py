import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
transplant_seedlings = Transition(label='Transplant Seedlings')
mix_nutrients = Transition(label='Mix Nutrients')
adjust_pH = Transition(label='Adjust pH')
monitor_climate = Transition(label='Monitor Climate')
control_humidity = Transition(label='Control Humidity')
CO2_regulation = Transition(label='CO2 Regulation')
detect_pests = Transition(label='Detect Pests')
deploy_biocontrols = Transition(label='Deploy Biocontrols')
schedule_harvest = Transition(label='Schedule Harvest')
automate_picking = Transition(label='Automate Picking')
package_produce = Transition(label='Package Produce')
compost_waste = Transition(label='Compost Waste')
recycle_water = Transition(label='Recycle Water')
data_logging = Transition(label='Data Logging')
system_maintenance = Transition(label='System Maintenance')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[detect_pests, deploy_biocontrols])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, automate_picking])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[package_produce, compost_waste])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[recycle_water, data_logging])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance, None])

# Define the POWL model
root = StrictPartialOrder(nodes=[seed_select, germinate_seeds, transplant_seedlings, mix_nutrients, adjust_pH, monitor_climate, control_humidity, CO2_regulation, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, transplant_seedlings)
root.order.add_edge(transplant_seedlings, mix_nutrients)
root.order.add_edge(mix_nutrients, adjust_pH)
root.order.add_edge(adjust_pH, monitor_climate)
root.order.add_edge(monitor_climate, control_humidity)
root.order.add_edge(control_humidity, CO2_regulation)
root.order.add_edge(CO2_regulation, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, system_maintenance)

print(root)
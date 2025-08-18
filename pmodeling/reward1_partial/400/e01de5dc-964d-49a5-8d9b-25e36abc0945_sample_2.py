import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[detect_pests, deploy_biocontrols])
xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[automate_picking, package_produce])
xor_loop2 = OperatorPOWL(operator=Operator.LOOP, children=[compost_waste, recycle_water])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    seed_select, germinate_seeds, transplant_seedlings, mix_nutrients, adjust_pH, 
    monitor_climate, control_humidity, co2_regulation, xor, xor_loop, xor_loop2,
    data_logging, system_maintenance
])

# Add edges to the root model
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, transplant_seedlings)
root.order.add_edge(transplant_seedlings, mix_nutrients)
root.order.add_edge(mix_nutrients, adjust_pH)
root.order.add_edge(adjust_pH, monitor_climate)
root.order.add_edge(monitor_climate, control_humidity)
root.order.add_edge(control_humidity, co2_regulation)
root.order.add_edge(co2_regulation, xor)
root.order.add_edge(xor, xor_loop)
root.order.add_edge(xor, xor_loop2)
root.order.add_edge(xor_loop, data_logging)
root.order.add_edge(xor_loop2, system_maintenance)

print(root)
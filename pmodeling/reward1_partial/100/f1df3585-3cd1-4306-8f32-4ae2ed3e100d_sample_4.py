import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_assess = Transition(label='Site Assess')
plan_layout = Transition(label='Plan Layout')
install_racks = Transition(label='Install Racks')
mix_nutrients = Transition(label='Mix Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
setup_lighting = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
select_seeds = Transition(label='Select Seeds')
monitor_germinate = Transition(label='Monitor Germinate')
apply_bio_controls = Transition(label='Apply Bio-controls')
maintain_systems = Transition(label='Maintain Systems')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
quality_check = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[select_seeds, monitor_germinate, analyze_data])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[apply_bio_controls, maintain_systems])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip1, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip2, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip3, skip4])

root = StrictPartialOrder(nodes=[site_assess, plan_layout, install_racks, mix_nutrients, calibrate_sensors, setup_lighting, configure_climate, xor1, xor2, xor3, harvest_crops, quality_check, package_produce, distribute_goods])
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(plan_layout, install_racks)
root.order.add_edge(install_racks, mix_nutrients)
root.order.add_edge(mix_nutrients, calibrate_sensors)
root.order.add_edge(calibrate_sensors, setup_lighting)
root.order.add_edge(setup_lighting, configure_climate)
root.order.add_edge(configure_climate, xor1)
root.order.add_edge(configure_climate, xor2)
root.order.add_edge(xor1, harvest_crops)
root.order.add_edge(xor1, quality_check)
root.order.add_edge(xor1, package_produce)
root.order.add_edge(xor1, distribute_goods)
root.order.add_edge(xor2, harvest_crops)
root.order.add_edge(xor2, quality_check)
root.order.add_edge(xor2, package_produce)
root.order.add_edge(xor2, distribute_goods)

print(root)
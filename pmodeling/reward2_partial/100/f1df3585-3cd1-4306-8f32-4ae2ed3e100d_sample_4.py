from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_assess, plan_layout, install_racks, mix_nutrients, calibrate_sensors, setup_lighting, configure_climate, select_seeds, monitor_germinate, apply_bio_controls, maintain_systems, analyze_data, harvest_crops, quality_check, package_produce, distribute_goods])

# Define the dependencies
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(plan_layout, install_racks)
root.order.add_edge(install_racks, mix_nutrients)
root.order.add_edge(mix_nutrients, calibrate_sensors)
root.order.add_edge(calibrate_sensors, setup_lighting)
root.order.add_edge(setup_lighting, configure_climate)
root.order.add_edge(configure_climate, select_seeds)
root.order.add_edge(select_seeds, monitor_germinate)
root.order.add_edge(monitor_germinate, apply_bio_controls)
root.order.add_edge(apply_bio_controls, maintain_systems)
root.order.add_edge(maintain_systems, analyze_data)
root.order.add_edge(analyze_data, harvest_crops)
root.order.add_edge(harvest_crops, quality_check)
root.order.add_edge(quality_check, package_produce)
root.order.add_edge(package_produce, distribute_goods)

print(root)
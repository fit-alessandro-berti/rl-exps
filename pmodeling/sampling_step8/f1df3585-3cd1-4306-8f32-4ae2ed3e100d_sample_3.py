import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for concurrent activities
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_assess, plan_layout, install_racks, mix_nutrients, calibrate_sensors,
    setup_lighting, configure_climate, select_seeds, monitor_germinate, apply_bio_controls,
    maintain_systems, analyze_data, harvest_crops, quality_check, package_produce, distribute_goods
])

# Define the dependencies
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(site_assess, install_racks)
root.order.add_edge(site_assess, mix_nutrients)
root.order.add_edge(site_assess, calibrate_sensors)
root.order.add_edge(site_assess, setup_lighting)
root.order.add_edge(site_assess, configure_climate)
root.order.add_edge(site_assess, select_seeds)
root.order.add_edge(site_assess, monitor_germinate)
root.order.add_edge(site_assess, apply_bio_controls)
root.order.add_edge(site_assess, maintain_systems)
root.order.add_edge(site_assess, analyze_data)
root.order.add_edge(site_assess, harvest_crops)
root.order.add_edge(site_assess, quality_check)
root.order.add_edge(site_assess, package_produce)
root.order.add_edge(site_assess, distribute_goods)

# The final result is stored in the 'root' variable
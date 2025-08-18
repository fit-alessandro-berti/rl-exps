import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define concurrent activities
concurrent_activities = [mix_nutrients, calibrate_sensors, setup_lighting, configure_climate, select_seeds, monitor_germinate]

# Define loop for pest management and system maintenance
pest_management_loop = OperatorPOWL(operator=Operator.LOOP, children=[apply_bio_controls, maintain_systems])
pest_management_loop.order.add_edge(apply_bio_controls, maintain_systems)

# Define partial order
root = StrictPartialOrder(nodes=[site_assess, plan_layout, install_racks, concurrent_activities, pest_management_loop, analyze_data, harvest_crops, quality_check, package_produce, distribute_goods])
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(site_assess, install_racks)
root.order.add_edge(plan_layout, install_racks)
root.order.add_edge(install_racks, concurrent_activities)
root.order.add_edge(concurrent_activities, pest_management_loop)
root.order.add_edge(pest_management_loop, analyze_data)
root.order.add_edge(analyze_data, harvest_crops)
root.order.add_edge(harvest_crops, quality_check)
root.order.add_edge(quality_check, package_produce)
root.order.add_edge(package_produce, distribute_goods)
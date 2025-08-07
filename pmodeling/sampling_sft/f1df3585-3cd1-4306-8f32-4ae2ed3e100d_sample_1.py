import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess      = Transition(label='Site Assess')
plan_layout      = Transition(label='Plan Layout')
install_racks    = Transition(label='Install Racks')
select_seeds     = Transition(label='Select Seeds')
monitor_germinate= Transition(label='Monitor Germinate')
harvest_crops    = Transition(label='Harvest Crops')
quality_check    = Transition(label='Quality Check')
package_produce  = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define nutrient and sensor sub-processes as partial orders
nutrient_mix = StrictPartialOrder(nodes=[site_assess, plan_layout, install_racks])
nutrient_mix.order.add_edge(site_assess, plan_layout)
nutrient_mix.order.add_edge(plan_layout, install_racks)

sensor_calib = StrictPartialOrder(nodes=[site_assess, plan_layout])
sensor_calib.order.add_edge(site_assess, plan_layout)

# Define lighting and climate sub-processes as partial orders
lighting_setup = StrictPartialOrder(nodes=[site_assess, plan_layout])
lighting_setup.order.add_edge(site_assess, plan_layout)

climate_config = StrictPartialOrder(nodes=[site_assess, plan_layout])
climate_config.order.add_edge(site_assess, plan_layout)

# Define maintenance loop: Maintain Systems, then optionally repeat
maintain_loop = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Maintain Systems'), SilentTransition()])

# Define bio-controls application as a choice between application and skip
bio_choice = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Apply Bio-controls'), SilentTransition()])

# Define the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_assess, plan_layout, install_racks,
    select_seeds, monitor_germinate, harvest_crops,
    quality_check, package_produce, distribute_goods,
    nutrient_mix, sensor_calib,
    lighting_setup, climate_config,
    maintain_loop, bio_choice
])

# Add ordering edges
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(site_assess, install_racks)
root.order.add_edge(site_assess, select_seeds)
root.order.add_edge(site_assess, maintain_loop)
root.order.add_edge(site_assess, bio_choice)

root.order.add_edge(plan_layout, install_racks)
root.order.add_edge(plan_layout, select_seeds)
root.order.add_edge(plan_layout, maintain_loop)
root.order.add_edge(plan_layout, bio_choice)

root.order.add_edge(install_racks, monitor_germinate)
root.order.add_edge(select_seeds, monitor_germinate)

root.order.add_edge(monitor_germinate, harvest_crops)
root.order.add_edge(monitor_germinate, maintain_loop)
root.order.add_edge(monitor_germinate, bio_choice)

root.order.add_edge(harvest_crops, quality_check)
root.order.add_edge(harvest_crops, maintain_loop)
root.order.add_edge(harvest_crops, bio_choice)

root.order.add_edge(quality_check, package_produce)
root.order.add_edge(quality_check, maintain_loop)
root.order.add_edge(quality_check, bio_choice)

root.order.add_edge(package_produce, distribute_goods)
root.order.add_edge(distribute_goods, maintain_loop)
root.order.add_edge(distribute_goods, bio_choice)

# Nutrient and sensor sub-processes can be executed in parallel
root.order.add_edge(nutrient_mix, monitor_germinate)
root.order.add_edge(sensor_calib, monitor_germinate)

# Lighting and climate sub-processes can be executed in parallel
root.order.add_edge(lighting_setup, monitor_germinate)
root.order.add_edge(climate_config, monitor_germinate)

# Maintain loop and bio-choice can be executed in parallel
root.order.add_edge(maintain_loop, harvest_crops)
root.order.add_edge(maintain_loop, quality_check)
root.order.add_edge(maintain_loop, package_produce)
root.order.add_edge(maintain_loop, distribute_goods)

root.order.add_edge(bio_choice, harvest_crops)
root.order.add_edge(bio_choice, quality_check)
root.order.add_edge(bio_choice, package_produce)
root.order.add_edge(bio_choice, distribute_goods)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess = Transition(label='Site Assess')
plan_layout = Transition(label='Plan Layout')
install_racks = Transition(label='Install Racks')
mix_nutrients = Transition(label='Mix Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
setup_lighting = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
select_seeds = Transition(label='Select Seeds')
monitor_germinate = Transition(label='Monitor Germinate')
apply_biocontrols = Transition(label='Apply Bio-controls')
maintain_systems = Transition(label='Maintain Systems')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
quality_check = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define silent transitions
skip_site_assess = SilentTransition()
skip_plan_layout = SilentTransition()
skip_install_racks = SilentTransition()
skip_mix_nutrients = SilentTransition()
skip_calibrate_sensors = SilentTransition()
skip_setup_lighting = SilentTransition()
skip_configure_climate = SilentTransition()
skip_select_seeds = SilentTransition()
skip_monitor_germinate = SilentTransition()
skip_apply_biocontrols = SilentTransition()
skip_maintain_systems = SilentTransition()
skip_analyze_data = SilentTransition()
skip_harvest_crops = SilentTransition()
skip_quality_check = SilentTransition()
skip_package_produce = SilentTransition()
skip_distribute_goods = SilentTransition()

# Define XOR choices
xor_site_assess = OperatorPOWL(operator=Operator.XOR, children=[skip_site_assess, site_assess])
xor_plan_layout = OperatorPOWL(operator=Operator.XOR, children=[skip_plan_layout, plan_layout])
xor_install_racks = OperatorPOWL(operator=Operator.XOR, children=[skip_install_racks, install_racks])
xor_mix_nutrients = OperatorPOWL(operator=Operator.XOR, children=[skip_mix_nutrients, mix_nutrients])
xor_calibrate_sensors = OperatorPOWL(operator=Operator.XOR, children=[skip_calibrate_sensors, calibrate_sensors])
xor_setup_lighting = OperatorPOWL(operator=Operator.XOR, children=[skip_setup_lighting, setup_lighting])
xor_configure_climate = OperatorPOWL(operator=Operator.XOR, children=[skip_configure_climate, configure_climate])
xor_select_seeds = OperatorPOWL(operator=Operator.XOR, children=[skip_select_seeds, select_seeds])
xor_monitor_germinate = OperatorPOWL(operator=Operator.XOR, children=[skip_monitor_germinate, monitor_germinate])
xor_apply_biocontrols = OperatorPOWL(operator=Operator.XOR, children=[skip_apply_biocontrols, apply_biocontrols])
xor_maintain_systems = OperatorPOWL(operator=Operator.XOR, children=[skip_maintain_systems, maintain_systems])
xor_analyze_data = OperatorPOWL(operator=Operator.XOR, children=[skip_analyze_data, analyze_data])
xor_harvest_crops = OperatorPOWL(operator=Operator.XOR, children=[skip_harvest_crops, harvest_crops])
xor_quality_check = OperatorPOWL(operator=Operator.XOR, children=[skip_quality_check, quality_check])
xor_package_produce = OperatorPOWL(operator=Operator.XOR, children=[skip_package_produce, package_produce])
xor_distribute_goods = OperatorPOWL(operator=Operator.XOR, children=[skip_distribute_goods, distribute_goods])

# Define loops
loop_site_assess = OperatorPOWL(operator=Operator.LOOP, children=[xor_site_assess])
loop_plan_layout = OperatorPOWL(operator=Operator.LOOP, children=[xor_plan_layout])
loop_install_racks = OperatorPOWL(operator=Operator.LOOP, children=[xor_install_racks])
loop_mix_nutrients = OperatorPOWL(operator=Operator.LOOP, children=[xor_mix_nutrients])
loop_calibrate_sensors = OperatorPOWL(operator=Operator.LOOP, children=[xor_calibrate_sensors])
loop_setup_lighting = OperatorPOWL(operator=Operator.LOOP, children=[xor_setup_lighting])
loop_configure_climate = OperatorPOWL(operator=Operator.LOOP, children=[xor_configure_climate])
loop_select_seeds = OperatorPOWL(operator=Operator.LOOP, children=[xor_select_seeds])
loop_monitor_germinate = OperatorPOWL(operator=Operator.LOOP, children=[xor_monitor_germinate])
loop_apply_biocontrols = OperatorPOWL(operator=Operator.LOOP, children=[xor_apply_biocontrols])
loop_maintain_systems = OperatorPOWL(operator=Operator.LOOP, children=[xor_maintain_systems])
loop_analyze_data = OperatorPOWL(operator=Operator.LOOP, children=[xor_analyze_data])
loop_harvest_crops = OperatorPOWL(operator=Operator.LOOP, children=[xor_harvest_crops])
loop_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[xor_quality_check])
loop_package_produce = OperatorPOWL(operator=Operator.LOOP, children=[xor_package_produce])
loop_distribute_goods = OperatorPOWL(operator=Operator.LOOP, children=[xor_distribute_goods])

# Define partial order
root = StrictPartialOrder(nodes=[
    loop_site_assess,
    loop_plan_layout,
    loop_install_racks,
    loop_mix_nutrients,
    loop_calibrate_sensors,
    loop_setup_lighting,
    loop_configure_climate,
    loop_select_seeds,
    loop_monitor_germinate,
    loop_apply_biocontrols,
    loop_maintain_systems,
    loop_analyze_data,
    loop_harvest_crops,
    loop_quality_check,
    loop_package_produce,
    loop_distribute_goods
])

# Define dependencies
root.order.add_edge(loop_site_assess, loop_plan_layout)
root.order.add_edge(loop_plan_layout, loop_install_racks)
root.order.add_edge(loop_install_racks, loop_mix_nutrients)
root.order.add_edge(loop_mix_nutrients, loop_calibrate_sensors)
root.order.add_edge(loop_calibrate_sensors, loop_setup_lighting)
root.order.add_edge(loop_setup_lighting, loop_configure_climate)
root.order.add_edge(loop_configure_climate, loop_select_seeds)
root.order.add_edge(loop_select_seeds, loop_monitor_germinate)
root.order.add_edge(loop_monitor_germinate, loop_apply_biocontrols)
root.order.add_edge(loop_apply_biocontrols, loop_maintain_systems)
root.order.add_edge(loop_maintain_systems, loop_analyze_data)
root.order.add_edge(loop_analyze_data, loop_harvest_crops)
root.order.add_edge(loop_harvest_crops, loop_quality_check)
root.order.add_edge(loop_quality_check, loop_package_produce)
root.order.add_edge(loop_package_produce, loop_distribute_goods)

print(root)
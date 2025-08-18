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
apply_biocontrols = Transition(label='Apply Bio-controls')
maintain_systems = Transition(label='Maintain Systems')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
quality_check = Transition(label='Quality Check')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

skip = SilentTransition()

# Concurrent activities
concurrent_activities = OperatorPOWL(operator=Operator.XOR, children=[install_racks, mix_nutrients, calibrate_sensors, setup_lighting, configure_climate, select_seeds, monitor_germinate, apply_biocontrols, maintain_systems, analyze_data, harvest_crops, quality_check, package_produce, distribute_goods])

# Loop for pest management
pest_management_loop = OperatorPOWL(operator=Operator.LOOP, children=[apply_biocontrols])

root = StrictPartialOrder(nodes=[site_assess, plan_layout, concurrent_activities, pest_management_loop])
root.order.add_edge(site_assess, plan_layout)
root.order.add_edge(plan_layout, concurrent_activities)
root.order.add_edge(concurrent_activities, pest_management_loop)
root.order.add_edge(pest_management_loop, concurrent_activities)

print(root)
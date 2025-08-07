import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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
root = StrictPartialOrder(nodes=[
    site_assess,
    plan_layout,
    install_racks,
    mix_nutrients,
    calibrate_sensors,
    setup_lighting,
    configure_climate,
    select_seeds,
    monitor_germinate,
    apply_bio_controls,
    maintain_systems,
    analyze_data,
    harvest_crops,
    quality_check,
    package_produce,
    distribute_goods
])

# Add dependencies if necessary
# For example, if 'Site Assess' must be done before 'Plan Layout':
# root.order.add_edge(site_assess, plan_layout)

# If there are no dependencies, you can simply define 'root' as above
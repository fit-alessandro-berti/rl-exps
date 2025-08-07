import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_analysis       = Transition(label='Site Analysis')
structure_check     = Transition(label='Structure Check')
modify_layout       = Transition(label='Modify Layout')
install_hvac        = Transition(label='Install HVAC')
setup_hydroponics   = Transition(label='Setup Hydroponics')
prepare_nutrients   = Transition(label='Prepare Nutrients')
select_seeds        = Transition(label='Select Seeds')
automate_planting   = Transition(label='Automate Planting')
deploy_sensors      = Transition(label='Deploy Sensors')
pest_control        = Transition(label='Pest Control')
optimize_energy     = Transition(label='Optimize Energy')
recycle_water       = Transition(label='Recycle Water')
automate_harvest    = Transition(label='Automate Harvest')
package_crops       = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data        = Transition(label='Analyze Data')

# Define the loop for continuous monitoring and maintenance
# Body A: Pest Control -> Optimize Energy -> Recycle Water
body_a = StrictPartialOrder(nodes=[pest_control, optimize_energy, recycle_water])
body_a.order.add_edge(pest_control, optimize_energy)
body_a.order.add_edge(optimize_energy, recycle_water)

# Body B: Analyze Data -> Coordinate Delivery
body_b = StrictPartialOrder(nodes=[analyze_data, coordinate_delivery])
body_b.order.add_edge(analyze_data, coordinate_delivery)

# Loop: Deploy Sensors, then either exit or execute Body A and then Body B, repeated
loop = OperatorPOWL(operator=Operator.LOOP, children=[deploy_sensors, body_a, body_b])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structure_check, modify_layout,
    install_hvac, setup_hydroponics, prepare_nutrients,
    select_seeds, automate_planting, loop,
    package_crops, coordinate_delivery, analyze_data
])

# Add the control-flow edges
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, modify_layout)
root.order.add_edge(modify_layout, install_hvac)
root.order.add_edge(install_hvac, setup_hydroponics)
root.order.add_edge(setup_hydroponics, prepare_nutrients)
root.order.add_edge(prepare_nutrients, select_seeds)
root.order.add_edge(select_seeds, automate_planting)
root.order.add_edge(automate_planting, loop)
root.order.add_edge(loop, package_crops)
root.order.add_edge(loop, coordinate_delivery)
root.order.add_edge(loop, analyze_data)
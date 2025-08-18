import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
modify_layout = Transition(label='Modify Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
deploy_sensors = Transition(label='Deploy Sensors')
pest_control = Transition(label='Pest Control')
optimize_energy = Transition(label='Optimize Energy')
recycle_water = Transition(label='Recycle Water')
automate_harvest = Transition(label='Automate Harvest')
package_crops = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data = Transition(label='Analyze Data')

# Define silent transitions for empty labels
skip = SilentTransition()

# Define partial order nodes
site_analysis_node = OperatorPOWL(operator=Operator.NONE, children=[site_analysis])
structure_check_node = OperatorPOWL(operator=Operator.NONE, children=[structure_check])
modify_layout_node = OperatorPOWL(operator=Operator.NONE, children=[modify_layout])
install_hvac_node = OperatorPOWL(operator=Operator.NONE, children=[install_hvac])
setup_hydroponics_node = OperatorPOWL(operator=Operator.NONE, children=[setup_hydroponics])
prepare_nutrients_node = OperatorPOWL(operator=Operator.NONE, children=[prepare_nutrients])
select_seeds_node = OperatorPOWL(operator=Operator.NONE, children=[select_seeds])
automate_planting_node = OperatorPOWL(operator=Operator.NONE, children=[automate_planting])
deploy_sensors_node = OperatorPOWL(operator=Operator.NONE, children=[deploy_sensors])
pest_control_node = OperatorPOWL(operator=Operator.NONE, children=[pest_control])
optimize_energy_node = OperatorPOWL(operator=Operator.NONE, children=[optimize_energy])
recycle_water_node = OperatorPOWL(operator=Operator.NONE, children=[recycle_water])
automate_harvest_node = OperatorPOWL(operator=Operator.NONE, children=[automate_harvest])
package_crops_node = OperatorPOWL(operator=Operator.NONE, children=[package_crops])
coordinate_delivery_node = OperatorPOWL(operator=Operator.NONE, children=[coordinate_delivery])
analyze_data_node = OperatorPOWL(operator=Operator.NONE, children=[analyze_data])

# Define partial order graph
root = StrictPartialOrder(nodes=[
    site_analysis_node,
    structure_check_node,
    modify_layout_node,
    install_hvac_node,
    setup_hydroponics_node,
    prepare_nutrients_node,
    select_seeds_node,
    automate_planting_node,
    deploy_sensors_node,
    pest_control_node,
    optimize_energy_node,
    recycle_water_node,
    automate_harvest_node,
    package_crops_node,
    coordinate_delivery_node,
    analyze_data_node
])
root.order.add_edge(site_analysis_node, structure_check_node)
root.order.add_edge(structure_check_node, modify_layout_node)
root.order.add_edge(modify_layout_node, install_hvac_node)
root.order.add_edge(install_hvac_node, setup_hydroponics_node)
root.order.add_edge(setup_hydroponics_node, prepare_nutrients_node)
root.order.add_edge(prepare_nutrients_node, select_seeds_node)
root.order.add_edge(select_seeds_node, automate_planting_node)
root.order.add_edge(automate_planting_node, deploy_sensors_node)
root.order.add_edge(deploy_sensors_node, pest_control_node)
root.order.add_edge(pest_control_node, optimize_energy_node)
root.order.add_edge(optimize_energy_node, recycle_water_node)
root.order.add_edge(recycle_water_node, automate_harvest_node)
root.order.add_edge(automate_harvest_node, package_crops_node)
root.order.add_edge(package_crops_node, coordinate_delivery_node)
root.order.add_edge(coordinate_delivery_node, analyze_data_node)
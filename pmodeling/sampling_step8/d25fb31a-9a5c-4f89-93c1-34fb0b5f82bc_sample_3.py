from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Add activities
assess_structure = Transition(label='Assess Structure')
analyze_environment = Transition(label='Analyze Environment')
design_modules = Transition(label='Design Modules')
procure_materials = Transition(label='Procure Materials')
install_irrigation = Transition(label='Install Irrigation')
set_sensors = Transition(label='Set Sensors')
select_seeds = Transition(label='Select Seeds')
schedule_planting = Transition(label='Schedule Planting')
monitor_growth = Transition(label='Monitor Growth')
collect_data = Transition(label='Collect Data')
manage_pests = Transition(label='Manage Pests')
harvest_crops = Transition(label='Harvest Crops')
coordinate_sales = Transition(label='Coordinate Sales')
compost_waste = Transition(label='Compost Waste')
review_feedback = Transition(label='Review Feedback')

# Add edges to the POWL model
root.nodes.add(assess_structure)
root.nodes.add(analyze_environment)
root.nodes.add(design_modules)
root.nodes.add(procure_materials)
root.nodes.add(install_irrigation)
root.nodes.add(set_sensors)
root.nodes.add(select_seeds)
root.nodes.add(schedule_planting)
root.nodes.add(monitor_growth)
root.nodes.add(collect_data)
root.nodes.add(manage_pests)
root.nodes.add(harvest_crops)
root.nodes.add(coordinate_sales)
root.nodes.add(compost_waste)
root.nodes.add(review_feedback)

root.order.add_edge(assess_structure, analyze_environment)
root.order.add_edge(analyze_environment, design_modules)
root.order.add_edge(design_modules, procure_materials)
root.order.add_edge(procure_materials, install_irrigation)
root.order.add_edge(install_irrigation, set_sensors)
root.order.add_edge(set_sensors, select_seeds)
root.order.add_edge(select_seeds, schedule_planting)
root.order.add_edge(schedule_planting, monitor_growth)
root.order.add_edge(monitor_growth, collect_data)
root.order.add_edge(collect_data, manage_pests)
root.order.add_edge(manage_pests, harvest_crops)
root.order.add_edge(harvest_crops, coordinate_sales)
root.order.add_edge(coordinate_sales, compost_waste)
root.order.add_edge(compost_waste, review_feedback)

# Print the POWL model
print(root)
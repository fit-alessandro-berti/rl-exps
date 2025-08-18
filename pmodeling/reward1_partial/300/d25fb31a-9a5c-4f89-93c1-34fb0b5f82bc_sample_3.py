from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for data collection and pest management
loop_data_pests = OperatorPOWL(operator=Operator.LOOP, children=[collect_data, manage_pests])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[
    assess_structure,
    analyze_environment,
    design_modules,
    procure_materials,
    install_irrigation,
    set_sensors,
    select_seeds,
    schedule_planting,
    loop_data_pests,
    harvest_crops,
    coordinate_sales,
    compost_waste,
    review_feedback
])

# Define dependencies in the partial order
root.order.add_edge(assess_structure, analyze_environment)
root.order.add_edge(analyze_environment, design_modules)
root.order.add_edge(design_modules, procure_materials)
root.order.add_edge(procure_materials, install_irrigation)
root.order.add_edge(install_irrigation, set_sensors)
root.order.add_edge(set_sensors, select_seeds)
root.order.add_edge(select_seeds, schedule_planting)
root.order.add_edge(schedule_planting, loop_data_pests)
root.order.add_edge(loop_data_pests, harvest_crops)
root.order.add_edge(harvest_crops, coordinate_sales)
root.order.add_edge(coordinate_sales, compost_waste)
root.order.add_edge(compost_waste, review_feedback)

print(root)
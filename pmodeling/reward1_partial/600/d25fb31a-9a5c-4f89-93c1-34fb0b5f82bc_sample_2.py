import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
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

# Define the relationships between activities using OperatorPOWL objects
partial_order = StrictPartialOrder(nodes=[
    assess_structure,
    analyze_environment,
    design_modules,
    procure_materials,
    install_irrigation,
    set_sensors,
    select_seeds,
    schedule_planting,
    monitor_growth,
    collect_data,
    manage_pests,
    harvest_crops,
    coordinate_sales,
    compost_waste,
    review_feedback
])

# Add the defined activities and relationships to the StrictPartialOrder model
partial_order.order.add_edge(assess_structure, analyze_environment)
partial_order.order.add_edge(analyze_environment, design_modules)
partial_order.order.add_edge(design_modules, procure_materials)
partial_order.order.add_edge(procure_materials, install_irrigation)
partial_order.order.add_edge(install_irrigation, set_sensors)
partial_order.order.add_edge(set_sensors, select_seeds)
partial_order.order.add_edge(select_seeds, schedule_planting)
partial_order.order.add_edge(schedule_planting, monitor_growth)
partial_order.order.add_edge(monitor_growth, collect_data)
partial_order.order.add_edge(collect_data, manage_pests)
partial_order.order.add_edge(manage_pests, harvest_crops)
partial_order.order.add_edge(harvest_crops, coordinate_sales)
partial_order.order.add_edge(coordinate_sales, compost_waste)
partial_order.order.add_edge(compost_waste, review_feedback)

# Save the final result in the variable 'root'
root = partial_order
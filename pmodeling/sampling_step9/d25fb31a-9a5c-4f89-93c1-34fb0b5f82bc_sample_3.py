import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the exclusive choice for selecting irrigation and sensor installation
xor = OperatorPOWL(operator=Operator.XOR, children=[install_irrigation, set_sensors])

# Define the loop for planting and pest management
loop = OperatorPOWL(operator=Operator.LOOP, children=[schedule_planting, manage_pests])

# Define the partial order
root = StrictPartialOrder(nodes=[assess_structure, analyze_environment, design_modules, procure_materials, xor, loop, harvest_crops, coordinate_sales, compost_waste, review_feedback])
root.order.add_edge(assess_structure, analyze_environment)
root.order.add_edge(analyze_environment, design_modules)
root.order.add_edge(design_modules, procure_materials)
root.order.add_edge(procure_materials, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, harvest_crops)
root.order.add_edge(harvest_crops, coordinate_sales)
root.order.add_edge(coordinate_sales, compost_waste)
root.order.add_edge(compost_waste, review_feedback)
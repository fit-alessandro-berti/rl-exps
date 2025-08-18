import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
procure_modules = Transition(label='Procure Modules')
install_framework = Transition(label='Install Framework')
setup_sensors = Transition(label='Setup Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
configure_iot = Transition(label='Configure IoT')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_lighting = Transition(label='Manage Lighting')
pest_control = Transition(label='Pest Control')
recycle_waste = Transition(label='Recycle Waste')
analyze_data = Transition(label='Analyze Data')
adjust_environment = Transition(label='Adjust Environment')
harvest_crops = Transition(label='Harvest Crops')
distribute_produce = Transition(label='Distribute Produce')

# Define workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[procure_modules, install_framework])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[setup_sensors, calibrate_nutrients])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[configure_iot, plant_seeding])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, manage_lighting])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, recycle_waste])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[analyze_data, adjust_environment])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, distribute_produce])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)

print(root)
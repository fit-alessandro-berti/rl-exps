import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

site_survey_and_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
procure_and_install = OperatorPOWL(operator=Operator.XOR, children=[procure_modules, install_framework])
setup_and_calibrate = OperatorPOWL(operator=Operator.XOR, children=[setup_sensors, calibrate_nutrients])
iot_and_manage = OperatorPOWL(operator=Operator.XOR, children=[configure_iot, manage_lighting])
pest_and_recycle = OperatorPOWL(operator=Operator.XOR, children=[pest_control, recycle_waste])
analyze_and_adjust = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, adjust_environment])
harvest_and_distribute = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, distribute_produce])

site_survey_and_design_and_procure_and_install = OperatorPOWL(operator=Operator.XOR, children=[site_survey_and_design, procure_and_install])
setup_and_calibrate_and_iot_and_manage_and_pest_and_recycle = OperatorPOWL(operator=Operator.XOR, children=[setup_and_calibrate, iot_and_manage, pest_and_recycle])
analyze_and_adjust_and_harvest_and_distribute = OperatorPOWL(operator=Operator.XOR, children=[analyze_and_adjust, harvest_and_distribute])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey_and_design_and_procure_and_install, setup_and_calibrate_and_iot_and_manage_and_pest_and_recycle])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[analyze_and_adjust_and_harvest_and_distribute])

root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, analyze_and_adjust_and_harvest_and_distribute)
root.order.add_edge(loop2, analyze_and_adjust_and_harvest_and_distribute)
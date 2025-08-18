from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
program_climate = Transition(label='Program Climate')
select_crops = Transition(label='Select Crops')
optimize_lighting = Transition(label='Optimize Lighting')
train_staff = Transition(label='Train Staff')
plan_harvest = Transition(label='Plan Harvest')
recycle_waste = Transition(label='Recycle Waste')
analyze_demand = Transition(label='Analyze Demand')
plan_logistics = Transition(label='Plan Logistics')
monitor_systems = Transition(label='Monitor Systems')

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
site_survey_node = StrictPartialOrder(nodes=[site_survey, regulation_check])
design_modules_node = StrictPartialOrder(nodes=[design_modules, install_hydroponics, integrate_sensors, calibrate_nutrients, program_climate])
crop_selection_node = StrictPartialOrder(nodes=[select_crops, optimize_lighting, train_staff, plan_harvest])
waste_recycling_node = StrictPartialOrder(nodes=[recycle_waste, analyze_demand, plan_logistics])
system_monitoring_node = StrictPartialOrder(nodes=[monitor_systems])

# Define exclusive choice nodes
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[crop_selection_node, waste_recycling_node])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[site_survey_node, design_modules_node])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[choice_2, choice_1])
root.order.add_edge(choice_2, choice_1)

print(root)
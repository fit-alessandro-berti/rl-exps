import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the exclusive choice for regulatory checks and site surveys
xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, site_survey])

# Define the loop for design modules and installation of hydroponics
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, install_hydroponics])

# Define the exclusive choice for nutrient solution calibration and climate programming
xor2 = OperatorPOWL(operator=Operator.XOR, children=[calibrate_nutrients, program_climate])

# Define the exclusive choice for crop selection based on microclimate data and lighting optimization
xor3 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, optimize_lighting])

# Define the exclusive choice for staff training on automated systems and harvesting schedule development
xor4 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, plan_harvest])

# Define the exclusive choice for waste recycling protocols and market demand analysis
xor5 = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, analyze_demand])

# Define the exclusive choice for distribution logistics planning and ongoing system performance monitoring
xor6 = OperatorPOWL(operator=Operator.XOR, children=[plan_logistics, monitor_systems])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])

# Define the dependencies between nodes
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

# Return the root node
return root
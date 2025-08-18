import pm4py
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

# Define exclusive choice for staff training
xor_staff = OperatorPOWL(operator=Operator.XOR, children=[train_staff, skip])

# Define exclusive choice for crop selection
xor_crop = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])

# Define exclusive choice for nutrient solution calibration
xor_calibrate = OperatorPOWL(operator=Operator.XOR, children=[calibrate_nutrients, skip])

# Define exclusive choice for lighting optimization
xor_lighting = OperatorPOWL(operator=Operator.XOR, children=[optimize_lighting, skip])

# Define loop for climate control programming
loop_program = OperatorPOWL(operator=Operator.LOOP, children=[program_climate])

# Define loop for hydroponic unit installation
loop_install = OperatorPOWL(operator=Operator.LOOP, children=[install_hydroponics])

# Define loop for sensor integration
loop_integrate = OperatorPOWL(operator=Operator.LOOP, children=[integrate_sensors])

# Define loop for nutrient solution calibration
loop_calibrate = OperatorPOWL(operator=Operator.LOOP, children=[xor_calibrate])

# Define loop for lighting optimization
loop_lighting = OperatorPOWL(operator=Operator.LOOP, children=[xor_lighting])

# Define root node as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    design_modules,
    loop_install,
    loop_integrate,
    loop_calibrate,
    loop_lighting,
    xor_crop,
    xor_staff,
    plan_harvest,
    recycle_waste,
    analyze_demand,
    plan_logistics,
    monitor_systems
])

# Define dependencies between nodes
root.order.add_edge(site_survey, regulation_check)
root.order.add_edge(regulation_check, design_modules)
root.order.add_edge(design_modules, loop_install)
root.order.add_edge(loop_install, loop_integrate)
root.order.add_edge(loop_integrate, loop_calibrate)
root.order.add_edge(loop_calibrate, loop_lighting)
root.order.add_edge(loop_lighting, xor_crop)
root.order.add_edge(xor_crop, xor_staff)
root.order.add_edge(xor_staff, plan_harvest)
root.order.add_edge(plan_harvest, recycle_waste)
root.order.add_edge(recycle_waste, analyze_demand)
root.order.add_edge(analyze_demand, plan_logistics)
root.order.add_edge(plan_logistics, monitor_systems)

# Print the root node
print(root)
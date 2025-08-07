import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
regulation_check  = Transition(label='Regulation Check')
design_modules    = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
program_climate   = Transition(label='Program Climate')
select_crops      = Transition(label='Select Crops')
optimize_lighting = Transition(label='Optimize Lighting')
train_staff       = Transition(label='Train Staff')
plan_harvest      = Transition(label='Plan Harvest')
recycle_waste     = Transition(label='Recycle Waste')
analyze_demand    = Transition(label='Analyze Demand')
plan_logistics    = Transition(label='Plan Logistics')
monitor_systems   = Transition(label='Monitor Systems')

# Define the loop body: Plan Harvest -> Recycle Waste -> Analyze Demand -> Plan Logistics
body = StrictPartialOrder(nodes=[plan_harvest, recycle_waste, analyze_demand, plan_logistics])
body.order.add_edge(plan_harvest, recycle_waste)
body.order.add_edge(recycle_waste, analyze_demand)
body.order.add_edge(analyze_demand, plan_logistics)

# LOOP operator: do Design Modules, then repeatedly do the loop body and Design Modules again
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, regulation_check, loop,
    train_staff, optimize_lighting,
    select_crops, calibrate_nutrients, program_climate,
    install_hydroponics, integrate_sensors
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, regulation_check)
root.order.add_edge(regulation_check, loop)
root.order.add_edge(loop, train_staff)
root.order.add_edge(loop, optimize_lighting)
root.order.add_edge(loop, select_crops)
root.order.add_edge(loop, calibrate_nutrients)
root.order.add_edge(loop, program_climate)
root.order.add_edge(loop, install_hydroponics)
root.order.add_edge(loop, integrate_sensors)
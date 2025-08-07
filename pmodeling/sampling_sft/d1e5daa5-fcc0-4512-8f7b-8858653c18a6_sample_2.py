import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
regulation_check= Transition(label='Regulation Check')
design_modules  = Transition(label='Design Modules')
install_hydro   = Transition(label='Install Hydroponics')
integrate_sens  = Transition(label='Integrate Sensors')
calibrate_nut   = Transition(label='Calibrate Nutrients')
program_climate = Transition(label='Program Climate')
select_crops    = Transition(label='Select Crops')
optimize_light  = Transition(label='Optimize Lighting')
train_staff     = Transition(label='Train Staff')
plan_harvest    = Transition(label='Plan Harvest')
recycle_waste   = Transition(label='Recycle Waste')
analyze_demand  = Transition(label='Analyze Demand')
plan_logistics  = Transition(label='Plan Logistics')
monitor_systems = Transition(label='Monitor Systems')

# Loop for ongoing system monitoring
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_systems, monitor_systems]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, regulation_check,
    design_modules, install_hydro, integrate_sens, calibrate_nut, program_climate,
    select_crops, optimize_light, train_staff,
    plan_harvest, recycle_waste, analyze_demand, plan_logistics,
    monitor_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, regulation_check)
root.order.add_edge(regulation_check, design_modules)
root.order.add_edge(design_modules, install_hydro)
root.order.add_edge(install_hydro, integrate_sens)
root.order.add_edge(integrate_sens, calibrate_nut)
root.order.add_edge(calibrate_nut, program_climate)
root.order.add_edge(program_climate, select_crops)
root.order.add_edge(select_crops, optimize_light)
root.order.add_edge(optimize_light, train_staff)
root.order.add_edge(train_staff, plan_harvest)
root.order.add_edge(plan_harvest, recycle_waste)
root.order.add_edge(recycle_waste, analyze_demand)
root.order.add_edge(analyze_demand, plan_logistics)
root.order.add_edge(plan_logistics, monitor_loop)
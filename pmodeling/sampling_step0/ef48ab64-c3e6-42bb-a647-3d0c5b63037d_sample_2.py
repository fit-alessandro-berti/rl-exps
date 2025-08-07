from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_select = Transition(label='Site Select')
env_assess = Transition(label='Env Assess')
design_modules = Transition(label='Design Modules')
hydroponics_setup = Transition(label='Hydroponics Setup')
software_dev = Transition(label='Software Dev')
seed_choose = Transition(label='Seed Choose')
led_install = Transition(label='LED Install')
train_staff = Transition(label='Train Staff')
compliance_check = Transition(label='Compliance Check')
engage_community = Transition(label='Engage Community')
plant_crops = Transition(label='Plant Crops')
monitor_growth = Transition(label='Monitor Growth')
optimize_yields = Transition(label='Optimize Yields')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
water_recycle = Transition(label='Water Recycle')

# Define silent transitions
skip = SilentTransition()

# Define partial order for each phase
phase1 = OperatorPOWL(operator=Operator.PO, children=[site_select, env_assess, design_modules, hydroponics_setup])
phase2 = OperatorPOWL(operator=Operator.PO, children=[software_dev, seed_choose, led_install, train_staff])
phase3 = OperatorPOWL(operator=Operator.PO, children=[compliance_check, engage_community])
phase4 = OperatorPOWL(operator=Operator.PO, children=[plant_crops, monitor_growth, optimize_yields])
phase5 = OperatorPOWL(operator=Operator.PO, children=[waste_manage, energy_audit, water_recycle])

# Define exclusive choice for each phase
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[phase1, phase2, phase3, phase4, phase5])

# Define loop for each phase
loop_phase1 = OperatorPOWL(operator=Operator.LOOP, children=[phase1])
loop_phase2 = OperatorPOWL(operator=Operator.LOOP, children=[phase2])
loop_phase3 = OperatorPOWL(operator=Operator.LOOP, children=[phase3])
loop_phase4 = OperatorPOWL(operator=Operator.LOOP, children=[phase4])
loop_phase5 = OperatorPOWL(operator=Operator.LOOP, children=[phase5])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop_phase1, loop_phase2, loop_phase3, loop_phase4, loop_phase5, exclusive_choice])

# Add edges to the root POWL model
root.order.add_edge(loop_phase1, exclusive_choice)
root.order.add_edge(loop_phase2, exclusive_choice)
root.order.add_edge(loop_phase3, exclusive_choice)
root.order.add_edge(loop_phase4, exclusive_choice)
root.order.add_edge(loop_phase5, exclusive_choice)

print(root)
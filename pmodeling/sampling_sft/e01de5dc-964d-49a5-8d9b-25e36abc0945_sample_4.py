import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_select    = Transition(label='Seed Select')
germinate      = Transition(label='Germinate Seeds')
transplant     = Transition(label='Transplant Seedlings')
mix_nutrients  = Transition(label='Mix Nutrients')
adjust_pH      = Transition(label='Adjust pH')
monitor_climate= Transition(label='Monitor Climate')
control_humidity=Transition(label='Control Humidity')
co2_regulation = Transition(label='CO2 Regulation')
detect_pests   = Transition(label='Detect Pests')
deploy_bio     = Transition(label='Deploy Biocontrols')
schedule_harv  = Transition(label='Schedule Harvest')
automate_pick  = Transition(label='Automate Picking')
package_produce= Transition(label='Package Produce')
compost_waste  = Transition(label='Compost Waste')
recycle_water  = Transition(label='Recycle Water')
data_logging   = Transition(label='Data Logging')
system_maint   = Transition(label='System Maintenance')

# Loop for continuous monitoring and control
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_climate, control_humidity, co2_regulation]
)

# Choice for pest intervention: either detect or do nothing
pest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[detect_pests, SilentTransition()]
)

# Choice for biocontrol deployment: either deploy or do nothing
bio_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[deploy_bio, SilentTransition()]
)

# Loop for harvest scheduling and automated picking
harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[schedule_harv, automate_pick]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seed_select, germinate, transplant,
    mix_nutrients, adjust_pH,
    monitor_loop, pest_choice, bio_choice,
    harvest_loop, package_produce,
    compost_waste, recycle_water,
    data_logging, system_maint
])

# Add the control-flow edges
root.order.add_edge(seed_select, germinate)
root.order.add_edge(germinate, transplant)
root.order.add_edge(transplant, mix_nutrients)
root.order.add_edge(mix_nutrients, adjust_pH)
root.order.add_edge(adjust_pH, monitor_loop)

# After monitoring, choose either to detect pests or skip
root.order.add_edge(monitor_loop, pest_choice)

# After pest choice, either deploy bio or skip
root.order.add_edge(pest_choice, bio_choice)

# After bio choice, enter the harvest loop
root.order.add_edge(bio_choice, harvest_loop)

# Inside the harvest loop, do the rest of the steps
for target in [schedule_harv, automate_pick, package_produce,
               compost_waste, recycle_water, data_logging, system_maint]:
    root.order.add_edge(harvest_loop, target)
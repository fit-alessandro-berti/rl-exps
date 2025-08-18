import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

# Define the dependencies and loops
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, permit_acquire])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[modular_build, climate_setup, nutrient_mix])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[seed_automation, pest_control, energy_audit])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, growth_monitor, waste_process])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, staff_train, community_link])

# Create the partial order
root = StrictPartialOrder(nodes=[
    loop_1, loop_2, loop_3, loop_4, loop_5, yield_report
])

# Add dependencies between loops
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)
root.order.add_edge(loop_5, yield_report)

# Print the root POWL model
print(root)
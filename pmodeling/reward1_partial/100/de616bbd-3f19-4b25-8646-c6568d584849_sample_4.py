import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
system_design = Transition(label='System Design')
hydroponics_setup = Transition(label='Hydroponics Setup')
lighting_install = Transition(label='Lighting Install')
sensor_install = Transition(label='Sensor Install')
climate_control = Transition(label='Climate Control')
nutrient_monitor = Transition(label='Nutrient Monitor')
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
auto_planting = Transition(label='Auto Planting')
growth_monitoring = Transition(label='Growth Monitoring')
ai_analytics = Transition(label='AI Analytics')
robotic_harvest = Transition(label='Robotic Harvest')
packaging = Transition(label='Packaging')
trace_labeling = Transition(label='Trace Labeling')
logistics_plan = Transition(label='Logistics Plan')

# Define the exclusive choice
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, germination_start])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_setup, lighting_install])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, structural_check, system_design, loop, exclusive_choice, climate_control, nutrient_monitor, ai_analytics, robotic_harvest, packaging, trace_labeling, logistics_plan])
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, loop)
root.order.add_edge(loop, exclusive_choice)
root.order.add_edge(exclusive_choice, climate_control)
root.order.add_edge(climate_control, nutrient_monitor)
root.order.add_edge(nutrient_monitor, ai_analytics)
root.order.add_edge(ai_analytics, robotic_harvest)
root.order.add_edge(robotic_harvest, packaging)
root.order.add_edge(packaging, trace_labeling)
root.order.add_edge(trace_labeling, logistics_plan)

print(root)
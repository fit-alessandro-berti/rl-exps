import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_setup, lighting_install, sensor_install, climate_control, nutrient_monitor, seed_selection, germination_start])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[auto_planting, growth_monitoring, ai_analytics, robotic_harvest, packaging, trace_labeling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan])

root = StrictPartialOrder(nodes=[site_analysis, structural_check, system_design, xor1, xor2, xor3])
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
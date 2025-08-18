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

site_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structural_check])
system_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, hydroponics_setup, lighting_install, sensor_install, climate_control, nutrient_monitor])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_start, auto_planting])
growth_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, ai_analytics])
robotic_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[robotic_harvest, packaging, trace_labeling, logistics_plan])

root = StrictPartialOrder(nodes=[site_analysis_loop, system_design_loop, seed_selection_loop, growth_monitoring_loop, robotic_harvest_loop])
root.order.add_edge(site_analysis_loop, system_design_loop)
root.order.add_edge(system_design_loop, seed_selection_loop)
root.order.add_edge(seed_selection_loop, growth_monitoring_loop)
root.order.add_edge(growth_monitoring_loop, robotic_harvest_loop)

print(root)
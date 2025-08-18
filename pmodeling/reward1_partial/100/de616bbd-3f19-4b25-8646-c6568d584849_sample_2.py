import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define choices
system_design_choice = OperatorPOWL(operator=Operator.XOR, children=[system_design, hydroponics_setup, lighting_install])
sensor_install_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, climate_control, nutrient_monitor])
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, germination_start, auto_planting])
growth_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, ai_analytics, robotic_harvest])
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging, trace_labeling])
logistics_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan])

# Define loops
hydroponics_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_setup, lighting_install])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, climate_control, nutrient_monitor])
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_start, auto_planting])
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, ai_analytics, robotic_harvest])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging, trace_labeling])

# Define root node
root = StrictPartialOrder(nodes=[site_analysis, structural_check, system_design_choice, sensor_install_choice, seed_selection_choice, growth_monitoring_choice, packaging_choice, logistics_plan_choice])
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design_choice)
root.order.add_edge(system_design_choice, sensor_install_choice)
root.order.add_edge(sensor_install_choice, seed_selection_choice)
root.order.add_edge(seed_selection_choice, growth_monitoring_choice)
root.order.add_edge(growth_monitoring_choice, packaging_choice)
root.order.add_edge(packaging_choice, logistics_plan_choice)
root.order.add_edge(site_analysis, hydroponics_loop)
root.order.add_edge(hydroponics_loop, sensor_loop)
root.order.add_edge(sensor_loop, seed_loop)
root.order.add_edge(seed_loop, growth_loop)
root.order.add_edge(growth_loop, packaging_loop)
root.order.add_edge(packaging_loop, hydroponics_loop)

print(root)
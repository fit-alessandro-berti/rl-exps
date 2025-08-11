import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, auto_planting, growth_monitoring])
ai_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_analytics, robotic_harvest, packaging])

# Define XOR nodes
sensor_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
climate_control_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_control, skip])

# Define partial order
root = StrictPartialOrder(nodes=[site_analysis, structural_check, system_design, hydroponics_setup, lighting_install, sensor_xor, climate_control_xor, growth_loop, ai_loop, logistics_plan])
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, hydroponics_setup)
root.order.add_edge(hydroponics_setup, lighting_install)
root.order.add_edge(lighting_install, sensor_xor)
root.order.add_edge(sensor_xor, climate_control_xor)
root.order.add_edge(climate_control_xor, growth_loop)
root.order.add_edge(growth_loop, ai_loop)
root.order.add_edge(ai_loop, logistics_plan)

print(root)
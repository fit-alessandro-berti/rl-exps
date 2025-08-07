import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis       = Transition(label='Site Analysis')
structural_check    = Transition(label='Structural Check')
system_design       = Transition(label='System Design')
hydroponics_setup   = Transition(label='Hydroponics Setup')
lighting_install    = Transition(label='Lighting Install')
sensor_install      = Transition(label='Sensor Install')
climate_control     = Transition(label='Climate Control')
nutrient_monitor    = Transition(label='Nutrient Monitor')
seed_selection      = Transition(label='Seed Selection')
germination_start   = Transition(label='Germination Start')
auto_planting       = Transition(label='Auto Planting')
growth_monitoring   = Transition(label='Growth Monitoring')
ai_analytics        = Transition(label='AI Analytics')
robotic_harvest     = Transition(label='Robotic Harvest')
packaging           = Transition(label='Packaging')
trace_labeling      = Transition(label='Trace Labeling')
logistics_plan      = Transition(label='Logistics Plan')

# Build the monitoring & harvesting partial order
monitoring_po = StrictPartialOrder(nodes=[
    growth_monitoring, ai_analytics, robotic_harvest, packaging, trace_labeling, logistics_plan
])
monitoring_po.order.add_edge(growth_monitoring, ai_analytics)
monitoring_po.order.add_edge(ai_analytics, robotic_harvest)
monitoring_po.order.add_edge(robotic_harvest, packaging)
monitoring_po.order.add_edge(packaging, trace_labeling)
monitoring_po.order.add_edge(trace_labeling, logistics_plan)

# Loop: after each growth monitoring, either exit or repeat the monitoring
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, monitoring_po])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structural_check, system_design,
    hydroponics_setup, lighting_install, sensor_install,
    climate_control, nutrient_monitor,
    seed_selection, germination_start,
    auto_planting, loop_monitoring
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, hydroponics_setup)
root.order.add_edge(system_design, lighting_install)
root.order.add_edge(system_design, sensor_install)
root.order.add_edge(hydroponics_setup, climate_control)
root.order.add_edge(hydroponics_setup, nutrient_monitor)
root.order.add_edge(lighting_install, climate_control)
root.order.add_edge(lighting_install, nutrient_monitor)
root.order.add_edge(sensor_install, climate_control)
root.order.add_edge(sensor_install, nutrient_monitor)
root.order.add_edge(climate_control, auto_planting)
root.order.add_edge(nutrient_monitor, auto_planting)
root.order.add_edge(auto_planting, loop_monitoring)
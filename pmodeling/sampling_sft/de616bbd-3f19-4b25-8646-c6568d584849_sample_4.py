import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_analysis    = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
system_design    = Transition(label='System Design')
hydroponics      = Transition(label='Hydroponics Setup')
lighting         = Transition(label='Lighting Install')
sensor_install   = Transition(label='Sensor Install')
climate_control  = Transition(label='Climate Control')
nutrient_monitor = Transition(label='Nutrient Monitor')
seed_selection   = Transition(label='Seed Selection')
germination      = Transition(label='Germination Start')
auto_planting    = Transition(label='Auto Planting')
growth_monitor   = Transition(label='Growth Monitoring')
ai_analytics     = Transition(label='AI Analytics')
robotic_harvest  = Transition(label='Robotic Harvest')
packaging        = Transition(label='Packaging')
trace_labeling   = Transition(label='Trace Labeling')
logistics_plan   = Transition(label='Logistics Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structural_check,
    system_design,
    hydroponics,
    lighting,
    sensor_install,
    climate_control,
    nutrient_monitor,
    seed_selection,
    germination,
    auto_planting,
    growth_monitor,
    ai_analytics,
    robotic_harvest,
    packaging,
    trace_labeling,
    logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis,    structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design,    hydroponics)
root.order.add_edge(system_design,    lighting)
root.order.add_edge(hydroponics,      sensor_install)
root.order.add_edge(lighting,         sensor_install)
root.order.add_edge(sensor_install,   climate_control)
root.order.add_edge(sensor_install,   nutrient_monitor)
root.order.add_edge(climate_control,  germination)
root.order.add_edge(nutrient_monitor, germination)
root.order.add_edge(germination,      auto_planting)

# Continuous monitoring and automated actions
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, ai_analytics])
root.order.add_edge(auto_planting, monitor_loop)

# Harvesting and packaging
root.order.add_edge(monitor_loop, robotic_harvest)
root.order.add_edge(robotic_harvest, packaging)

# Final steps
root.order.add_edge(packaging, trace_labeling)
root.order.add_edge(trace_labeling, logistics_plan)
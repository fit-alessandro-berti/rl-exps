import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
permit_filing    = Transition(label='Permit Filing')
foundation_prep  = Transition(label='Foundation Prep')
frame_build      = Transition(label='Frame Build')
system_design    = Transition(label='System Design')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
climate_control  = Transition(label='Climate Control')
nutrient_mix     = Transition(label='Nutrient Mix')
crop_planting    = Transition(label='Crop Planting')
pest_scouting    = Transition(label='Pest Scouting')
data_monitoring  = Transition(label='Data Monitoring')
energy_audit     = Transition(label='Energy Audit')
waste_sorting    = Transition(label='Waste Sorting')
community_meet   = Transition(label='Community Meet')
yield_analysis   = Transition(label='Yield Analysis')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitoring, skip]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    permit_filing,
    foundation_prep,
    frame_build,
    system_design,
    irrigation_setup,
    lighting_install,
    climate_control,
    nutrient_mix,
    crop_planting,
    pest_scouting,
    monitor_loop,
    energy_audit,
    waste_sorting,
    community_meet,
    yield_analysis
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, permit_filing)
root.order.add_edge(permit_filing, foundation_prep)
root.order.add_edge(foundation_prep, frame_build)
root.order.add_edge(frame_build, system_design)
root.order.add_edge(system_design, irrigation_setup)
root.order.add_edge(system_design, lighting_install)
root.order.add_edge(system_design, climate_control)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(lighting_install, climate_control)
root.order.add_edge(climate_control, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_planting)
root.order.add_edge(crop_planting, pest_scouting)
root.order.add_edge(pest_scouting, monitor_loop)
root.order.add_edge(monitor_loop, energy_audit)
root.order.add_edge(monitor_loop, waste_sorting)
root.order.add_edge(monitor_loop, community_meet)
root.order.add_edge(monitor_loop, yield_analysis)
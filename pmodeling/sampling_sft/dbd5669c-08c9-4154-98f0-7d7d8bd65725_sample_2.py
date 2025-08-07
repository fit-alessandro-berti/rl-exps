import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
unit_assembly    = Transition(label='Unit Assembly')
system_wiring    = Transition(label='System Wiring')
sensor_install   = Transition(label='Sensor Install')
water_testing    = Transition(label='Water Testing')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
planting_setup   = Transition(label='Planting Setup')
climate_control  = Transition(label='Climate Control')
pest_management  = Transition(label='Pest Management')
data_calibration = Transition(label='Data Calibration')
yield_analysis   = Transition(label='Yield Analysis')
community_meet   = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
expansion_plan   = Transition(label='Expansion Plan')

# Loop for continuous yield analysis and data calibration
loop_body = StrictPartialOrder(nodes=[yield_analysis, data_calibration])
loop_body.order.add_edge(yield_analysis, data_calibration)

# Loop: do Site Survey, then either exit or repeat Design Layout->...->loop_body
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    loop,
    design_layout,
    material_sourcing,
    unit_assembly,
    system_wiring,
    sensor_install,
    water_testing,
    nutrient_mix,
    seed_selection,
    planting_setup,
    climate_control,
    pest_management,
    community_meet,
    compliance_check,
    expansion_plan
])

# Sequence for initial design layout
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, unit_assembly)
root.order.add_edge(unit_assembly, system_wiring)
root.order.add_edge(system_wiring, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(planting_setup, climate_control)
root.order.add_edge(climate_control, pest_management)
root.order.add_edge(pest_management, data_calibration)
root.order.add_edge(data_calibration, yield_analysis)

# Community engagement and compliance check after the initial loop
root.order.add_edge(loop, community_meet)
root.order.add_edge(community_meet, compliance_check)

# Expansion planning after compliance check
root.order.add_edge(compliance_check, expansion_plan)
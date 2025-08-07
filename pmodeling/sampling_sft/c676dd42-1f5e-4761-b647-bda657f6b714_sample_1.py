import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
system_assembly  = Transition(label='System Assembly')
sensor_install   = Transition(label='Sensor Install')
nutrient_prep    = Transition(label='Nutrient Prep')
water_testing    = Transition(label='Water Testing')
climate_setup    = Transition(label='Climate Setup')
data_integration = Transition(label='Data Integration')
energy_audit     = Transition(label='Energy Audit')
growth_monitoring= Transition(label='Growth Monitoring')
pest_control     = Transition(label='Pest Control')
waste_sorting    = Transition(label='Waste Sorting')
harvest_plan     = Transition(label='Harvest Plan')
produce_pack     = Transition(label='Produce Pack')
community_setup  = Transition(label='Community Setup')

# Silent transition for loop exit
skip = SilentTransition()

# Loop body (monitoring, pest control, waste sorting)
body = StrictPartialOrder(nodes=[growth_monitoring, pest_control, waste_sorting])
body.order.add_edge(growth_monitoring, pest_control)
body.order.add_edge(pest_control, waste_sorting)

# Loop: after sensor install, do body then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    material_sourcing,
    system_assembly,
    loop,
    data_integration,
    energy_audit,
    harvest_plan,
    produce_pack,
    community_setup
])

# Add the control-flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, system_assembly)
root.order.add_edge(system_assembly, loop)
root.order.add_edge(loop, data_integration)
root.order.add_edge(data_integration, energy_audit)
root.order.add_edge(energy_audit, harvest_plan)
root.order.add_edge(harvest_plan, produce_pack)
root.order.add_edge(produce_pack, community_setup)
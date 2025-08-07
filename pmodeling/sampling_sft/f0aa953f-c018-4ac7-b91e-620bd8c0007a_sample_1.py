import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
system_assembly= Transition(label='System Assembly')
climate_setup  = Transition(label='Climate Setup')
light_calibration= Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep  = Transition(label='Seedling Prep')
nutrient_mix   = Transition(label='Nutrient Mix')
irrigation_setup= Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration= Transition(label='Data Integration')
waste_routing  = Transition(label='Waste Routing')
energy_audit   = Transition(label='Energy Audit')
regulation_check= Transition(label='Regulation Check')
operational_test= Transition(label='Operational Test')
community_outreach= Transition(label='Community Outreach')

# Build the operational test sequence as a partial order
op_seq = StrictPartialOrder(nodes=[
    climate_setup, light_calibration,
    seed_selection, seedling_prep,
    nutrient_mix, irrigation_setup,
    sensor_install, data_integration,
    waste_routing, energy_audit,
    regulation_check, operational_test
])
op_seq.order.add_edge(climate_setup, light_calibration)
op_seq.order.add_edge(climate_setup, seed_selection)
op_seq.order.add_edge(light_calibration, seed_selection)
op_seq.order.add_edge(seed_selection, seedling_prep)
op_seq.order.add_edge(seedling_prep, nutrient_mix)
op_seq.order.add_edge(nutrient_mix, irrigation_setup)
op_seq.order.add_edge(irrigation_setup, sensor_install)
op_seq.order.add_edge(sensor_install, data_integration)
op_seq.order.add_edge(data_integration, waste_routing)
op_seq.order.add_edge(waste_routing, energy_audit)
op_seq.order.add_edge(energy_audit, regulation_check)
op_seq.order.add_edge(regulation_check, operational_test)

# Loop for repeated community outreach after each operational test
community_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[community_outreach, operational_test]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_assembly,
    op_seq, community_loop
])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, op_seq)
root.order.add_edge(op_seq, community_loop)

print(root)
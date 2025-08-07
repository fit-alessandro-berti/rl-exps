import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
system_assembly  = Transition(label='System Assembly')
climate_setup    = Transition(label='Climate Setup')
light_calibration= Transition(label='Light Calibration')
seed_selection   = Transition(label='Seed Selection')
seedling_prep    = Transition(label='Seedling Prep')
nutrient_mix     = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install   = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing    = Transition(label='Waste Routing')
energy_audit     = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach= Transition(label='Community Outreach')

# Define the calibration sub-process: Climate Setup -> Light Calibration
calibration = StrictPartialOrder(nodes=[climate_setup, light_calibration])
calibration.order.add_edge(climate_setup, light_calibration)

# Define the nutrient mix sub-process: Seed Selection -> Seedling Prep -> Nutrient Mix
nutrient_sub = StrictPartialOrder(nodes=[seed_selection, seedling_prep, nutrient_mix])
nutrient_sub.order.add_edge(seed_selection, seedling_prep)
nutrient_sub.order.add_edge(seedling_prep, nutrient_mix)

# Define the sensor setup sub-process: Irrigation Setup -> Sensor Install
sensor_sub = StrictPartialOrder(nodes=[irrigation_setup, sensor_install])
sensor_sub.order.add_edge(irrigation_setup, sensor_install)

# Define the waste routing sub-process: Waste Routing
waste_routing_sub = StrictPartialOrder(nodes=[waste_routing])

# Define the energy audit sub-process: Energy Audit
energy_sub = StrictPartialOrder(nodes=[energy_audit])

# Define the regulation check sub-process: Regulation Check
regulation_sub = StrictPartialOrder(nodes=[regulation_check])

# Define the operational test sub-process: Operational Test
operational_sub = StrictPartialOrder(nodes=[operational_test])

# Define the community outreach sub-process: Community Outreach
community_sub = StrictPartialOrder(nodes=[community_outreach])

# Define the root process as a loop: 
#   Site Survey -> Design Layout -> System Assembly -> Calibration -> Nutrient Mix
#   -> Sensor Setup -> Waste Routing -> Energy Audit -> Regulation Check
#   -> Operational Test -> Community Outreach
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_assembly, calibration,
    nutrient_sub, sensor_sub, waste_routing_sub, energy_sub,
    regulation_sub, operational_sub, community_outreach
])

# Add the sequence and parallel dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, calibration)
root.order.add_edge(calibration, nutrient_sub)
root.order.add_edge(calibration, sensor_sub)
root.order.add_edge(nutrient_sub, sensor_sub)
root.order.add_edge(sensor_sub, waste_routing_sub)
root.order.add_edge(waste_routing_sub, energy_sub)
root.order.add_edge(energy_sub, regulation_sub)
root.order.add_edge(regulation_sub, operational_sub)
root.order.add_edge(operational_sub, community_outreach)

# Define the loop: do Site Survey -> Design Layout -> System Assembly, then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, system_assembly])

# Assemble the final root process
root.order.add_edge(loop, calibration)
root.order.add_edge(calibration, nutrient_sub)
root.order.add_edge(calibration, sensor_sub)
root.order.add_edge(nutrient_sub, waste_routing_sub)
root.order.add_edge(waste_routing_sub, energy_sub)
root.order.add_edge(energy_sub, regulation_sub)
root.order.add_edge(regulation_sub, operational_sub)
root.order.add_edge(operational_sub, community_outreach)
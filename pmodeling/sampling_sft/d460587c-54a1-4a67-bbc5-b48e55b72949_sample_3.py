import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
permit_filing    = Transition(label='Permit Filing')
load_testing     = Transition(label='Load Testing')
soil_sampling    = Transition(label='Soil Sampling')
water_testing    = Transition(label='Water Testing')
system_design    = Transition(label='System Design')
solar_setup      = Transition(label='Solar Setup')
crop_planning    = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order   = Transition(label='Material Order')
system_install   = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control     = Transition(label='Pest Control')
market_launch    = Transition(label='Market Launch')

# Silent transition for loop continuation
skip = SilentTransition()

# Define the growth monitoring loop:
#   * (monitoring, pest_control) means: do monitoring, then choose to exit or do pest_control then repeat
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitoring, pest_control]
)

# Build the overall partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_filing,
        load_testing,
        soil_sampling,
        water_testing,
        system_design,
        solar_setup,
        crop_planning,
        stakeholder_meet,
        material_order,
        system_install,
        environmental_audit,
        growth_loop,
        market_launch
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(site_survey,     permit_filing)
root.order.add_edge(permit_filing,   load_testing)
root.order.add_edge(load_testing,    soil_sampling)
root.order.add_edge(soil_sampling,   water_testing)
root.order.add_edge(water_testing,   system_design)
root.order.add_edge(system_design,   solar_setup)
root.order.add_edge(solar_setup,     crop_planning)
root.order.add_edge(crop_planning,   stakeholder_meet)
root.order.add_edge(stakeholder_meet, material_order)
root.order.add_edge(material_order, system_install)
root.order.add_edge(system_install,  environmental_audit)
root.order.add_edge(environmental_audit, growth_loop)
root.order.add_edge(growth_loop,     market_launch)
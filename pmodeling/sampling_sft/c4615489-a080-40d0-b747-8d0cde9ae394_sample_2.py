import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
structural_audit  = Transition(label='Structural Audit')
permit_filing     = Transition(label='Permit Filing')
design_layout     = Transition(label='Design Layout')
install_hvac      = Transition(label='Install HVAC')
set_lighting      = Transition(label='Set Lighting')
build_racks       = Transition(label='Build Racks')
install_hydro     = Transition(label='Install Hydroponics')
configure_sensors = Transition(label='Configure Sensors')
select_crops      = Transition(label='Select Crops')
seed_planting     = Transition(label='Seed Planting')
monitor_growth    = Transition(label='Monitor Growth')
nutrient_mixing   = Transition(label='Nutrient Mixing')
staff_training    = Transition(label='Staff Training')
market_launch     = Transition(label='Market Launch')
waste_recycling   = Transition(label='Waste Recycling')
customer_onboard  = Transition(label='Customer Onboarding')

# Define the monitoring loop: Monitor Growth, then optionally repeat Nutrient Mixing
monitor_po = StrictPartialOrder(nodes=[monitor_growth, nutrient_mixing])
monitor_po.order.add_edge(monitor_growth, nutrient_mixing)

loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_po, nutrient_mixing])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    permit_filing,
    design_layout,
    install_hvac,
    set_lighting,
    build_racks,
    install_hydro,
    configure_sensors,
    select_crops,
    seed_planting,
    loop_monitor,
    staff_training,
    market_launch,
    waste_recycling,
    customer_onboard
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, permit_filing)
root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(design_layout, install_hvac)
root.order.add_edge(install_hvac, set_lighting)
root.order.add_edge(set_lighting, build_racks)
root.order.add_edge(build_racks, install_hydro)
root.order.add_edge(install_hydro, configure_sensors)
root.order.add_edge(configure_sensors, select_crops)
root.order.add_edge(select_crops, seed_planting)
root.order.add_edge(seed_planting, loop_monitor)
root.order.add_edge(loop_monitor, staff_training)
root.order.add_edge(staff_training, market_launch)
root.order.add_edge(market_launch, waste_recycling)
root.order.add_edge(waste_recycling, customer_onboard)
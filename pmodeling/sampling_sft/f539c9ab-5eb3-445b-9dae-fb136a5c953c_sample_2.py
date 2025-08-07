import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
structural_audit  = Transition(label='Structural Audit')
modular_design    = Transition(label='Modular Design')
hydroponic_setup  = Transition(label='Hydroponic Setup')
climate_config    = Transition(label='Climate Config')
lighting_setup    = Transition(label='Lighting Setup')
energy_audit      = Transition(label='Energy Audit')
automation_install= Transition(label='Automation Install')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_detect       = Transition(label='Pest Detect')
staff_training    = Transition(label='Staff Training')
market_analysis   = Transition(label='Market Analysis')
regulation_check  = Transition(label='Regulation Check')
yield_monitor     = Transition(label='Yield Monitor')
waste_manage      = Transition(label='Waste Manage')
data_analytics    = Transition(label='Data Analytics')

# Loop for continuous yield monitoring and waste management
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitor, waste_manage]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    modular_design,
    hydroponic_setup,
    climate_config,
    lighting_setup,
    energy_audit,
    automation_install,
    nutrient_mix,
    pest_detect,
    staff_training,
    market_analysis,
    regulation_check,
    monitor_loop,
    data_analytics
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, modular_design)
root.order.add_edge(modular_design, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_config)
root.order.add_edge(climate_config, lighting_setup)
root.order.add_edge(lighting_setup, energy_audit)
root.order.add_edge(energy_audit, automation_install)
root.order.add_edge(automation_install, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_detect)
root.order.add_edge(pest_detect, staff_training)
root.order.add_edge(staff_training, market_analysis)
root.order.add_edge(market_analysis, regulation_check)
root.order.add_edge(regulation_check, monitor_loop)
root.order.add_edge(monitor_loop, data_analytics)
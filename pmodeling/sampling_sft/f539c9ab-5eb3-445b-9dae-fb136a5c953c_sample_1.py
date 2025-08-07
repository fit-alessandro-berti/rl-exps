import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
modular_design  = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config  = Transition(label='Climate Config')
nutrient_mix    = Transition(label='Nutrient Mix')
lighting_setup  = Transition(label='Lighting Setup')
energy_audit    = Transition(label='Energy Audit')
automation_install = Transition(label='Automation Install')
regulation_check = Transition(label='Regulation Check')
market_analysis = Transition(label='Market Analysis')
staff_training  = Transition(label='Staff Training')
yield_monitor   = Transition(label='Yield Monitor')
waste_manage    = Transition(label='Waste Manage')
data_analytics  = Transition(label='Data Analytics')

# Define the monitoring & optimization loop: monitor then optionally optimize and repeat
monitor_body = StrictPartialOrder(nodes=[yield_monitor, waste_manage])
monitor_body.order.add_edge(yield_monitor, waste_manage)

optimization_body = StrictPartialOrder(nodes=[data_analytics, automation_install])
optimization_body.order.add_edge(data_analytics, automation_install)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, optimization_body])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_audit, modular_design,
    hydroponic_setup, climate_config, nutrient_mix, lighting_setup,
    energy_audit, automation_install, regulation_check,
    market_analysis, staff_training,
    monitor_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, modular_design)
root.order.add_edge(modular_design, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_config)
root.order.add_edge(climate_config, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_setup)
root.order.add_edge(lighting_setup, energy_audit)
root.order.add_edge(energy_audit, automation_install)
root.order.add_edge(automation_install, regulation_check)
root.order.add_edge(regulation_check, market_analysis)
root.order.add_edge(market_analysis, staff_training)
root.order.add_edge(staff_training, monitor_loop)
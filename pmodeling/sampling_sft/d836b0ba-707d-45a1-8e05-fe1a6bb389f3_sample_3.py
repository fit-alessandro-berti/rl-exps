import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_select      = Transition(label='Site Select')
design_layout    = Transition(label='Design Layout')
sensor_integrate = Transition(label='Sensor Integrate')
crop_choose      = Transition(label='Crop Choose')
soil_prepare     = Transition(label='Soil Prepare')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control     = Transition(label='Pest Control')
lighting_install = Transition(label='Lighting Install')
staff_train      = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
market_analyze   = Transition(label='Market Analyze')
package_design   = Transition(label='Package Design')
logistics_plan   = Transition(label='Logistics Plan')
data_analyze     = Transition(label='Data Analyze')
feedback_loop    = Transition(label='Feedback Loop')

# Define the monitoring & analysis partial order
monitoring = StrictPartialOrder(nodes=[
    sensor_integrate,
    soil_prepare,
    irrigation_setup,
    pest_control,
    lighting_install,
    data_analyze
])
# No ordering constraints => they can run in parallel

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    site_select,
    design_layout,
    compliance_check,
    market_analyze,
    staff_train,
    monitoring,
    package_design,
    logistics_plan,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_select, design_layout)
root.order.add_edge(design_layout, compliance_check)
root.order.add_edge(design_layout, market_analyze)
root.order.add_edge(design_layout, staff_train)
root.order.add_edge(compliance_check, monitoring)
root.order.add_edge(market_analyze, monitoring)
root.order.add_edge(staff_train, monitoring)
root.order.add_edge(monitoring, package_design)
root.order.add_edge(monitoring, logistics_plan)
root.order.add_edge(monitoring, feedback_loop)
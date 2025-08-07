import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
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

# Build the loop body: Data Analyze -> Feedback Loop
body = StrictPartialOrder(nodes=[data_analyze, feedback_loop])
body.order.add_edge(data_analyze, feedback_loop)

# Define the LOOP operator: do Design Layout -> Sensor Integrate -> Crop Choose -> Soil Prepare -> Irrigation Setup -> Pest Control -> Lighting Install -> Staff Train -> Compliance Check -> Market Analyze -> Package Design -> Logistics Plan, then optionally repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_select,
    loop,
    compliance_check,
    market_analyze,
    package_design,
    logistics_plan
])

# Define the control-flow edges
root.order.add_edge(site_select, loop)
root.order.add_edge(loop, compliance_check)
root.order.add_edge(compliance_check, market_analyze)
root.order.add_edge(market_analyze, package_design)
root.order.add_edge(package_design, logistics_plan)
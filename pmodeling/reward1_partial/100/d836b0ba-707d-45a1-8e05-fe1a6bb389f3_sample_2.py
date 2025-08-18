from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
site_select = Transition(label='Site Select')
design_layout = Transition(label='Design Layout')
sensor_integrate = Transition(label='Sensor Integrate')
crop_choose = Transition(label='Crop Choose')
soil_prepare = Transition(label='Soil Prepare')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control = Transition(label='Pest Control')
lighting_install = Transition(label='Lighting Install')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
market_analyze = Transition(label='Market Analyze')
package_design = Transition(label='Package Design')
logistics_plan = Transition(label='Logistics Plan')
data_analyze = Transition(label='Data Analyze')
feedback_loop = Transition(label='Feedback Loop')

# Create exclusive choice for steps after site selection
site_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, sensor_integrate])

# Create loop for steps related to soil preparation and pest control
soil_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_prepare, pest_control])

# Create exclusive choice for steps related to irrigation setup and lighting installation
irrigation_lighting_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, lighting_install])

# Create exclusive choice for steps related to staff training, compliance check, market analysis, packaging, logistics, and data analysis
staff_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_train, compliance_check, market_analyze, package_design, logistics_plan, data_analyze])

# Create loop for steps related to feedback loop
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_select, site_choice, soil_pest_loop, irrigation_lighting_choice, staff_analysis_choice, feedback_loop_loop])

# Add edges between nodes
root.order.add_edge(site_select, site_choice)
root.order.add_edge(site_choice, soil_pest_loop)
root.order.add_edge(site_choice, irrigation_lighting_choice)
root.order.add_edge(soil_pest_loop, staff_analysis_choice)
root.order.add_edge(irrigation_lighting_choice, staff_analysis_choice)
root.order.add_edge(staff_analysis_choice, feedback_loop_loop)
root.order.add_edge(feedback_loop_loop, site_select)
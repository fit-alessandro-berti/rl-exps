from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_select = Transition(label='Site Select')
layout_design = Transition(label='Design Layout')
sensor_integration = Transition(label='Sensor Integrate')
crop_selection = Transition(label='Crop Choose')
soil_preparation = Transition(label='Soil Prepare')
irrigation_setup = Transition(label='Irrigation Setup')
pest_management = Transition(label='Pest Control')
lighting_installation = Transition(label='Lighting Install')
staff_training = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
market_analysis = Transition(label='Market Analyze')
package_design = Transition(label='Package Design')
logistics_planning = Transition(label='Logistics Plan')
data_analysis = Transition(label='Data Analyze')
feedback_loop = Transition(label='Feedback Loop')

root = StrictPartialOrder(nodes=[
    site_select,
    layout_design,
    sensor_integration,
    crop_selection,
    soil_preparation,
    irrigation_setup,
    pest_management,
    lighting_installation,
    staff_training,
    compliance_check,
    market_analysis,
    package_design,
    logistics_planning,
    data_analysis,
    feedback_loop
])

# Define dependencies between activities
root.order.add_edge(site_select, layout_design)
root.order.add_edge(layout_design, sensor_integration)
root.order.add_edge(sensor_integration, crop_selection)
root.order.add_edge(crop_selection, soil_preparation)
root.order.add_edge(soil_preparation, irrigation_setup)
root.order.add_edge(irrigation_setup, pest_management)
root.order.add_edge(pest_management, lighting_installation)
root.order.add_edge(lighting_installation, staff_training)
root.order.add_edge(staff_training, compliance_check)
root.order.add_edge(compliance_check, market_analysis)
root.order.add_edge(market_analysis, package_design)
root.order.add_edge(package_design, logistics_planning)
root.order.add_edge(logistics_planning, data_analysis)
root.order.add_edge(data_analysis, feedback_loop)

# Close the loop by adding a self-loop at the end
root.order.add_edge(feedback_loop, feedback_loop)
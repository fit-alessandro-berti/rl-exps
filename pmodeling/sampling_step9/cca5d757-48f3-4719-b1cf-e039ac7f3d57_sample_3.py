import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Load_Testing = Transition(label='Load Testing')
Climate_Study = Transition(label='Climate Study')
Medium_Prep = Transition(label='Medium Prep')
Bed_Install = Transition(label='Bed Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Monitor_Deploy = Transition(label='Monitor Deploy')
Waste_Cycle = Transition(label='Waste Cycle')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Link = Transition(label='Market Link')
Workshop_Plan = Transition(label='Workshop Plan')
Tech_Integrate = Transition(label='Tech Integrate')
skip = SilentTransition()

# Site Assessment and Load Testing
site_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Assess, Load_Testing])
# Climate Study and Soil Medium Preparation
climate_study_loop = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Study, Medium_Prep])
# Modular Bed Installation and Automated Irrigation Setup
bed_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[Bed_Install, Irrigation_Setup])
# Crop Selection and Pest Management
crop_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Select, Pest_Control])
# Community Engagement and Educational Workshops
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[Community_Meet, Workshop_Plan])
# Digital Monitoring System Deployment and Waste Recycling Integration
monitor_deploy_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Deploy, Waste_Cycle])
# Seasonal Yield Forecasting and Establishment of Distribution Channels
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Forecast, Market_Link])

root = StrictPartialOrder(nodes=[site_assess_loop, climate_study_loop, bed_install_loop, crop_select_loop, community_meet_loop, monitor_deploy_loop, yield_forecast_loop, Tech_Integrate])
root.order.add_edge(site_assess_loop, climate_study_loop)
root.order.add_edge(climate_study_loop, bed_install_loop)
root.order.add_edge(bed_install_loop, crop_select_loop)
root.order.add_edge(crop_select_loop, community_meet_loop)
root.order.add_edge(community_meet_loop, monitor_deploy_loop)
root.order.add_edge(monitor_deploy_loop, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, Tech_Integrate)
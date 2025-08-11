from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_assess = Transition(label='Site Assess')
load_testing = Transition(label='Load Testing')
climate_study = Transition(label='Climate Study')
medium_prep = Transition(label='Medium Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
monitor_deploy = Transition(label='Monitor Deploy')
waste_cycle = Transition(label='Waste Cycle')
yield_forecast = Transition(label='Yield Forecast')
market_link = Transition(label='Market Link')
workshop_plan = Transition(label='Workshop Plan')
tech_integrate = Transition(label='Tech Integrate')

skip = SilentTransition()

site_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[site_assess, load_testing])
climate_study_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_study, medium_prep])
medium_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[medium_prep, bed_install])
bed_install_choice = OperatorPOWL(operator=Operator.XOR, children=[bed_install, irrigation_setup])
irrigation_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, crop_select])
crop_select_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_select, pest_control])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, community_meet])
community_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, monitor_deploy])
monitor_deploy_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_deploy, waste_cycle])
waste_cycle_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, yield_forecast])
yield_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, market_link])
market_link_choice = OperatorPOWL(operator=Operator.XOR, children=[market_link, workshop_plan])
workshop_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, tech_integrate])

root = StrictPartialOrder(nodes=[
    site_assess_choice,
    climate_study_choice,
    medium_prep_choice,
    bed_install_choice,
    irrigation_setup_choice,
    crop_select_choice,
    pest_control_choice,
    community_meet_choice,
    monitor_deploy_choice,
    waste_cycle_choice,
    yield_forecast_choice,
    market_link_choice,
    workshop_plan_choice
])
root.order.add_edge(site_assess_choice, climate_study_choice)
root.order.add_edge(climate_study_choice, medium_prep_choice)
root.order.add_edge(medium_prep_choice, bed_install_choice)
root.order.add_edge(bed_install_choice, irrigation_setup_choice)
root.order.add_edge(irrigation_setup_choice, crop_select_choice)
root.order.add_edge(crop_select_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, community_meet_choice)
root.order.add_edge(community_meet_choice, monitor_deploy_choice)
root.order.add_edge(monitor_deploy_choice, waste_cycle_choice)
root.order.add_edge(waste_cycle_choice, yield_forecast_choice)
root.order.add_edge(yield_forecast_choice, market_link_choice)
root.order.add_edge(market_link_choice, workshop_plan_choice)
root.order.add_edge(workshop_plan_choice, tech_integrate)
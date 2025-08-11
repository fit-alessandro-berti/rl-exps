from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the operators for the POWL model
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, community_meet])
partial_order = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[yield_forecast, market_link, workshop_plan, tech_integrate])
inclusive_choice = OperatorPOWL(operator=Operator.INCLUSIVE, children=[climate_study, medium_prep, bed_install, irrigation_setup, crop_select])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[inclusive_choice, exclusive_choice, partial_order])
root.order.add_edge(inclusive_choice, exclusive_choice)
root.order.add_edge(inclusive_choice, partial_order)
root.order.add_edge(exclusive_choice, partial_order)

print(root)
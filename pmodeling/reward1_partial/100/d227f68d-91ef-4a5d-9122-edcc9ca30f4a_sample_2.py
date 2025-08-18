from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_check = Transition(label='Permits Check')
foundation_prep = Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup = Transition(label='Hydro Setup')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_calibration = Transition(label='System Calibration')
pest_control = Transition(label='Pest Control')
automation_link = Transition(label='Automation Link')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')
distribution_plan = Transition(label='Distribution Plan')

# Define exclusive choice for seed selection
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])

# Define partial order for site survey, design layout, permits check, foundation prep, frame assembly, hydro setup, climate setup
site_infrastructure = StrictPartialOrder(nodes=[site_survey, design_layout, permits_check, foundation_prep, frame_assembly, hydro_setup, climate_setup])
site_infrastructure.order.add_edge(site_survey, design_layout)
site_infrastructure.order.add_edge(design_layout, permits_check)
site_infrastructure.order.add_edge(permits_check, foundation_prep)
site_infrastructure.order.add_edge(foundation_prep, frame_assembly)
site_infrastructure.order.add_edge(frame_assembly, hydro_setup)
site_infrastructure.order.add_edge(hydro_setup, climate_setup)

# Define partial order for pest control and automation link
pest_automation = StrictPartialOrder(nodes=[pest_control, automation_link])
pest_automation.order.add_edge(pest_control, automation_link)

# Define partial order for staff training, yield tracking, distribution plan
staff_yield_dist = StrictPartialOrder(nodes=[staff_training, yield_tracking, distribution_plan])
staff_yield_dist.order.add_edge(staff_training, yield_tracking)
staff_yield_dist.order.add_edge(yield_tracking, distribution_plan)

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[site_infrastructure, seed_selection_choice, pest_automation, staff_yield_dist])
root.order.add_edge(site_infrastructure, seed_selection_choice)
root.order.add_edge(seed_selection_choice, pest_automation)
root.order.add_edge(pest_automation, staff_yield_dist)
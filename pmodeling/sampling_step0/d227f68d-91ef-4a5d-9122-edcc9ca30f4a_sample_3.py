import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip = SilentTransition()

# Define the process model
site_survey_to_permits_check = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permits_check])
permits_check_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[permits_check, design_layout])
design_layout_to_foundation_prep = OperatorPOWL(operator=Operator.XOR, children=[design_layout, foundation_prep])
foundation_prep_to_frame_assembly = OperatorPOWL(operator=Operator.XOR, children=[foundation_prep, frame_assembly])
frame_assembly_to_hydro_setup = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, hydro_setup])
hydro_setup_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[hydro_setup, climate_setup])
climate_setup_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, seed_selection])
seed_selection_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
nutrient_mix_to_system_calibration = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, system_calibration])
system_calibration_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[system_calibration, pest_control])
pest_control_to_automation_link = OperatorPOWL(operator=Operator.XOR, children=[pest_control, automation_link])
automation_link_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[automation_link, staff_training])
staff_training_to_yield_tracking = OperatorPOWL(operator=Operator.XOR, children=[staff_training, yield_tracking])
yield_tracking_to_distribution_plan = OperatorPOWL(operator=Operator.XOR, children=[yield_tracking, distribution_plan])

root = StrictPartialOrder(nodes=[
    site_survey_to_permits_check,
    permits_check_to_design_layout,
    design_layout_to_foundation_prep,
    foundation_prep_to_frame_assembly,
    frame_assembly_to_hydro_setup,
    hydro_setup_to_climate_setup,
    climate_setup_to_seed_selection,
    seed_selection_to_nutrient_mix,
    nutrient_mix_to_system_calibration,
    system_calibration_to_pest_control,
    pest_control_to_automation_link,
    automation_link_to_staff_training,
    staff_training_to_yield_tracking,
    yield_tracking_to_distribution_plan
])

root.order.add_edge(site_survey_to_permits_check, permits_check_to_design_layout)
root.order.add_edge(permits_check_to_design_layout, design_layout_to_foundation_prep)
root.order.add_edge(design_layout_to_foundation_prep, foundation_prep_to_frame_assembly)
root.order.add_edge(foundation_prep_to_frame_assembly, frame_assembly_to_hydro_setup)
root.order.add_edge(frame_assembly_to_hydro_setup, hydro_setup_to_climate_setup)
root.order.add_edge(hydro_setup_to_climate_setup, climate_setup_to_seed_selection)
root.order.add_edge(climate_setup_to_seed_selection, seed_selection_to_nutrient_mix)
root.order.add_edge(seed_selection_to_nutrient_mix, nutrient_mix_to_system_calibration)
root.order.add_edge(nutrient_mix_to_system_calibration, system_calibration_to_pest_control)
root.order.add_edge(system_calibration_to_pest_control, pest_control_to_automation_link)
root.order.add_edge(pest_control_to_automation_link, automation_link_to_staff_training)
root.order.add_edge(automation_link_to_staff_training, staff_training_to_yield_tracking)
root.order.add_edge(staff_training_to_yield_tracking, yield_tracking_to_distribution_plan)

# Save the final result in the variable 'root'
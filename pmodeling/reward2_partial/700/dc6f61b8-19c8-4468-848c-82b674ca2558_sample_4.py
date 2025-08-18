from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
energy_partner = Transition(label='Energy Partner')
permit_filing = Transition(label='Permit Filing')
hydro_unit = Transition(label='Hydro Unit')
ai_setup = Transition(label='AI Setup')
nutrient_plan = Transition(label='Nutrient Plan')
system_install = Transition(label='System Install')
crop_testing = Transition(label='Crop Testing')
data_analysis = Transition(label='Data Analysis')
community_meet = Transition(label='Community Meet')
yield_adjust = Transition(label='Yield Adjust')
carbon_audit = Transition(label='Carbon Audit')
logistics_plan = Transition(label='Logistics Plan')
quality_check = Transition(label='Quality Check')
scale_review = Transition(label='Scale Review')

# Define the POWL model
root = StrictPartialOrder(nodes=[site_survey, energy_partner, permit_filing, hydro_unit, ai_setup, nutrient_plan, system_install, crop_testing, data_analysis, community_meet, yield_adjust, carbon_audit, logistics_plan, quality_check, scale_review])

# Define the dependencies
root.order.add_edge(site_survey, energy_partner)
root.order.add_edge(energy_partner, permit_filing)
root.order.add_edge(permit_filing, hydro_unit)
root.order.add_edge(hydro_unit, ai_setup)
root.order.add_edge(ai_setup, nutrient_plan)
root.order.add_edge(nutrient_plan, system_install)
root.order.add_edge(system_install, crop_testing)
root.order.add_edge(crop_testing, data_analysis)
root.order.add_edge(data_analysis, community_meet)
root.order.add_edge(community_meet, yield_adjust)
root.order.add_edge(yield_adjust, carbon_audit)
root.order.add_edge(carbon_audit, logistics_plan)
root.order.add_edge(logistics_plan, quality_check)
root.order.add_edge(quality_check, scale_review)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
permit_apply = Transition(label='Permit Apply')
material_order = Transition(label='Material Order')
bed_install = Transition(label='Bed Install')
pest_control = Transition(label='Pest Control')
solar_setup = Transition(label='Solar Setup')
staff_train = Transition(label='Staff Train')
market_outreach = Transition(label='Market Outreach')
system_setup = Transition(label='System Setup')
supplier_contact = Transition(label='Supplier Contact')
health_monitor = Transition(label='Health Monitor')

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    soil_sample,
    crop_select,
    irrigation_plan,
    permit_apply,
    material_order,
    bed_install,
    pest_control,
    solar_setup,
    staff_train,
    market_outreach,
    system_setup,
    supplier_contact,
    health_monitor
])

# Define the partial order dependencies
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(soil_sample, crop_select)
root.order.add_edge(crop_select, irrigation_plan)
root.order.add_edge(irrigation_plan, permit_apply)
root.order.add_edge(permit_apply, material_order)
root.order.add_edge(material_order, bed_install)
root.order.add_edge(bed_install, pest_control)
root.order.add_edge(pest_control, solar_setup)
root.order.add_edge(solar_setup, staff_train)
root.order.add_edge(staff_train, market_outreach)
root.order.add_edge(market_outreach, system_setup)
root.order.add_edge(system_setup, supplier_contact)
root.order.add_edge(supplier_contact, health_monitor)

# Print the root of the POWL model
print(root)
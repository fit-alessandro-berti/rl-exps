import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_survey_to_load_test = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test])
load_test_to_soil_sample = OperatorPOWL(operator=Operator.XOR, children=[load_test, soil_sample])
soil_sample_to_crop_select = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, crop_select])
crop_select_to_irrigation_plan = OperatorPOWL(operator=Operator.XOR, children=[crop_select, irrigation_plan])
irrigation_plan_to_permit_apply = OperatorPOWL(operator=Operator.XOR, children=[irrigation_plan, permit_apply])
permit_apply_to_material_order = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, material_order])
material_order_to_bed_install = OperatorPOWL(operator=Operator.XOR, children=[material_order, bed_install])
bed_install_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[bed_install, pest_control])
pest_control_to_solar_setup = OperatorPOWL(operator=Operator.XOR, children=[pest_control, solar_setup])
solar_setup_to_staff_train = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, staff_train])
staff_train_to_market_outreach = OperatorPOWL(operator=Operator.XOR, children=[staff_train, market_outreach])
market_outreach_to_system_setup = OperatorPOWL(operator=Operator.XOR, children=[market_outreach, system_setup])
system_setup_to_supplier_contact = OperatorPOWL(operator=Operator.XOR, children=[system_setup, supplier_contact])
supplier_contact_to_health_monitor = OperatorPOWL(operator=Operator.XOR, children=[supplier_contact, health_monitor])

root = StrictPartialOrder(nodes=[
    site_survey_to_load_test,
    load_test_to_soil_sample,
    soil_sample_to_crop_select,
    crop_select_to_irrigation_plan,
    irrigation_plan_to_permit_apply,
    permit_apply_to_material_order,
    material_order_to_bed_install,
    bed_install_to_pest_control,
    pest_control_to_solar_setup,
    solar_setup_to_staff_train,
    staff_train_to_market_outreach,
    market_outreach_to_system_setup,
    system_setup_to_supplier_contact,
    supplier_contact_to_health_monitor
])
root.order.add_edge(site_survey_to_load_test, load_test_to_soil_sample)
root.order.add_edge(load_test_to_soil_sample, soil_sample_to_crop_select)
root.order.add_edge(soil_sample_to_crop_select, crop_select_to_irrigation_plan)
root.order.add_edge(crop_select_to_irrigation_plan, irrigation_plan_to_permit_apply)
root.order.add_edge(irrigation_plan_to_permit_apply, permit_apply_to_material_order)
root.order.add_edge(permit_apply_to_material_order, material_order_to_bed_install)
root.order.add_edge(material_order_to_bed_install, bed_install_to_pest_control)
root.order.add_edge(bed_install_to_pest_control, pest_control_to_solar_setup)
root.order.add_edge(pest_control_to_solar_setup, solar_setup_to_staff_train)
root.order.add_edge(solar_setup_to_staff_train, staff_train_to_market_outreach)
root.order.add_edge(staff_train_to_market_outreach, market_outreach_to_system_setup)
root.order.add_edge(market_outreach_to_system_setup, system_setup_to_supplier_contact)
root.order.add_edge(system_setup_to_supplier_contact, supplier_contact_to_health_monitor)
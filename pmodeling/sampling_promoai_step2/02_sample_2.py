import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
begin_onboarding = Transition(label='Begin onboarding process')
choose_candidate = Transition(label='Choose candidate')
collect_resumes = Transition(label='Collect resumes')
complete_orientation = Transition(label='Complete orientation')
complete_paperwork = Transition(label='Complete paperwork')
complete_training = Transition(label='Complete training')
conduct_virtual_interview = Transition(label='Conduct a virtual interview')
conduct_in_person_interview = Transition(label='Conduct an in-person interview')
conduct_phone_interviews = Transition(label='Conduct initial phone interviews')
create_job_description = Transition(label='Create job description')
extend_offer = Transition(label='Extend offer')
identify_need_for_new_hire = Transition(label='Identify need for new hire')
invite_candidates = Transition(label='Invite candidates for interviews')
negotiate_salary = Transition(label='Negotiate salary')
post_job_description = Transition(label='Post job description')
screen_resumes = Transition(label='Screen resumes')

# Define the partial order
root = StrictPartialOrder(nodes=[
    begin_onboarding,
    choose_candidate,
    collect_resumes,
    complete_orientation,
    complete_paperwork,
    complete_training,
    conduct_virtual_interview,
    conduct_in_person_interview,
    conduct_phone_interviews,
    create_job_description,
    extend_offer,
    identify_need_for_new_hire,
    invite_candidates,
    negotiate_salary,
    post_job_description,
    screen_resumes
])

# Define the dependencies
root.order.add_edge(identify_need_for_new_hire, post_job_description)
root.order.add_edge(post_job_description, collect_resumes)
root.order.add_edge(collect_resumes, screen_resumes)
root.order.add_edge(screen_resumes, conduct_phone_interviews)
root.order.add_edge(conduct_phone_interviews, choose_candidate)
root.order.add_edge(choose_candidate, conduct_virtual_interview)
root.order.add_edge(choose_candidate, conduct_in_person_interview)
root.order.add_edge(conduct_virtual_interview, invite_candidates)
root.order.add_edge(conduct_in_person_interview, invite_candidates)
root.order.add_edge(invite_candidates, conduct_phone_interviews)
root.order.add_edge(invite_candidates, conduct_virtual_interview)
root.order.add_edge(invite_candidates, conduct_in_person_interview)
root.order.add_edge(conduct_phone_interviews, negotiate_salary)
root.order.add_edge(negotiate_salary, extend_offer)
root.order.add_edge(extend_offer, complete_paperwork)
root.order.add_edge(complete_paperwork, complete_training)
root.order.add_edge(complete_training, complete_orientation)
root.order.add_edge(complete_orientation, begin_onboarding)
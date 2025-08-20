import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Begin_onboarding_process = Transition(label='Begin onboarding process')
Choose_candidate = Transition(label='Choose candidate')
Collect_resumes = Transition(label='Collect resumes')
Complete_orientation = Transition(label='Complete orientation')
Complete_paperwork = Transition(label='Complete paperwork')
Complete_training = Transition(label='Complete training')
Conduct_a_virtual_interview = Transition(label='Conduct a virtual interview')
Conduct_an_in_person_interview = Transition(label='Conduct an in-person interview')
Conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
Create_job_description = Transition(label='Create job description')
Extend_offer = Transition(label='Extend offer')
Identify_need_for_new_hire = Transition(label='Identify need for new hire')
Invite_candidates_for_interviews = Transition(label='Invite candidates for interviews')
Negotiate_salary = Transition(label='Negotiate salary')
Post_job_description = Transition(label='Post job description')
Screen_resumes = Transition(label='Screen resumes')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Identify_need_for_new_hire,
    Create_job_description,
    Post_job_description,
    Collect_resumes,
    Screen_resumes,
    Conduct_initial_phone_interviews,
    Invite_candidates_for_interviews,
    Choose_candidate,
    Extend_offer,
    Negotiate_salary,
    Begin_onboarding_process,
    Complete_paperwork,
    Complete_orientation,
    Complete_training
])

root.order.add_edge(Identify_need_for_new_hire, Create_job_description)
root.order.add_edge(Create_job_description, Post_job_description)
root.order.add_edge(Post_job_description, Collect_resumes)
root.order.add_edge(Collect_resumes, Screen_resumes)
root.order.add_edge(Screen_resumes, Conduct_initial_phone_interviews)
root.order.add_edge(Conduct_initial_phone_interviews, Invite_candidates_for_interviews)
root.order.add_edge(Invite_candidates_for_interviews, Choose_candidate)
root.order.add_edge(Choose_candidate, Extend_offer)
root.order.add_edge(Extend_offer, Negotiate_salary)
root.order.add_edge(Negotiate_salary, Begin_onboarding_process)
root.order.add_edge(Begin_onboarding_process, Complete_paperwork)
root.order.add_edge(Complete_paperwork, Complete_orientation)
root.order.add_edge(Complete_orientation, Complete_training)

# Define the choice between in-person and virtual interviews
in_person_or_virtual_interview = OperatorPOWL(operator=Operator.XOR, children=[
    Conduct_an_in_person_interview,
    Conduct_a_virtual_interview
])

# Add the choice to the POWL model
root.nodes.add(in_person_or_virtual_interview)
root.order.add_edge(Invite_candidates_for_interviews, in_person_or_virtual_interview)
root.order.add_edge(in_person_or_virtual_interview, Choose_candidate)

# Define the loop for interviewing candidates
interview_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Invite_candidates_for_interviews,
    in_person_or_virtual_interview,
    Choose_candidate
])

# Add the loop to the POWL model
root.nodes.add(interview_loop)
root.order.add_edge(Conduct_initial_phone_interviews, interview_loop)
root.order.add_edge(interview_loop, Extend_offer)

# Define the choice between salary negotiations and extending the offer
salary_or_offer = OperatorPOWL(operator=Operator.XOR, children=[
    Negotiate_salary,
    Extend_offer
])

# Add the choice to the POWL model
root.nodes.add(salary_or_offer)
root.order.add_edge(Choose_candidate, salary_or_offer)
root.order.add_edge(salary_or_offer, Begin_onboarding_process)

# Define the loop for onboarding process
onboarding_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Begin_onboarding_process,
    Complete_paperwork,
    Complete_orientation,
    Complete_training
])

# Add the loop to the POWL model
root.nodes.add(onboarding_loop)
root.order.add_edge(Begin_onboarding_process, onboarding_loop)

# Define the end of the process
end_of_process = Transition(label='End of process')
root.nodes.add(end_of_process)
root.order.add_edge(Complete_training, end_of_process)
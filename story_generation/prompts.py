INSTRUCTIONS = """I want you to write a short story that involves a person X (or a group of people) who is NOT aware of a certain critical piece of KEY INFORMATION about an object or person (object/person/event Z). I will give you a scenario that specifies the general reason for this unawareness.

Your task is to instantiate the scenario with a 2-sentence story. Follow these steps:

1. Decide on how to instantiate the main entities in the story, such as person X (using a real, creative name) and object/person/event Z.

2. Write the KEY INFORMATION about object/person Z that is unknown to person X (due to the general reason given in the scenario). Person X should not be able to observe this KEY INFORMATION through their actions in the story (either implicit or explicit actions). DO NOT use information which might be observed by person X through normal, careful observation (such as "expiration date", "leaking container", "smell", etc). This will be the first sentence in the story.

3. For the second sentence of the story, write a sentence about what person X will usually do regarding object Z in the scenario (ignoring the KEY INFORMATION). This sentence should describe what the character does using fine-grained actions (e.g., "picked up object Z and walks to the cashier" rather than "buy object Z"). DO NOT include any descriptions which involve the emotions or thoughts of person X, just describe actions.

4. Write a question about what the next action of person X will likely be. 

5. Write a correct answer to the question (given the fact that person X is not aware of the KEY INFORMATION). Make sure the story does not have any mention of this action.

6. Write a counterfactual (incorrect) answer to the question. This answer should be a likely answer to the question under the assumption that person X somehow has full access to the KEY INFORMATION after all (maybe only possible using "magic" or some omnipotent skill).

7. Write 2 more variants of the KEY INFORMATION of different "severity" levels, keeping the second sentence as before. The "MILD SEVERITY" variant should be a more minor issue with less concern to person X. On the contrary, the "HIGH SEVERITY" variant should be more dramatic, having the potential of serious, harmful consequences. Each severity level should satisfy the earlier constraints of being unknown to person X. 

8. For each of the 2 new variants of KEY INFORMATION, write an updated counterfactual answer as tailored to the new variant. The question and correct answer should stay the same, so make sure the variants are compatible with them.


Important reminders to double-check before generating the story:

* Avoid stories about fantasy and magic, rather make them grounded in the real world.

* The fact that person X is unaware of the KEY INFORMATION should be a purely implicit deduction based on the commonsense logic of the scenario.

* Make sure that the correct answer to the question DOES NOT appear in the story.

* Make sure the KEY INFORMATION is not a regular occurrence or common practice that can be assumed to be true by default, or likely to be noticed through normal observation (e.g., a bottle that is leaking)

* DO NOT make KEY INFORMATION (even at MILD SEVERITY) so minor that it does not affect the action even if person X had been aware of it.

* DO NOT use phrases which make the hidden nature of the KEY INFORMATION obvious. That is, DO NOT use phrases like "actually", "in fact", "secret", "hidden", etc.


Here is an example scenario and associated story. Please follow the same template when creating the new story.

{scenario_example}

Here is the scenario I want you to use for the story (which might be the same as above but then generate a very different key information and story!). Please follow the steps above, skipping any steps I have already completed, and fill in the template following the pattern in the example above:
"""



SCENARIO_TEMPLATE = """SCENARIO:
{scenario}

ENTITIES:
{entities}

KEY INFORMATION:
{key_information}

STORY SECOND SENTENCE:
{story_sentence}

QUESTION:
{question}

CORRECT ANSWER (Person X doesn't know the KEY INFORMATION):
{correct_answer}

COUNTERFACTUAL ANSWER (assume Person X actually knows the KEY INFORMATION):
{incorrect_answer}

MILD SEVERITY KEY INFORMATION:
{sev1}

MILD SEVERITY COUNTERFACTUAL ANSWER:
{incorrect_answer_sev1}

HIGH SEVERITY KEY INFORMATION:
{sev3}

HIGH SEVERITY COUNTERFACTUAL ANSWER:
{incorrect_answer_sev3}

"""


INSTRUCTIONS_ENTITY_BRAINSTORM = """I want you to write a short story that involves a person X (or a group of people) who is NOT aware of a certain critical piece of KEY INFORMATION about an object or person (object/person Z). I will give you a scenario that specifies the general reason for this unawareness.

Your task is to instantiate the scenario with a 2-sentence story. Follow these steps:

1. Decide on how to instantiate the main entities in the story, such as person X (using a real, creative name) and object Z.

2. Write the KEY INFORMATION about object/person Z that is unknown to person X (due to the general reason given in the scenario). Person X should not be able to observe this KEY INFORMATION through their actions in the story (either implicit or explicit actions). DO NOT use information which might be observed by person X through normal, careful observation (such as "expiration date", "leaking container", "smell", etc). This will be the first sentence in the story.

3. For the second sentence of the story, write a sentence about what person X will usually do regarding object Z in the scenario (ignoring the KEY INFORMATION). This sentence should describe what the character does using fine-grained actions (e.g., "picked up object Z and walks to the cashier" rather than "buy object Z"). DO NOT include any descriptions which involve the emotions or thoughts of person X, just describe actions.

4. Write a question about what the next action of person X will likely be. 

5. Write a correct answer to the question (given the fact that person X is not aware of the KEY INFORMATION). Make sure the story does not have any mention of this action.

6. Write a counterfactual (incorrect) answer to the question. This answer should be a likely answer to the question under the assumption that person X somehow has full access to the KEY INFORMATION after all (maybe only possible using "magic" or some omnipotent skill).

For now, let us focus on step 1 to come up with possible suggestions for object Z which make it possible to generate such KEY INFORMATION and stories.

I will give you an example of entities and KEY INFORMATION. Your task is to come up with 10 more such examples, that are diverse and fulfill all these requirements.


Important reminders to double-check before generating the entities:

* Avoid stories about fantasy and magic, rather make them grounded in the real world.

* The fact that person X is unaware of the KEY INFORMATION should be a purely implicit deduction based on the commonsense logic of the scenario.

* Make sure the KEY INFORMATION is not a regular commonsense occurrence, a common practice, or likely to be noticed through normal observation (e.g., a bottle that is leaking)

* DO NOT make KEY INFORMATION so minor that it does not affect the action even if person X is aware of it.


The scenario in question is:

{scenario}


Here is the example:

{scenario_entity_example}


Now make 10 more examples of entities (and example KEY INFORMATION) for the above scenario, following the template above:

Example <N>:

ENTITIES:
<entities>

KEY INFORMATION:
<key information>
"""

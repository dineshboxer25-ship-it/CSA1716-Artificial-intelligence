
% Medical Diagnosis System

% Patient symptoms
symptom(ravi, fever).
symptom(ravi, cough).
symptom(priya, sneezing).
symptom(priya, runny_nose).

% Diagnosis rules
diagnosis(Person, flu_like_illness) :-
    symptom(Person, fever),
    symptom(Person, cough).

diagnosis(Person, allergy_like_symptoms) :-
    symptom(Person, sneezing),
    symptom(Person, runny_nose).

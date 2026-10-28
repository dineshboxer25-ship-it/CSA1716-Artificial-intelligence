
% Forward Chaining Program

% Initial facts
fact(rain).
fact(cloudy).

% Rules
rule(wet_ground) :-
    fact(rain).

rule(carry_umbrella) :-
    fact(rain).

rule(possible_rain) :-
    fact(cloudy).

% Derived conclusions
conclusion(X) :-
    rule(X).


% Family Tree Program

% Parent relationships
parent(john, mary).
parent(john, peter).
parent(mary, alice).
parent(peter, david).

% Gender facts
male(john).
male(peter).
male(david).

female(mary).
female(alice).

% Father relationship
father(X, Y) :-
    parent(X, Y),
    male(X).

% Mother relationship
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Grandparent relationship
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

% Sibling relationship
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

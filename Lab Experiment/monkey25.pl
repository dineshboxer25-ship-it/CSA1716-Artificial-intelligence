
% Monkey and Banana Problem

% State: state(MonkeyPosition, BoxPosition, Status)

% Monkey climbs onto the box
move(state(middle, middle, on_floor), climb,
     state(middle, middle, on_box)).

% Monkey grasps the banana
move(state(middle, middle, on_box), grasp,
     state(middle, middle, has_banana)).

% Goal: Monkey has the banana
solve(state(_, _, has_banana), []).

% Find the sequence of actions
solve(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).

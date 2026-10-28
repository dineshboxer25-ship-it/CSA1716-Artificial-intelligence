
% Fruit and Color Database

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grapes, purple).
fruit_color(mango, yellow).
fruit_color(guava, green).

% Find fruit by color
fruit_with_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

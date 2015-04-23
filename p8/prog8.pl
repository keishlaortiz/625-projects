%Keishla D. Ortiz López
%CSCE625-Artificial Intelligence

%Programming Assignment 8: Prolog - practice problems

%1. Write Prolog clauses that can be used to compute the intersection of two lists.
%?- intersection([1,2,3,4,5,6],[2,4,6,8],V).
%V = [2, 4, 6]

%the function assumes that the two lists are sets
% I couldn't redefine intersection, so I used intersect instead.
intersect([],C,[]). %base case
%if A is a member of the list C, then append A to the list D and recursively calls intersect with the rest of the list (B), C and D.
intersect([A|B],C,[A|D]) :- member(A,C),!,intersect(B,C,D). 
%if the second clause fails, then recursively calls intersect with the rest of the list B (excluding first element A), C and D.
intersect([A|B],C,D) :- intersect(B,C,D).

%% 2. Meal planning. Write a Prolog program that can be used to determine whether a list of foods
%% is a good meal.

calories(water,0).
calories(hamburger,354).
calories(carrot,25).
calories(salad,100).
calories(banana,105).
calories(apple,95).
calories(peanuts,828).
calories(chicken_soup,87).
calories(lasagna,166). % traditional meat lasagna
calories(apple_pie,67).
calories(beans,41).
calories(peas,118).
calories(milk,8).
calories(orange_juice,39).
calories(coke,140).
calories(cookie,132).
calories(naan,78).
calories(potato_soup,149).
calories(pineapple,452).
calories(watermelon,85).

meat(hamburger).
meat(chicken_soup).
meat(lasagna).

vegetable(carrot).
vegetable(salad).
vegetable(beans).
vegetable(peas).
vegetable(potato_soup).

fruit(apple).
fruit(banana).
fruit(orange_juice).
fruit(apple_pie).
fruit(pineapple).
fruit(watermelon).

drink(water).
drink(coke).
drink(orange_juice).
drink(milk).

legume(peas).
legume(beans).
legume(peanuts).

protein(milk).
protein(X) :- legume(X).
protein(X) :- meat(X).

fruit_or_vegetable(X) :- fruit(X).
fruit_or_vegetable(X) :- vegetable(X).

contains_protein([F|M]) :- protein(F),!.
contains_protein([F|M]) :- contains_protein(M). 

contains_fruit_or_vegetable([F|M]) :- fruit_or_vegetable(F),!.
contains_fruit_or_vegetable([F|M]) :- contains_fruit_or_vegetable(M).

contains_meat([F|M]):- meat(F),!.
contains_meat([F|M]):- contains_meat(M).

total([],0). %base case
total([F|Meal],Cals) :- total(Meal,MCals),calories(F,FCal),Cals is MCals+FCal.

nutritious(M) :- contains_fruit_or_vegetable(M),contains_protein(M).
vegetarian(M) :- \+contains_meat(M).

good_meal(M) :- total(M,Cals),write('Total calories: '),write(Cals),nutritious(M),Cals>=400,Cals=<600.
good_vegetarian_meal(M) :- good_meal(M),vegetarian(M).

%3. Write Prolog clauses that can be used to calculate square roots by Newton-Raphson
%% iteration. (see http://en.wikipedia.org/wiki/Newton%27s_method)
%% ?- sqrt(10,X).
%% X = 3.162288819352989

%fails if X is a negative number
sqrt(X,Y) :- X >= 0, CurrentEst is X, Tolerance is 1.0e-7, sqrt(X,CurrentEst,Tolerance,Y).

%base case
sqrt(Target,CurrentEst,Tolerance,FinalAnswer):- abs(CurrentEst*CurrentEst-Target,D),
                                                D=<Tolerance,
                                                !,
                                                FinalAnswer is CurrentEst.

%recursive (iterative) step
sqrt(Target,CurrentEst,Tolerance,FinalAnswer) :- X is CurrentEst - (CurrentEst*CurrentEst-Target)/(2*CurrentEst),
                                                 sqrt(Target,X,Tolerance,FinalAnswer). 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% 4. Solve the 5-queens problem in Prolog.
%% ?- queens(A,B,C,D,E).
%% A = 5 , B = 3 , C = 1 , D = 4, E = 2;
%% ...
%% (there are 10 solutions; show them all)
%% Each variables above are the Columns of the queens in Rows A-E.

solve_queens([]). %base case
solve_queens([(R1,C1)|L]) :- solve_queens(L),member(C1,[1,2,3,4,5]),no_attack((R1,C1),L).

no_attack(A,[]). %base case
no_attack((R1,C1),[(R2,C2)|L]) :- C1=\=C2,abs(R1-R2,A),abs(C1-C2,B),A=\=B,no_attack((R1,C1),L). %they cannot share column and diagonals
queens(A,B,C,D,E) :- L=[(1,A),(2,B),(3,C),(4,D),(5,E)],solve_queens(L). %L is a list of tuples (row,column)

%visualize board and then the assignment to variables...
%% print_queens(A,B,C,D,E) :- queens(A,B,C,D,E),L=[A,B,C,D,E],
%%                            forall(member(Col,L),(Col1 is Col-1, format('~|~`-t~*+Q~`-t~*|~n',[Col1,5]))).
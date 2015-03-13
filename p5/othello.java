/*
    Keishla D. Ortiz-Lopez
    CSCE 625 - Artificial Intelligence


    Othello main program
*/
import java.util.*;
public class othello 
{
    public static void main(String[] args)
    {
        //square size of the board
        int size = Integer.parseInt(args[0]);
        //color of the initial player (max)
        char color = args[1].toUpperCase().charAt(0);
        //depth limit of the minimax function
        int depth = Integer.parseInt(args[2]);

        Board game = new Board(color,size);

        Scanner input = new Scanner(System.in);
        char current_player = color; //current player
        int count = 0;

        //play the game
        while(true)
        {   
            count++;
            if(game.isGameOver() && count != 1) //determine the winner
            {
                int score = game.score();
                if(score == 0) //draw
                {
                    System.out.println("# draw");
                }
                else if(score < 0)
                {
                    System.out.println("# player "+game.getOpponent(color)+" won");
                }
                else
                {
                    System.out.println("# player "+color+" won");
                }

                current_player = color;
            }
            String command = input.nextLine();
            String[] pieces = command.split(" ");
            String c = pieces[0].toLowerCase();
            
            if(c.equals("quit"))
            {
                break;
            }
            else if(c.equals("init"))
            {
                if(game.isEmpty() || game.isGameOver())
                {
                    int x = -1, y = -1;
                    char answer;
                    System.out.println("# Random initial state? Y or N?");
                    answer = input.nextLine().charAt(0);
                    if(answer == 'y' || answer == 'Y')
                    {
                        x = randInt(0,size-2);
                        y = randInt(0,size-2);
                    }
                    game.init(x,y);
                    game.printBoard();
                }
                else
                    System.out.println("# board is not empty or the current game is not over yet");
            }
            else if(c.equals("reset"))
            {
                game.reset();
                System.out.println("# score=0");
                game.printBoard();
                current_player = color;
            }
            else if(c.equals("put"))
            {
                char player = pieces[1].toUpperCase().charAt(0);
                if(current_player == player)
                {
                    int x = Integer.parseInt(pieces[2]);
                    int y = Integer.parseInt(pieces[3]);
                    
                    ArrayList<Move> legal = game.legal_moves(current_player);

                    if(legal.size()==0)
                    {
                        System.out.println("forfeit turn");

                        current_player = game.getOpponent(current_player);
                    }
                    else{

                        boolean movement = false;
                        for (Move pos : legal) 
                        {
                            if(pos.x == x && pos.y == y)
                            {
                                System.out.println("("+x+","+y+")");
                                Board testBoard = game.make_move(current_player,x,y);
                                game.setBoard(testBoard.getBoard());
                                int score = game.score();
                                System.out.println("# score="+score);
                                game.printBoard();
                                current_player = game.getOpponent(current_player);
                                movement = true;
                                break;
                            }   
                        }

                        if(!movement)
                        {
                            System.out.println("# illegal move ("+x+","+y+")");
                        }
                    }
                }
                else
                {
                    System.out.println("# turn of player "+current_player+".");
                }
            }
            else if(c.equals("move"))
            {
                char player = pieces[1].toUpperCase().charAt(0);

                if(current_player == player)
                {
                    //call function minimax_move with the current board, player and depth (limit)
                    //if move is not null, call make move, otherwise forfeit the turn
                    System.out.println("# making move for "+current_player+"...");
                    boolean maximize = false;
                    if(current_player == color)
                    {
                        maximize = true;
                    }
                    Move possible_move = Minimax.minimax_move(game,current_player,depth,maximize,true);

                    if(possible_move.x != -1)
                    {
                        int x = possible_move.x, y = possible_move.y;
                        System.out.println("("+x+","+y+")");
                        Board testBoard = game.make_move(current_player,x,y);
                        game.setBoard(testBoard.getBoard());
                        System.out.println("# score="+game.score());
                        game.printBoard();
                    }
                    else
                    {
                        System.out.println("forfeit turn");
                    }

                    current_player = game.getOpponent(current_player); //in this case an movement or forfeit can occur.
                }
                else
                {
                    System.out.println("# turn of player "+current_player+".");
                }
            }
            else
            {
                System.out.println("# unknown command. Try again.");
            }

        }
    }

    //Reference: http://stackoverflow.com/questions/363681/generating-random-integers-in-a-range-with-java
    /**
    * Returns a pseudo-random number between min and max, inclusive.
    * The difference between min and max can be at most
    * <code>Integer.MAX_VALUE - 1</code>.
    *
    * @param min Minimum value
    * @param max Maximum value.  Must be greater than min.
    * @return Integer between min and max, inclusive.
    * @see java.util.Random#nextInt(int)
    */
    public static int randInt(int min, int max) {

        // NOTE: Usually this should be a field rather than a method
        // variable so that it is not re-seeded every call.
        Random rand = new Random();

        // nextInt is normally exclusive of the top value,
        // so add 1 to make it inclusive
        int randomNum = rand.nextInt((max - min) + 1) + min;

        return randomNum;
    }   
}
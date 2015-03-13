/*
    Keishla D. Ortiz-Lopez
    CSCE 625 - Artificial Intelligence


    Minimax function based on the pseudocode in http://en.wikipedia.org/wiki/Minimax
*/


import java.util.*;
public class Minimax
{
    public static Move minimax_move(Board board, char player, int depth, boolean maximizingPlayer, boolean origin)
    {
        if(depth==0 || board.isGameOver())
        {
            Move pos = new Move(-1,-1);
            pos.value = board.evaluation();
            return pos;
        }
    
        if(maximizingPlayer)
        {
            Move bestPos = new Move(-1,-1);
            ArrayList<Move> possible_moves = board.legal_moves(player);
            
            for(Move pos: possible_moves)
            {
                Board tempBoard = board.make_move(player,pos.x,pos.y);
                Move tempMove = minimax_move(tempBoard,board.getOpponent(player),depth-1,false,false);
                if(bestPos.x == -1 || tempMove.value >= bestPos.value)
                {

                    bestPos.value = tempMove.value;
                    bestPos.x = pos.x;
                    bestPos.y = pos.y;
                    if(origin)
                        System.out.println("# considering: "+"("+bestPos.x+","+bestPos.y+"), mm="+bestPos.value);
                }
            }

            return bestPos;
        }
        else
        {
            Move bestPos = new Move(-1,-1);
            
            ArrayList<Move> possible_moves = board.legal_moves(player);
            
            for(Move pos: possible_moves)
            {
                Board tempBoard = board.make_move(player,pos.x,pos.y);
                Move tempMove = minimax_move(tempBoard,board.getOpponent(player),depth-1,true,false);
                if(bestPos.x == -1 || tempMove.value <= bestPos.value)
                {
                    bestPos.value = tempMove.value;
                    bestPos.x = pos.x;
                    bestPos.y = pos.y;
                    if(origin)
                        System.out.println("# considering: "+"("+bestPos.x+","+bestPos.y+"), mm="+bestPos.value);
                }
            }
            
            return bestPos;
        }
    }
}

/*
    Keishla D. Ortiz-Lopez
    CSCE 625 - Artificial Intelligence


    Board class
*/
import java.util.ArrayList;
public class Board
{
    private char initial_player;
    private char board[][];
    private int n;

    public Board(char p, int size)
    {
        initial_player = p;
        board = new char[size][size];
        n = size;
    }

    //init the board
    public void init(int x,int y)
    {
        for (int i=0; i < n; i++) {
            for (int j=0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        if(x == -1 && y == -1)
        {
            int column = n/2;
            int row = column - 1;

            board[row][column-1] = getOpponent(initial_player);
            board[row][column] = initial_player;
            board[row+1][column-1] = initial_player;
            board[row+1][column] = getOpponent(initial_player);
        }
        else
        {
            board[x][y] = getOpponent(initial_player);
            board[x][y+1] = initial_player;
            board[x+1][y] = initial_player;
            board[x+1][y+1] = getOpponent(initial_player);
        }

        
        return;
    }

    //check if the board is empty
    public boolean isEmpty()
    {
        for (int i=0; i < n; i++) {
            for (int j=0; j < n; j++) {
                if (board[i][j] == 'B' || board[i][j] == 'W') //one position occupied
                    return false;
            }
        }
        return true;
    }

    //check if the board is full
    public boolean isFull()
    {
        for (int i=0; i < n; i++) {
            for (int j=0; j < n; j++) {
                if (board[i][j] != 'B' || board[i][j] != 'W') //one position empty
                    return false;
            }
        }
        return true;
    }

    //leaves the board empty
    public void reset()
    {
        for (int i=0; i < n; i++) {
            for (int j=0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        return;
    }
    //check if the game is over
    public boolean isGameOver()
    {
        //game is over when the board is full or there is no legal moves for both players
        if(isFull() || (legal_moves('W').size() == 0 && legal_moves('B').size() == 0))
            return true;

        return false;
    }

    public char getOpponent(char p)
    {
        if(p == 'B')
            return 'W';

        return 'B';
    }

    public char[][] getBoard()
    {
        return board;
    }

    public void setBoard(char[][] newBoard)
    {
        board = newBoard;
    }

    public void printBoard()
    {
        for (int i=0; i < n; i++) {
            System.out.print("# ");
            for (int j=0; j < n; j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println("");
        }
        return;
    }
    //check row to see if there are pieces to flip
    //return a list of positions to flip
    private ArrayList<Move> checkRow(char[][] tBoard, char p, Move c1, Move c2)
    {
        //same row
        ArrayList<Move> flip = new ArrayList<Move>();
        int x = c1.x, y = c1.y, i = c2.x, j = c2.y;
        boolean opponent = true;
        if(j < y)
        {
            for (int c = j+1; c < y; c++) 
            {
                if(tBoard[i][c] != getOpponent(p))
                {
                    opponent = false;
                    break;
                }

            }

            if(opponent)
            {
                for (int c = j+1; c < y; c++) 
                {
                    flip.add(new Move(i,c));
                }
            }
        }
        else
        {
            for (int c = j-1; c > y; c--) 
            {
                if(tBoard[i][c] != getOpponent(p))
                {
                    opponent = false;
                    break;
                }

            }

            if(opponent)
            {
                for (int c = j-1; c > y; c--) 
                {
                    flip.add(new Move(i,c));
                }
            }
        }

        return flip;
    }
    //check column to see if there are pieces to flip
    //return a list of positions to flip
    private ArrayList<Move> checkColumn(char[][] tBoard, char p, Move c1, Move c2)
    {
        ArrayList<Move> flip = new ArrayList<Move>();
        int x = c1.x, y = c1.y, i = c2.x, j = c2.y;
        boolean opponent = true;
        if(i < x)
        {
            for (int r = i+1; r < x; r++) 
            {
                if(tBoard[r][j] != getOpponent(p))
                {
                    opponent = false;
                    break;
                }

            }

            if(opponent)
            {
                for (int r = i+1; r < x; r++) 
                {
                    flip.add(new Move(r,j));
                }
            }
        }
        else
        {
            for (int r = i-1; r > x; r--) 
            {
                if(tBoard[r][j] != getOpponent(p))
                {
                    opponent = false;
                    break;
                }

            }

            if(opponent)
            {
                for (int r = i-1; r > x; r--) 
                {
                    flip.add(new Move(r,j));
                }
            }
        }

        return flip;
    }
    //check diagonal to see if there are pieces to flip
    //return a list of positions to flip
    private ArrayList<Move> checkDiagonal(char[][] tBoard, char p, Move c1, Move c2)
    {
        ArrayList<Move> flip = new ArrayList<Move>();
        int x = c1.x, y = c1.y, i = c2.x, j = c2.y;
        boolean opponent = true;
        if(i < x && j > y) //row is less than x and column is greater than y
        {
            int r = i+1, c = j - 1;
            while(r < x && c > y)
            {
                if(tBoard[r][c] != getOpponent(p))
                {
                    opponent = false;
                         break;
                }
                r++;
                c--;
            }

            if(opponent)
            {
                r = i+1; c = j - 1;
                while(r < x && c > y)
                {
                    flip.add(new Move(r,c));
                    r++;
                    c--;
                }
            }
        }
        else if(i > x && j < y)
        {
            int r = i-1, c = j + 1;
            while(r > x && c < y)
            {
                if(tBoard[r][c] != getOpponent(p))
                {
                    opponent = false;
                         break;
                }
                r--;
                c++;
            }

            if(opponent)
            {
                r = i-1; c = j + 1;
                while(r > x && c < y)
                {
                    flip.add(new Move(r,c));
                    r--;
                    c++;
                }
            }
        }
        else if(i < x && j < y)
        {
            int r = i+1, c = j + 1;
            while(r < x && c < y)
            {
                if(tBoard[r][c] != getOpponent(p))
                {
                    opponent = false;
                         break;
                }
                r++;
                c++;
            }

            if(opponent)
            {
                r = i+1; c = j + 1;
                while(r < x && c < y)
                {
                    flip.add(new Move(r,c));
                    r++;
                    c++;
                }
            }
        }
        else if(i > x && j > y)
        {
            int r = i-1, c = j - 1;
            while(r > x && c > y)
            {
                if(tBoard[r][c] != getOpponent(p))
                {
                    opponent = false;
                         break;
                }
                r--;
                c--;
            }

            if(opponent)
            {
                r = i-1; c = j-1;
                while(r > x && c > y)
                {
                    flip.add(new Move(r,c));
                    r--;
                    c--;
                }
            }
        }

        return flip;
    }

    private char[][] copyBoard()
    {
        char[][] state = new char[n][n];
        for (int i=0; i < n; i++) 
        {
            for (int j=0; j < n; j++) 
            {
                state[i][j] = board[i][j];      
            }    
        }

        return state;
    }

    //flipping algorithm function
    public Board make_move(char p, int x, int y)
    {
        char tempBoard[][] = copyBoard();
        ArrayList<Move> flipPositions = new ArrayList<Move>(); //positions to flip
        for (int i=0; i < n; i++)
        {
            for (int j = 0; j < n; j++) 
            {
                if(i==x && j==y)
                    continue;
                if(tempBoard[i][j] != p)
                    continue;

                Move pos1 = new Move(x,y);
                Move pos2 = new Move(i,j);
                
                ArrayList<Move> tempFlip = new ArrayList<Move>();
                if(i==x) //same row
                {
                    tempFlip = checkRow(tempBoard,p,pos1,pos2);
                }
                else if(j==y) //same column
                {
                    tempFlip = checkColumn(tempBoard,p,pos1,pos2);
                }
                else if(Math.abs(i-x) == Math.abs(j-y)) //diagonal
                {
                    tempFlip = checkDiagonal(tempBoard,p,pos1,pos2);
                }

                for (Move pos : tempFlip)
                {
                    flipPositions.add(pos);    
                }

        
            }    
        }


        //flip all the positions in flipPositions
        for (Move pos : flipPositions) 
        {
            tempBoard[pos.x][pos.y] = p;
        }
        Board temp = new Board(initial_player,n);
        if(flipPositions.size() != 0) //at least one piece was changed otherwise the board will be the same
            tempBoard[x][y] = p;

        temp.setBoard(tempBoard);
        return temp;
    }

    //legal moves iterate the board and call make_move with a empty position
    //append valid moves to the list legal_moves
    public ArrayList<Move> legal_moves(char p)
    {
        ArrayList<Move> legal_moves = new ArrayList<Move>();
        
        for (int i=0; i<n; i++) 
        {
           for (int j=0; j < n; j++) 
           {
                if(board[i][j] != '.')
                    continue;

                Board tBoard = make_move(p,i,j);
                if(score() != tBoard.score())
                {
                    legal_moves.add(new Move(i,j));
                }
                
            } 
        }
        return legal_moves;
    }

    //calculates the score of the current board
    //used to determine the winner
    public int score()
    {
        int countB = 0;
        int countW = 0;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++) 
            {
                if (board[i][j] == 'B')
                {
                    countB++;
                }
                else if(board[i][j] == 'W')
                {
                    countW++;
                }
            }    
        }

        int difference = 0;
        if(initial_player == 'B')
            difference = countB - countW;
        else
            difference = countW - countB;
        return difference;
    }
    //evaluates the board (used in the minimax_move function)
    //for any piece the value will be 5,
    //for an edge piece the value is 15,
    //for a corner piece the value is 25
    public int evaluation()
    {
        int score = 0;

        for (int i = 0; i < n ; i++) 
        {
            for (int j=0; j < n; j++) 
            {
                int value = 5;

                if(i == 0 || i==n-1)
                {
                    value+=10;
                }
                if(j==0 || j==n-1)
                {
                    value+=10;
                }

                if(board[i][j] == initial_player)
                {
                    score += value;
                }
                else if(board[i][j] == getOpponent(initial_player))
                {
                    score -= value;
                }        
            }    
        }

        return score;
    }

}
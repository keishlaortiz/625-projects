/*
    Keishla D. Ortiz-Lopez
    CSCE 625 - Artificial Intelligence


    Move class
*/
//holds coordinates x and y and the value (used in the minimax move function)
public class Move
{
    int x;
    int y;
    int value;

    public Move(int xx, int yy)
    {
        x = xx;
        y = yy;
        value = 0;
    }
}

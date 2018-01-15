import java.util.Arrays;

public class Board
{
  public static char EX = 'X';
  public static char OH = 'O';
  public static char BLANK = ' ';
  
  public char[][] board;
  public int rows;
  public int columns;
  
  
  // signature of a constructor is the NAME
  // and paramater type list
  
  public Board()
  { // signature is Board:no inputs
    this(3,3);  // constructor chaining 
    // calls other constructor with 3,3 asd inputs
    //System.out.println("Created default 3x3 game");      
  }
  
  public Board(int rows, int cols)// overloaded constructor
  {
    // signature is Board:int, int
    board = new char[rows][cols];
    for(int i=0; i<board.length; i+=1)
    {
      for(int j=0; j<board[0].length; j+=1)
      {
        board[i][j] = BLANK;
      }
    }
    
    this.rows = rows;  // this is reference to current object
    this.columns = cols;
    
    System.out.println("Created " + rows + "x" + cols + " game");
  }
  
  // Tic-Tac-Toe board display method
  public String display()
  {
    for(int i = 0;i < rows;i++)
    {
      for(int j = 0; j< columns;j++)
      {
        if(j<rows-1)
        {
          System.out.print(this.board[i][j] + " | ");
        }
        else if(j == rows-1)
        {
          System.out.print(this.board[i][j]);
        }
      }
      
      if(i < rows-1)
      {
        System.out.print("\n"+"###");
        for(int k = 0; k<columns-2;k++)
        {
          System.out.print("####");
        }
        System.out.print("##"+"\n");
      }
      if(i == rows-1)
      {
        System.out.println("\n");
      }
    }
    return Arrays.deepToString(board);
  }
  
  
  public boolean isValid(int row, int col)
  {
    if( row < 0 || col < 0 || col >= columns || row >= rows)
    {
      return false;
    }else if( board[row][col] != BLANK )
    {
      return false;
    }else
    {
      return true;
    }
  }
  
  public String play(int row, int col, char symbol)
  {
    this.board[row][col] = symbol;
    //System.out.println(Arrays.deepToString(board));
    return display();
  }
  
  // win method checks for the possible cases for the win 
  public boolean win()
  {
    // Check first row win
    //System.out.println("hi: "+this.board[0][0]+" "+this.board[0][1]+" "+this.board[0][2]);
    if(rows<5){
      if( board[0][0] != BLANK &&
       board[0][0] == board[0][1] &&
       board[0][1] == board[0][2]){
       //System.out.println("WINN");
       return true;
      }
      // Check second row win
      else if( board[1][0] != BLANK &&
              board[1][0] == board[1][1] &&
              board[1][1] == board[1][2]){
        return true;
      }
      // Check third row win
      else if( board[2][0] != BLANK &&
              board[2][0] == board[2][1] &&
              board[2][1] == board[2][2]){
        return true;
      }
      // Check first column win
      else if( board[0][0] != BLANK &&
              board[0][0] == board[1][0] &&
              board[1][0] == board[2][0]){
        return true;
      }
      // Check second column win
      else if( board[0][1] != BLANK &&
              board[0][1] == board[1][1] &&
              board[1][1] == board[2][1]){
        return true;
      }
      // Check third column win
      else if( board[0][2] != BLANK &&
              board[0][2] == board[1][2] &&
              board[1][2] == board[2][2]){
        return true;
      }
      // Check diagonal top left corner to bottom right corner win
      else if( board[0][0] != BLANK &&
              board[0][0] == board[1][1] &&
              board[1][1] == board[2][2]){
        return true;
      }
      // Check diagonal top right corner to bottom left corner win
      else if( board[0][2] != BLANK &&
              board[0][2] == board[1][1] &&
              board[1][1] == board[2][0]){
        return true;
      }
    }
    
    if(rows>4){
        // Check 5 by 5 first row
      if( board[0][0] != BLANK &&
              board[0][0] == board[0][1] &&
              board[0][1] == board[0][2] &&
              board[0][2] == board[0][3] &&
              board[0][3] == board[0][4]){
        return true;
      }
      // Check 5 by 5 second row
      else if( board[1][0] != BLANK &&
              board[1][0] == board[1][1] &&
              board[1][1] == board[1][2] &&
              board[1][2] == board[1][3] &&
              board[1][3] == board[1][4]){
        return true;
      }
      // Check 5 by 5 third row
      else if( board[2][0] != BLANK &&
              board[2][0] == board[2][1] &&
              board[2][1] == board[2][2] &&
              board[2][2] == board[2][3] &&
              board[2][3] == board[2][4]){
        return true;
      }
      // Check 5 by 5 forth row
      else if( board[3][0] != BLANK &&
              board[3][0] == board[3][1] &&
              board[3][1] == board[3][2] &&
              board[3][2] == board[3][3] &&
              board[3][3] == board[3][4]){
        return true;
      }
      // Check 5 by 5 fifth row
      else if( board[4][0] != BLANK &&
              board[4][0] == board[4][1] &&
              board[4][1] == board[4][2] &&
              board[4][2] == board[4][3] &&
              board[4][3] == board[4][4]){
        return true;
      }
      // Check 5 by 5 first column
      else if( board[0][0] != BLANK &&
              board[0][0] == board[1][0] &&
              board[1][0] == board[2][0] &&
              board[2][0] == board[3][0] &&
              board[3][0] == board[4][0]){
        return true;
      }
      // Check 5 by 5 second column
      else if( board[0][1] != BLANK &&
              board[0][1] == board[1][1] &&
              board[1][1] == board[2][1] &&
              board[2][1] == board[3][1] &&
              board[3][1] == board[4][1]){
        return true;
      }
      // Check 5 by 5 third column
      else if( board[0][2] != BLANK &&
              board[0][2] == board[1][2] &&
              board[1][2] == board[2][2] &&
              board[2][2] == board[3][2] &&
              board[3][2] == board[4][2]){
        return true;
      }
      // Check 5 by 5 forth column
      else if( board[0][3] != BLANK &&
              board[0][3] == board[1][3] &&
              board[1][3] == board[2][3] &&
              board[2][3] == board[3][3] &&
              board[3][3] == board[4][3]){
        return true;
      }
      // Check 5 by 5 fifth column
      else if( board[0][4] != BLANK &&
              board[0][4] == board[1][4] &&
              board[1][4] == board[2][4] &&
              board[2][4] == board[3][4] &&
              board[3][4] == board[4][4]){
        return true;
      }
      // Check 5 by 5 top left diagonal 
      else if( board[0][0] != BLANK &&
              board[0][0] == board[1][1] &&
              board[1][1] == board[2][2] &&
              board[2][2] == board[3][3] &&
              board[3][3] == board[4][4]){
        return true;
      }
      // Check 5 by 5 top right diagonal
      else if( board[0][4] != BLANK &&
              board[0][4] == board[1][3] &&
              board[1][3] == board[2][2] &&
              board[2][2] == board[3][1] &&
              board[3][1] == board[4][0]){
        return true;
      }
    }
    
    return false;
    
    
  }// end of win method

}// end of class Board



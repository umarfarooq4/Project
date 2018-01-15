public class TicTacToeApp
{
  public static void main(String[] args)
  {
    // Create Player and Board class object
    Player play = new Player();
    Board gameBoard = new Board();

    char p1Move = 'X';
    char p2Move = 'O';
    boolean flag = true;
    int count = 0;
    
    if(args.length > 0)
    {
      System.out.println("This is args[0]: " +args[0].getClass().getName());
      gameBoard = new Board(5,5);
    }
    else
    {
      gameBoard = new Board();
    }
    play.display();
    while(flag && count != (gameBoard.rows*gameBoard.rows))
    {
      play.playerMove(p1Move); 
      count++;
      //System.out.println("Win: "+gameBoard.win()+" Rows: "+gameBoard.rows);
      if(play.win() || count > (gameBoard.rows*gameBoard.rows)-1)
      {
        break;
      }
      play.playerMove(p2Move); 
      count++;
      System.out.println(gameBoard.win());
      if(play.win() || count > (gameBoard.rows*gameBoard.rows)-1)
      {
        break;
      }
     }// end of while loop
     System.out.println("Gameover.");
   }// end of main method

}// end of class TicTacToeApp
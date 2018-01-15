import java.util.Scanner;


public class Player extends Board
{
 private char player1 = 'X';
 private char player2 = 'O';

 public Board game;
 
 public void playerMove(char symbol)
 {
  // Create a Scanner object to read input
  Scanner key = new Scanner(System.in);
  String[] p1;
  int row = 0; 
  int col = 0;
  boolean flag = true;
  String move;
  
  while(flag)
  {
   System.out.print("Enter player " +symbol+ " move: ");
   move = key.nextLine();
   p1 = getMove(move);
   row = Integer.parseInt(p1[0]); 
   col = Integer.parseInt(p1[1]);
   if(isValid(row,col))
   {
    flag = false;
   }
   else
   {
    System.out.println("The move entered is invalid.");
   }
  }// end of while loop 
  play(row, col, symbol);
 }// end of playerMove method
 
 public static String[] getMove(String input)
 {
  //replaces needless chars to empty string, "2, 3" == "23"
  input = input.replaceAll("[^0-9]","");
  //converts string of numbers to array of numbers
  return input.split("");
 }
 
}// end of class Player
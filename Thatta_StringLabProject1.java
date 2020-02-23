// Niyanth Thatta
// Thatta_StringLabProject1.java
// String project 1
public class Thatta_StringLabProject1
{
  public static void main (String [] args)
  {
String one = "NiyanthThatta15"; //should be FirstLastAge
String two = "4705056802"; //should include areacellnumber w/ no spaces
String three = "Niyanth Thatta"; // should include full name with spaces
System.out.println("The first string is " + one);
System.out.println("The second string is " + two);
System.out.println("The third first string is " + three);
System.out.println("The length of the first string is " + one.length());
System.out.println("The length of the second string is " + two.length());
System.out.println("The length of the third first string is " + three.length());
System.out.println("The character at index 0 is " + one.charAt(0));
System.out.println("The characters from index 0 to index 1 for string 1 is " + one.substring(0,1));
System.out.println("The characters from index 0 to index 2 for string 2 is " + two.substring(0,2));
System.out.println ("The characters from index 0 to index 3 for string 3 is " + three.substring(0,3));
System.out.println ("The phrase Niyanth in string 1 is  at index " + one.indexOf("Niyanth"));
System.out.println ("The phrase Niyanth in string 3  is  at index " + three.indexOf("Niyanth"));
System.out.println ("Are the first and second string equal " + one.equals(two));
System.out.println ("Are the first and third string equal " + one.equals(three));
System.out.println ("The difference in the letter value when the first string and second string are different is " + one.compareTo(two));
System.out.println ("The difference in the letter value when the second string and third string are different is " + two.compareTo(three));
System.out.println ("The first string in all caps is " + one.toUpperCase());
System.out.println ("The third string in all lower caps is " +three.toLowerCase());
System.out.println ("The string monkey cocatenated to string 1 is " + one.concat("monkey"));
System.out.println("When the letter q is substituted for all A's in string 3 it results in " + three.replace('a','q'));
System.out.println("When the letter q is substituted for all A's in string 1 it results in " + one.replace('a','q'));
System.out.println ("Is the second string equal to 4705056802? " + two.equalsIgnoreCase ("4705056802"));


  }
}


                   
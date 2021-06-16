import java.util.Scanner;


class CalculadorBasico
{
	
	
public static void main(String[]	args)
{
	String operacion;
	double a, b;
	
	 Scanner user = new Scanner(System.in);
	 
	 System.out.println("primer numero...");
	 
	 	a = user.nextDouble();
	 
	 System.out.println("segundo numero...");
	 
	 	b = user.nextDouble();
	 
	 System.out.println("operacion a realizar (suma,resta,multiplicacion,division): ");
	 
	 	user.nextLine();
	 
	 	operacion = user.nextLine();
	 
	 /*
	  *	ademas de definir la op
	  *eracion con palabras, podes hacerlo con simbolos
	  */
	 
	 if(operacion.equalsIgnoreCase("suma")||operacion.equals("+")) {
		 System.out.println(a+b);
	 }
	 else if(operacion.equalsIgnoreCase("resta")||operacion.equals("-")) {
		 System.out.println(a-b);
	 }
	 else if(operacion.equalsIgnoreCase("multiplicacion")||operacion.equals("*")) {
		 System.out.println(a*b);
	 }
	 else if(operacion.equalsIgnoreCase("division")||operacion.equals("/")){
		 System.out.println(a/b);
	 }
	 else {
		 System.out.println("error");
	 }
}
	
}

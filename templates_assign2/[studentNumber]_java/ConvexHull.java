import java.io.*;

public class ConvexHull {
    
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide input file as argument");
            return;
        }
        
        for(String file:args){
		System.out.println("input file name is: "+file);	
	}
    }
}

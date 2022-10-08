import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String args[]) throws IOException{

    	int n = readInt(), dp[][] = new int[n+1][3];

    	for(int i=1; i<=n; i++) {
    		int a = readInt();
    		int b = readInt();
    		int c = readInt();
    		dp[i][0] = a + Math.max(dp[i-1][1], dp[i-1][2]);
    		dp[i][1] = b + Math.max(dp[i-1][0], dp[i-1][2]);
    		dp[i][2] = c + Math.max(dp[i-1][0], dp[i-1][1]);
    	}
    	System.out.println(Math.max(Math.max(dp[n][0], dp[n][1]), dp[n][2]));
 

    	
    }
    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
    static double readDouble() throws IOException {
        return Double.parseDouble(next());
    }
    static String readLine() throws IOException {
        return br.readLine().trim();
    }
    
    static void debug( Object o ) throws IOException {
        System.out.println( o );
    }
    
}

import java.net.*;
import java.util.Arrays;

public class SpamChecker{
    public static void main(String[] args) throws Exception{
        String IP = args[0];

        String website = ".sbl.spamhaus.org";
        String query;

        String [] split = IP.split("\\.", 0);
        System.out.println(Arrays.toString(split));

        String correct_ip = split[3] + "." + split[1] + "." + split[2] + "." + split[0];
        System.out.println(correct_ip);

        try {
            query = correct_ip + website;
            InetAddress.getByName(query);
            System.out.println(IP + " is a known spammer");
        }
        catch (Exception e) { 
            System.out.println(IP + " appears legitimate");
        }
    }
}


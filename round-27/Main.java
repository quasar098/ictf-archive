import java.io.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.util.*;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Main {
    public static void main(String[] args) throws IOException, NoSuchPaddingException, NoSuchAlgorithmException, InvalidAlgorithmParameterException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        PrintWriter pw = new PrintWriter(new FileWriter("output.txt"));
        List<Long> keys = new ArrayList<>();
        List<Long> stream = new ArrayList<>();
        //Here are my real keys!
        Random r = new Random();
        for (int i = 0; i < 8; i++) keys.add(r.nextLong());
        //Here are my fake keys!
        SlightlyMoreSecureRandom rand = new SlightlyMoreSecureRandom();
        for (int i = 0; i < 524280; i++) {
            stream.add(rand.next());
        }
        stream.addAll(keys);
        //Shuffle so that no one can find the real keys
        Collections.shuffle(stream);
        for (long i : stream) {
            pw.print(pad(Long.toHexString(i)));
        }
        pw.println();

        //Encrypting the flag using my keys
        String flag = new BufferedReader(new FileReader("flag.txt")).readLine();
        SecretKey key = generateKey(keys);
        byte[] ivBytes = new byte[16];
        new SecureRandom().nextBytes(ivBytes);
        IvParameterSpec iv = new IvParameterSpec(ivBytes);
        Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
        c.init(1, key, iv);
        byte[] enc = c.doFinal(flag.getBytes(StandardCharsets.UTF_8));
        String encHex = bytesToHex(enc);
        String ivHex = bytesToHex(ivBytes);
        pw.println("enc: "+encHex);
        pw.println("iv: "+ivHex);
        pw.flush();
        pw.close();
    }
    public static SecretKey generateKey(List<Long> keys){
        //Super weird key generation that increases the security against a brute force attack by 40,000 times!
        long key1 = (Long.rotateLeft(keys.get(0), 11)^(Long.rotateLeft(keys.get(1), 31)+Long.rotateLeft(keys.get(2), 17))+Long.rotateLeft(keys.get(3), 5))^keys.get(4)+Long.reverse(keys.get(5))^Long.max(keys.get(6), keys.get(7));
        long key2 = Long.reverse(Long.rotateRight(keys.get(0), 13)^(Long.rotateRight(keys.get(1), 49)+Long.rotateRight(keys.get(2), 19))+Long.rotateRight(keys.get(3), 35))^keys.get(6)+Long.reverse(keys.get(4))^Long.min(keys.get(7), keys.get(5));
        ByteBuffer buffer = ByteBuffer.allocate(16);
        buffer.putLong(key1);
        buffer.putLong(key2);
        return new SecretKeySpec(buffer.array(), "AES");
    }
    //Credits to https://stackoverflow.com/questions/9655181/how-to-convert-a-byte-array-to-a-hex-string-in-java
    private static final byte[] HEX_ARRAY = "0123456789abcdef".getBytes(StandardCharsets.US_ASCII);

    public static String bytesToHex(byte[] bytes) {
        byte[] hexChars = new byte[bytes.length * 2];
        for (int j = 0; j < bytes.length; j++) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = HEX_ARRAY[v >>> 4];
            hexChars[j * 2 + 1] = HEX_ARRAY[v & 0x0F];
        }
        return new String(hexChars, StandardCharsets.UTF_8);
    }
    static String pad(String s) {
        StringBuilder sBuilder = new StringBuilder(s);
        for (int i = 0; i < 16 - s.length(); i++) {
            sBuilder.insert(0, '0');
        }
        s = sBuilder.toString();
        return s;
    }
}

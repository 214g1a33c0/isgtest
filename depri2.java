import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.security.*;
import java.util.Base64;

public class WeakCryptoExample {

    public static void main(String[] args) throws Exception {

        String data = "ConfidentialData";

        MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
        byte[] sha1Hash = sha1.digest(data.getBytes());

        System.out.println("SHA1 Hash: " + Base64.getEncoder().encodeToString(sha1Hash));

        KeyGenerator keyGen = KeyGenerator.getInstance("DESede");
        keyGen.init(112);  // Weak 3DES key
        SecretKey tripleDesKey = keyGen.generateKey();

        Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, tripleDesKey);

        byte[] encrypted = cipher.doFinal(data.getBytes());

        System.out.println("3DES Encryption: " + Base64.getEncoder().encodeToString(encrypted));

        KeyPairGenerator keyGenRSA = KeyPairGenerator.getInstance("RSA");
        keyGenRSA.initialize(1024);  // Weak RSA key

        KeyPair pair = keyGenRSA.generateKeyPair();

        Cipher rsaCipher = Cipher.getInstance("RSA");
        rsaCipher.init(Cipher.ENCRYPT_MODE, pair.getPublic());

        byte[] rsaEncrypted = rsaCipher.doFinal(data.getBytes());

        System.out.println("RSA1024 Encryption: " + Base64.getEncoder().encodeToString(rsaEncrypted));
    }
}

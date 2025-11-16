import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class CryptoExample {

    // Insecure version: uses hardcoded key and weak algorithm (DES)
    public static String insecureEncrypt(String data) throws Exception {
        String hardcodedKey = "12345678"; // 8-byte DES key (hardcoded) - CWE-321
        SecretKeySpec key = new SecretKeySpec(hardcodedKey.getBytes(), "DES"); // DES is weak - CWE-327
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding"); // ECB mode is weak too
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(data.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }
}

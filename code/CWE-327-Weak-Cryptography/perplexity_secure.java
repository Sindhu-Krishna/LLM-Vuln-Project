import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class CryptoExample {

    // Secure version: reads key from environment variable and uses AES with CBC and random IV
    public static String secureEncrypt(String data) throws Exception {
        String envKey = System.getenv("AES_KEY"); // Key provided in environment - no hardcoding
        if (envKey == null || envKey.length() != 16) {
            throw new IllegalStateException("Environment AES_KEY must be set to a 16-byte value");
        }
        SecretKeySpec key = new SecretKeySpec(envKey.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");

        // Use random IV for security
        byte[] iv = new byte[16];
        java.security.SecureRandom random = new java.security.SecureRandom();
        random.nextBytes(iv);
        javax.crypto.spec.IvParameterSpec ivSpec = new javax.crypto.spec.IvParameterSpec(iv);

        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
        byte[] encrypted = cipher.doFinal(data.getBytes());

        // Prepend IV to ciphertext for use in decryption
        byte[] combined = new byte[iv.length + encrypted.length];
        System.arraycopy(iv, 0, combined, 0, iv.length);
        System.arraycopy(encrypted, 0, combined, iv.length, encrypted.length);
        return Base64.getEncoder().encodeToString(combined);
    }
}

#include <stdio.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/sha.h>

int main() {

    unsigned char key[16] = "0123456789abcdef";
    unsigned char input[] = "SecretMessage123";
    unsigned char output[128];

    AES_KEY aes_key;

    AES_set_encrypt_key(key, 128, &aes_key);
    AES_encrypt(input, output, &aes_key);

    printf("AES Encryption Complete\n");

    unsigned char hash[SHA256_DIGEST_LENGTH];

    SHA256(input, strlen((char*)input), hash);

    printf("SHA256 Hash: ");
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        printf("%02x", hash[i]);

    printf("\n");

    return 0;
}

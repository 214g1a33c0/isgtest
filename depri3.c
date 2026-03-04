#include <stdio.h>
#include <string.h>
#include <openssl/des.h>
#include <openssl/md5.h>
#include <openssl/rc4.h>

int main() {

    unsigned char data[] = "SensitiveInformation";

    unsigned char md5_digest[MD5_DIGEST_LENGTH];

    MD5(data, strlen((char*)data), md5_digest);

    printf("MD5 Digest: ");
    for(int i=0;i<MD5_DIGEST_LENGTH;i++)
        printf("%02x", md5_digest[i]);
    printf("\n");

    DES_cblock key = "weakkey";
    DES_key_schedule schedule;

    DES_set_key_unchecked(&key, &schedule);

    DES_cblock input = "12345678";
    DES_cblock output;

    DES_ecb_encrypt(&input, &output, &schedule, DES_ENCRYPT);

    printf("DES Encryption Complete\n");

    RC4_KEY rc4_key;
    unsigned char rc4_out[256];

    RC4_set_key(&rc4_key, strlen("rc4weakkey"), (unsigned char *)"rc4weakkey");
    RC4(&rc4_key, strlen((char*)data), data, rc4_out);

    printf("RC4 Encryption Complete\n");

    return 0;
}

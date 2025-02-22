import pysui.sui.sui_crypto

# 生成sui的私钥、地址

def generate_sui_key(nums):

    SignatureScheme = pysui.sui.sui_crypto.SignatureScheme.ED25519
    while nums > 0:
        mnemonic_phrase, keypair, address = pysui.sui.sui_crypto.create_new_address(keytype=SignatureScheme)
        private_key = keypair.private_key
        public_key = keypair.public_key
        address = address.address

    # 将助记词、公钥、地址保存到json文件中
        with open('sui_key.json', 'a') as f:
            f.write(f'{{"mnemonic_phrase": "{mnemonic_phrase}", "private_key": "{private_key}", "public_key": "{public_key}", "address": "{address}"}}\n')
        nums -= 1


if __name__ == '__main__':

    generate_sui_key(10)




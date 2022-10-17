from time import sleep

class SimpleEncryption:
    def __init__(self, key_path: str, text_path: str, save_path: str) -> None:
        self.decoded_keys = self.__binaryToBytes(key_path)
        self.decoded_text = self.__binaryToBytes(text_path)
        self.save_path = save_path

    __binaryToBytes = lambda _, path: open(path, 'rb').read()

    def encrypt(self):
        mapped_keys = {}
        encrypted = []
        result = ""

        for i, k in enumerate(self.decoded_keys, start=0):
            mapped_keys[i] = k

        for _, j in enumerate(self.decoded_text):
            encrypted.append(mapped_keys[j])

        for _, m in enumerate(encrypted):
            result += (str(m) + "🥟")
        
        print(f'{"SAVING RESULTS TO `" + self.save_path + "RESULT_ENCODED.txt`":.^20}')
        sleep(1)
        open(f"{self.save_path}RESULT_ENCODED.txt", "w+").write(result.strip())
        return result

class SimpleDecryption:
    def __init__(self, key_path: str, text_path: str, save_path: str) -> None:
        self.decoded_keys = self.__binaryToBytes(key_path)
        self.encoded_text = open(text_path, "r").read()
        self.save_path = save_path

    __binaryToBytes = lambda _, path: open(path, 'rb').read()
    __filter = lambda _, unfiltered_list: list(filter(lambda value: value != "", unfiltered_list))

    def decrypt(self):
        mapped_keys = {}
        encrypted = self.__filter(self.encoded_text.split('🥟'))
        decrypted = []

        for i, k in enumerate(self.decoded_keys, start=0):
            mapped_keys[k] = i

        for _, j in enumerate(encrypted, start=0):
            decrypted.append(mapped_keys[int(j)])

        print(f'{"SAVING RESULTS TO `" + self.save_path + "RESULT_DECODED`":.^20}')
        sleep(1)
        open(f"{self.save_path}RESULT_DECODED", "wb").write(result:=bytearray(decrypted))
        return result


def main(path): 
    print(f'{"START":-^40}')
    # Test 1
    f = SimpleEncryption(path + "/" + "key", path + "/" + "plain_text", path + "/")
    f.encrypt()

    # Test 2
    t = SimpleDecryption(path + "/" + "key", path + "/" + "RESULT_ENCODED.txt", path + "/")
    t.decrypt()
    print(f'{"END":-^40}')


my_path = input("Please provide the directory where 'key' and 'plain_text' exist: ")
main(my_path) if len(my_path) >= 1 else main('test')
import json,os

# raw data from 
# https://sandilands.info/sgordon/teaching/css322y08s2/protected/CSS322Y08S2E02-Final-Exam-Answers.pdf


def create_folder_if_not_exists(d):
    if not os.path.exists(d):
        os.makedirs(d)


def main():
    question_list = [
        'What function can be used to convert a hash function into a MAC function? Select one from: MD5, SHA1, HMAC, Triple DES, RSA, None of the above',
        'Assume a user had a 10-character password. Which would you consider the strongest against a dictionary attack? Select one from: a) Random characters, b) Combination of two English words, c) Pronounceable string (without dictionary words), d) Combination of names of people, e) Words with a mixture of upper and lower case characters, f) Words combined with numbers and special characters',
        'If Transport Layer Security is used to secure data (e.g. web pages) between a client and server, TLS uses (select one from): a) Public key algorithms for data confidentiality and MD5 or SHA1 for data integrity, b) Symmetric key algorithms for key exchange and message authentication codes for authentication, c) Message authentication codes for data integrity and symmetric key algorithms for data confidentiality, d) Public key algorithms for key exchange and Diffie-Hellman for data integrity, e) None of the above',
        'Which technology is most appropriate to create a VPN? Select on from: a) TLS, b) IPsec, c) DDoS, d) SSH, e) RSA, f) None of the above',
        'Software the replicates itself and sends the copies to other computers is best described as a (select one from): a) Logic bomb, b) Trojan horse, c) Rootkit, d) Exploit, e) Worm, f) Backdoor ',
        'A malicious user in a buffer overflow attack aims to (select one from): a) Overwrite the existing instruction pointer with malicious code, b) Overwrite the existing instruction pointer with NOP instructions, c) Overwrite the existing instruction pointer with a new instruction pointer, d) Overwrite the program stack with the malicious code, e) Overwrite the program stack with NOP instructions, f) Overwrite the program stack with a new instruction pointer',
        'What standard is used to describe digital certificates? Select one from: a) X.509, b) IPsec, c) TLS, d) IETF, e) MD5, f) RSA',
        'To allow confidential access to web sites using HTTPS, web browsers most often use (select one from): a) IPsec, b) TLS, c) MD5, d) SSH, e) SHA-1, f) None of the above',
        'Using symmetric key encryption to successfully provide authentication relies upon (select one from): a) The sender encrypting with a private key, b) The sender encrypting with a public key, c) The sender sending an encrypted copy of the shared secret key, d) The recipient being able to identify messages encrypted with the wrong key, e) The recipient being able to make their shared secret key public, f) The recipient being able to perform a hash operation on the received ciphertext',
        'A DoS makes a system (network and/or computers) unavailable for normal users to use. Explain how the ICMP attack achieves this, including what does it make “unavailable”',
        'Explain the difference between a direct DDoS attack and a reflector DDoS attack',
        'State two advantages of a reflector DDoS attack (compared to direct DDoS attack).',
        'Describe the one-way property of hash functions.',
        'Describe the weak collision resistance property of hash functions',
        'Describe the strong collision resistance property of hash functions.',
        'Explain why MAC-based authentication cannot be used as a digital signature.',
        'Describe two advantages of using tunneling mode (versus transport mode) of IPsec.',
    ]
    
    answer_list = [
        'HMAC',
        'a) Random characters',
        'c) Message authentication codes for data integrity and symmetric key algorithms for data confidentiality',
        'b) IPsec',
        'e) Worm',
        'c) Overwrite the existing instruction pointer with a new instruction pointer',
        'a) X.509',
        'b) TLS',
        'd) The recipient being able to identify messages encrypted with the wrong key',
        'The ICMP attack uses up network capacity leading up to the Target (or the network of the Target), thereby making that network capacity unavailable. In addition, the processing of ICMP ECHO replies may use up processing (CPU) capacity of the Target, making that host unavailable',
        'A direct DDoS attack involves hosts under the control of the attacker directly performing an attack (by sending messages) on a target. A reflector DDoS attack involves hosts under control sending messages to uncontrolled (normal) hosts in the network, that then perform an attack on the target',
        '1. Potential of many more nodes participating in the attack, since the attacker can use uninfected nodes. 2. Harder for target to identify the attacker because traffic comes from many random uninfected nodes.',
        'Computationally hard to compute the inverse of a hash function',
        'Given a message X and its hash value A (H(X) = A), computationally hard to find another message Y such that H(X) = H(Y) = A.',
        'Computationally hard to find two messages, X and Y, such that their hash values are the same, i.e. H(X) = H(Y).',
        'A MAC function uses a shared secret key. A message authenticated with a MAC function confirms that the message was generated by either the of the parties that has the secret. It does not confirm which of the two parties generated the message (which is the purpose of a digital signature).',
        'IPsec only needs to be configured on routers, not on all PCs; hide the IP addresses of the originating and destination nodes.',
    ]

    print(len(question_list))
    print(len(answer_list))
    assert(len(question_list)==len(answer_list))

    result = []
    for i in range(len(question_list)):
        q = question_list[i]
        a = answer_list[i]
        result.append({'question':q, 'answer':a})

    create_folder_if_not_exists('dataset/')
    with open('dataset/sec_exam_01.json', 'w', encoding='utf-8') as fw:
        json.dump(result, fw, indent=4, ensure_ascii=False)

    # load
    with open('dataset/sec_exam_01.json', 'r', encoding='utf-8') as fr:
        d = json.load(fr)
        print(d)

if __name__=='__main__':
    main()
    
    

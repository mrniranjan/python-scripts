import base64
from sys import argv
import nss.nss as nss

def generate_sym_key():
    """ This Function generate Symmetric key and nonce data """    
    ## Initialize NSS Database opens temporary database and the internal PKCS #112 module
    nss.nss_init_nodb()
    ## Mechanism to be used for symmetric key 
    mechanism = nss.CKM_DES_CBC_PAD
    # From the Soft token that we initialized get slot to generate symmetric key
    slot = nss.get_best_slot(mechanism)
    # Generate a symmetric key on the pk11 slot, The sym_key is of type PK11SymKey
    sym_key = slot.key_gen(mechanism, None, slot.get_best_key_length(mechanism))

    # Generate Nonce 
    iv_length = nss.get_iv_length(mechanism)

    if iv_length > 0:
        # Generate Nonce
        iv_data = nss.generate_random(iv_length)
        # Pass this random data to NSS SecItem
        iv_si = nss.SecItem(iv_data)
        # Use the Data passed to SecItem for initialization Vector 
        iv_param = nss.param_from_iv(mechanism, iv_si)
        # Random data is converted to hex
        pki_nonce = nss.data_to_hex(data=iv_data, separator=":")
        #print "generated %d bytes initialization vector: %s" % (iv_length, pki_nonce)
    
        # Create a Symmetric key Context using the Symmetric key, nonce  The context should be 
        # used for encrypt as well as decrypt
        encoding_ctx = nss.create_context_by_sym_key(mechanism, nss.CKA_ENCRYPT, sym_key, iv_param)
        decoding_ctx = nss.create_context_by_sym_key(mechanism, nss.CKA_DECRYPT, sym_key, iv_param)
    #return the symmetric key, nonce data, encoding context and decoding context to encrypt and 
    # decrypt
    return sym_key, pki_nonce, encoding_ctx, decoding_ctx

def get_public_key(transport_cert):
    """ This function returns public key of the transport cert which will be 
        used to wrap the session key """
    # First convert from PEM to DER Format
    #transport_cert_der =  nss.base64_to_binary(transport_cert)
    # Read the contents of the file 
    certItem = nss.read_der_from_file(transport_cert, ascii=True)
    # We need to have an Object of nss.Certificate
    CertObject = nss.Certificate(certItem)
    # Get the public Key from the cert
    public_key = CertObject.subject_public_key_info.public_key
    return public_key

def wrap_skey_with_pub_key(transport_pub_key, sym_key):
    """ This function wraps the Session key with Public key 
        of Transport cert """

    mechanism = nss.CKM_DES_CBC_PAD
    wrapped_data =  nss.pub_wrap_sym_key(mechanism, transport_pub_key, sym_key)
    session_key_wrapped_transport_cert = wrapped_data.to_hex()
    return session_key_wrapped_transport_cert
    
def main():

    # Save the transport path in transport_cert
    transport_cert = './transport.pem'
    
    # Generate Symmetric key, nonce, Encoding and Decoding contexts
    sym_key, pki_nonce, encoding_ctx, decoding_ctx = generate_sym_key()

    # Plain text that will be encrypted using the encoding context
    plain_text = 'EncryptME'

    # Encrypt the Plain text using encoding context
    cipher_text = encoding_ctx.cipher_op(plain_text)
    # Add Digest to the Encrypted Text
    cipher_text += encoding_ctx.digest_final()
    # Do a base 64 of the Encrypted Text 
    base64_wrapped_data = base64.encodestring(cipher_text)

    #print "Cipher text:\n%s" % (nss.data_to_hex(data=cipher_text, separator=":"))
    #print "session_key_wrapped_secret:", base64_wrapped_data


    # To Decrypt the Encoding text pass the cipher text to decoding context    
    decoded_text = decoding_ctx.cipher_op(cipher_text)
    decoded_text += decoding_ctx.digest_final()
    #print "Decoded Text\n%s" % (decoded_text)

    # Now We want need public key of transport Cert , which will be used to wrap the 
    # the symmetric key    
    
    transport_public_key = get_public_key(transport_cert)
    
    # Use the transport cert and symmetric key to wrap symmetric key with transport Cert
    wrapped_skey_with_pubkey = wrap_skey_with_pub_key(transport_public_key, sym_key)
    base64_wrap_skey = base64.encodestring(wrapped_skey_with_pubkey)

    ## Print the data:
    print "Base64 Encoded nonce data:\n", base64.encodestring(pki_nonce)
    print "\n"
    print "Base64 Encoded private data encrypted with session key\n", base64_wrapped_data
    print "\n"
    print "Base64 Encoded Session key wrapped with Transport Cert\n", base64_wrap_skey
     
    del encoding_ctx
    del decoding_ctx

if __name__ == '__main__':
    main()

require 'openssl'
require 'base64'
def decryptPassword()
    file_contents = File.read(ARGV[0])
    filename = ARGV[1]
    key = OpenSSL::PKey::RSA.new(File.read("key.pem"))
    # decrypt the password
    password = key.private_decrypt(Base64.decode64(file_contents))
    puts "The password is #{password}"
    # return password to the python script 
    return password
end
decryptPassword()
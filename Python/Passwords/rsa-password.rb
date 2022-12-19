require 'openssl'
require 'base64'
password = ARGV[0] 
filename = ARGV[1]
bits = ARGV[2]
# check if the user has entered the password and the file name
if password == nil or filename == nil or bits == nil
    puts "Usage: ruby rsa-password.rb password filename bits"
    exit
end
File.new(filename, "w")
File.new("key.pem", "w")
# time key generation
start = Time.now
key = OpenSSL::PKey::RSA.new(bits.to_i)
File.write("key.pem", key.to_pem)
finish = Time.now
puts "Key generation took #{finish - start} seconds"
# encrypt the password
encryptedPassword = key.public_encrypt(password)
# write the encrypted password to a file
File.write(filename, Base64.encode64(encryptedPassword))
puts "The encrypted password is saved in #{filename}"

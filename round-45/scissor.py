flag = 'REDACTED'
ciphertext = b''
for i in flag:
	ciphertext += chr(ord(i)+0x1337).encode()
print(f'ciphertext = {ciphertext.hex()}')

# ciphertext = e18ea0e18e9ae18eabe18e9de18eb2e18e9ae18daae18ea9e18daee18da8e18e9de18da8e18daae18e9be18e96e18da8e18daae18daae18daee18e96e18e9fe18dabe18eafe18da7e18ea9e18d98e18eb4
str = 'X-DSPAM_Confidence:0.10050805'

index_before_num = str.find(':')

number = float(str[index_before_num+1:])

print(number)


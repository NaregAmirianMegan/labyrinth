# def parse_text(content, char_limit):
# 	lines = []
# 	words_iter = iter(content.split(" "))
# 	curr_word = next(words_iter)
# 	try:
# 		while True:
# 			char_count = 0
# 			curr_line = ""
# 			while True:
# 				char_count += len(curr_word) + 1
# 				curr_line += curr_word + " "
# 				if char_count >= char_limit:
# 					lines.append(curr_line)
# 					break
# 				else:
# 					curr_word = next(words_iter)
# 	except StopIteration:
# 		pass	
# 	return lines

def parse_text(content, char_limit):
	sentences = []
	words = content.split(" ")
	while words:
		curr_sentence = ""
		char_count = 0
		for word in words[:]:
			char_count += len(word) + 1
			if char_count <= char_limit:
				curr_sentence += word + " "
				words.remove(word)
				if not words:
					sentences.append(curr_sentence)
					break
			else:
				sentences.append(curr_sentence)
				break
	return sentences

test_string = "hello world, how are you today? I've been better. What do you think?"
print(parse_text(test_string, 40))
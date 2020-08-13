# Подключение библиотеки
import random

# Функция для изучения слов
def learn_words():
	count_words = sum(1 for line in open('words.txt', 'r')) # Переменная хранит в себе количество слов в списке

	print(f'\nВсего {count_words} слов!\n')

	all_eng_words = [] # Список с английскими словами в списке
	all_rus_words = [] # Список с переводом английских слов из списка

	f = open('words.txt', 'r') # Открыть список слов
	for line in f.readlines(): # Прочитать каждую строку
		all_eng_words.append((line.split(' __ ')[0])) # Разделить английское слово и его перевод
		all_rus_words.append((line.split(' __ ')[1]).split(', ')) # Если у слова несколько значений, значит разделить их по запятым
	
	dict_words = dict(zip(all_eng_words, all_rus_words)) # Объединить списки словарь

	using_words = [] # Слова, которые уже были повторены

	while len(using_words) != len(dict_words): # Пока количество повторенных слов не равно количеству всех слов в списке (пока не все слова повторены)
		word_learn = random.choice(list(dict_words.items()))[0] # Выбрать рандомное английское слово из словаря всех слов
		if word_learn in using_words: # Если слово уже было использовано, то пропустить остальное тело цикла и начать цикл заново
			continue
		else: # Если это новое слово
			translate_word = input(f'Как переводится слово «{word_learn}»: ')
			translated_word = dict_words[word_learn] # Список слов-переводов
			translated_word = [i.replace('\n', '') for i in translated_word] # Убрать все переносы строк в словах-переводах
			if translate_word in translated_word: # Если перевод пользователя совпал с переводом в списке (если перевод оказался правильным)
				using_words.append(word_learn) # Добавить это слово в список повторенных слов
				print(f'Правильно! Осталось проверить {len(dict_words) - len(using_words)} слов!\n')
			else:
				print(f'Неправильно! Попробуйте снова\n')

# Функция добавки слов в список
def add_word():
	eng_word = input('Введите английское слово: ')
	rus_translate = input('Введите русский перевод: ')
	if eng_word == '' and rus_translate == '': # Активировать режим изучения слов
		learn_words()

	else:
		# Добавить эти слова в список (основной и бэкап)
		f = open('words.txt', 'a')
		f.write(f'{eng_word} __ {rus_translate}\n')
		f.close()

		f = open('words (backup).txt', 'a')
		f.write(f'{eng_word} __ {rus_translate}\n')
		f.close()

		print(f'\nСлово «{eng_word}» добавлено!\n')

# Постоянно активировать функцию добавления новых слов
while True:
	add_word()
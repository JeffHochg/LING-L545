import networkx as nx
import json
import matplotlib.pyplot as plt


def recursion(wordIN,langcode,num, graph):
	#get word from dictionaries	
	if langcode == "en":
		try:
			word = eng[wordIN]
		except:
			return
	elif langcode == "de":
		try:
			word = ger[wordIN]
		except:
			return
	#end case
	if int(num) == 1:
		for dictionary in word:
			if 'translations' in list(dictionary.keys()):
				for translation in dictionary["translations"].keys():
					if isinstance(dictionary["translations"][translation], list):
						for newWord in dictionary["translations"][translation]:
							graph.add_edge(newWord, wordIN, label = translation)
					else:
						graph.add_edge(dictionary["translations"][translation], wordIN, label = translation)
			else:
				graph.add_node(dictionary["word"])
	else: 
	#continutation case
		#check if node & edge already exist
		for dictionary in word:
			if 'translations' in list(dictionary.keys()):
				for translation in dictionary["translations"].keys():
					if isinstance(dictionary["translations"][translation], list):
						if langcode == "en":
							for newWord in dictionary["translations"][translation]:
								G.add_edge(wordIN, newWord, label = translation)
								recursion(newWord, "de", int(num) - 1, graph)
						else:
							for newWord in dictionary["translations"][translation]:
								G.add_edge(wordIN, newWord, label = translation)
								recursion(newWord, "en", int(num) - 1, graph)
					else:
						if langcode == "en":
							G.add_edge(wordIN, dictionary["translations"][translation], label = translation)
							recursion(dictionary["translations"][translation], "de", int(num) - 1, graph)
						else:
							G.add_edge(wordIN, dictionary["translations"][translation], label = translation)
							recursion(dictionary["translations"][translation], "en", int(num) - 1, graph)
			else:
				graph.add_node(dictionary["word"])
if __name__ == "__main__":
	G = nx.Graph()

        #load translation files
        #English translations
	with open ("translations.txt", "r") as f:
		eng = json.load(f)
	#German translations
	with open ("translationsG.txt", "r") as f:
		ger = json.load(f)

	wordIN = input()
	langcode = input()
	num = input()
	recursion(wordIN, langcode, num, G)
	print(nx.write_network_text(G))
	pos = nx.spring_layout(G)
	plt.figure(figsize=(19,10))
	nx.draw_networkx(G)
	nx.draw_networkx_edge_labels(G, pos, rotate = False)
	plt.savefig("Graph.png")

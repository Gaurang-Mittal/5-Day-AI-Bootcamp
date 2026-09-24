import wordcloud 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


text = "I am deeply interested in technology and enjoy exploring how computers, software, networks, and intelligent systems work. My major interests include **cybersecurity, artificial intelligence, machine learning, backend development, ethical hacking, and software engineering**. I particularly enjoy working with **Python, C++, FastAPI, PostgreSQL, SQL, Docker, Linux, APIs, Git, and computer networks**. I like building practical projects that solve real-world problems and help me understand concepts through hands-on experience. I am also fascinated by **web security, authentication, JWT, penetration testing, vulnerability analysis, network security, and secure application development**. Artificial intelligence is another major area of interest, especially **large language models, computer vision, AI agents, RAG systems, and AI security**. I enjoy participating in **hackathons**, experimenting with new technologies, developing prototypes, and turning ideas into working applications. I am interested in **data science, visualization, automation, cloud computing, and DevOps** as well. Beyond technical skills, I enjoy **problem solving, logical thinking, continuous learning, innovation, startups, and entrepreneurship**. My long-term goal is to become highly skilled at the intersection of **AI and cybersecurity**, while building impactful products and gaining strong practical experience. I believe consistent learning, experimentation, and building projects are the best ways to grow in technology."


words = word_tokenize(text.lower())
# print(words)

word_frequencies = Counter(words)
# print(word_frequencies)


wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords.words('english')).generate_from_frequencies(word_frequencies)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('wordcloud.png', bbox_inches='tight')
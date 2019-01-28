Material for [the workshop at Appled Machine Learning Days 2019](https://www.appliedmldays.org/): "Machine Learning for fake news detection: theory and practice." Any content of this repository before the 27th January 2019 is subject to change.


### Challenge: 
https://github.com/FakeNewsChallenge/fnc-1
Dataset is provided in this repository.

## Downloading pickles (to speed up computation)
~~~
curl https://www.dropbox.com/s/bgfpgko57vicqj2/trainingdatatokens.pkl?dl=0 -L -o trainingdatatokens.pkl
curl https://www.dropbox.com/s/o38caqmlcehgq85/data_tfidf.pkl?dl=0 -L -o data_tfidf.pkl
~~~

### Getting started

1. Install Anaconda (miniconda would suffice)
2. Import the environment from the .yml file:

~~~
conda env create -f amld.yml
~~~

3. Activate the environment
~~~
source activate amld
~~~

### Learning more / Resources
#### Fake News Guide
http://www.cits.ucsb.edu/fake-news    

#### Books
Introduction to IR/NLP – https://nlp.stanford.edu/IR-book/information-retrieval-book.html     
Introduction to deep learning – https://github.com/janishar/mit-deep-learning-book-pdf      

#### Courses
Deep NLP (Stanford) - http://cs224d.stanford.edu/ or http://web.stanford.edu/class/cs224n/     
Video Lectures (YouTube) – https://www.youtube.com/playlist?list=PLqdrfNEc5QnuV9RwUAhoJcoQvu4Q46Lja     


### Schedule
9:00 - 9:15: Introduction   
9:15 - 9:30: Problem statement     
9:30 - 9:35: Dataset     
9:35 - 10:30: Introduction to Natural Language Processing    
10:30 - 10:45: Coffee Break / Technical issues    
10:45 - 12:00: Hands on session (introduction to general techniques)    
      
12:00 - 14:00: Lunch break / Technical issues      
    
14:00 - 15:15: Introduction to Neural networks      
15:15 - 15:30: Coffee Break / Technical issues     
15:30 - end: Discussion / hands on session (modifying/exploring a fake news detection engine)     

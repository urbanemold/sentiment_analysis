# sentiment_analysis
librerie necessarie :
1- NLTK (natural lenguage toolkik)
2-schikit learn (modelli machine-learning)
3-tweetpy (per la twitter API)

eseguire gli script nell'ordine :
1- sentiment_mod (questo script acquisirà i data-set da negative.txt e positive.txt, preparera i classifier e li salverà per una                   esecuzione più rapida del secondo modulo), è sufficiente eseguirlo solo la prima volta

2-text_classification_module, twetter_income, graph_drawing (dovrebbero essere in esecuzione insieme), 

in alternativa:
1- sentiment_mod (questo script acquisirà i data-set da negative.txt e positive.txt, preparera i classifier e li salverà per una                   esecuzione più rapida del secondo modulo), è sufficiente eseguirlo solo la prima volta

2-text_classification_module, twetter_income (devono essere in esecuzione insieme) 

3-graph_drawing (disegno del grafico)

NB: il modulo che gestisce la API di twitter non dovrebbe essere continuamente chiuso e riaperto, in quanto twitter fornisce una stream-API quindi pensata per restare attiva e quindi, se le connessioni sono ripetute, si verrà bloccati da twitter.
